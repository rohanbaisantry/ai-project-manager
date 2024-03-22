import json
import time
from typing import Self

import openai
from beanie import PydanticObjectId

from app.tasks.entities import CreateTaskEntity, UpdateTaskEntity
from app.tasks.models import Task
from app.utils.openai.functions import (
    create_new_task_for_self,
    get_tasks_assigned_to_a_user,
    update_task,
)


class AssistantManager:
    assistant_id = ""

    async def __init__(
        self: Self,
        user_id: PydanticObjectId,
        company_id: PydanticObjectId,
        thread_id: str | None = None,
    ):
        self.client = openai.AsyncOpenAI()
        self.model = "gpt-3.5-turbo-16k"
        self.assistant = await self.client.beta.assistants.retrieve(
            assistant_id=AssistantManager.assistant_id
        )
        self.thread = await self.create_or_get_thread(thread_id)
        self.user_id = user_id
        self.company_id = company_id

    async def create_or_get_thread(self: Self, thread_id: str):
        if not thread_id:
            return await self.client.beta.threads.create()
        return await self.client.beta.threads.retrieve(thread_id=thread_id)

    async def add_message_to_thread(self, role, content):
        await self.client.beta.threads.messages.create(
            thread_id=self.thread.id, role=role, content=content
        )

    async def run_assistant(self: Self, instructions: str):
        return await self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
            instructions=instructions,
        )

    async def get_latest_system_response(self: Self) -> str:
        messages = await self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )
        last_message = messages.data[0]
        response = last_message.content[0].text.value
        if last_message.role != "assistant":
            raise BrokenPipeError(
                "Last message was not from the system, there was an error"
            )
        return response

    async def call_required_functions(self: Self, run, required_actions):
        tool_outputs = []

        for action in required_actions["tool_calls"]:
            func_name = action["function"]["name"]
            arguments = json.loads(action["function"]["arguments"])

            if func_name == "get_tasks_assigned_to_a_user":
                output_str = await get_tasks_assigned_to_a_user(user_id=self.user_id)
                tool_outputs.append(
                    {"tool_call_id": action["id"], "output": output_str}
                )
            elif func_name == "update_task":
                output_str = await update_task(
                    task_id=PydanticObjectId(arguments["task_id"]),
                    updates=UpdateTaskEntity(
                        new_comment=arguments["comment"],
                        is_completed=arguments["is_completed"],
                        due_datetime=arguments["due_datetime"],
                        start_datetime=arguments["start_datetime"],
                        next_follow_up_datetime=arguments["next_follow_up_datetime"],
                    ),
                )
                tool_outputs.append(
                    {"tool_call_id": action["id"], "output": output_str}
                )
            elif func_name == "create_new_task_for_self":
                output_str = await create_new_task_for_self(
                    task_id=PydanticObjectId(arguments["task_id"]),
                    updates=CreateTaskEntity(
                        name=arguments["comment"],
                        description=arguments["is_completed"],
                        due_datetime=arguments["due_datetime"],
                        start_datetime=arguments["start_datetime"],
                        next_follow_up_datetime=arguments["next_follow_up_datetime"],
                        company_id=self.company_id,
                        user_id=self.user_id,
                    ),
                )
                tool_outputs.append(
                    {"tool_call_id": action["id"], "output": output_str}
                )
            else:
                raise ValueError(f"Unknown function: {func_name}")

        print("Submitting outputs back to the Assistant: ", json.dumps(tool_outputs))
        await self.client.beta.threads.runs.submit_tool_outputs(
            thread_id=self.thread.id, run_id=run.id, tool_outputs=tool_outputs
        )

    async def wait_for_completion(self: Self, run) -> str:
        while True:
            time.sleep(1)
            run_status = await self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id, run_id=run.id
            )
            print(f"RUN STATUS:: {run_status.model_dump_json(indent=4)}")

            if run_status.status == "completed":
                return await self.get_latest_system_response()

            if run_status.status in ["cancelling", "cancelled", "failed", "expired"]:
                raise Exception("Failed to respond")

            if run_status.status == "requires_action":
                print("FUNCTION CALLING NOW...")
                await self.call_required_functions(
                    run=run,
                    required_actions=run_status.required_action.submit_tool_outputs.model_dump(),
                )

    async def process_user_message_and_get_system_response(
        self: Self, user_message: str
    ) -> str:
        self.add_message_to_thread(role="user", content=user_message)
        message_continuation_instruction = "Continue the conversation and use the required tools for updating tasks, creating tasks, and fetching tasks."
        run = self.run_assistant(message_continuation_instruction)
        return self.wait_for_completion(run)

    async def send_follow_up_message(self: Self, task: Task) -> str:
        task_str = task.to_readable_string()
        follow_up_message_instruction = f"Here is some data about a task\n{task_str}\n\nWrite a message following up to the user about the task. Base your answer on the task's name, description, due_date, and comments. Be very clear and use very simple english in what you are saying so that the user does not misinterpret the message. Also, be polite and keep the message brief."
        run = self.run_assistant(follow_up_message_instruction)
        return self.wait_for_completion(run)


# manager.create_assistant(
#   name="News Summarizer",
#   instructions="You are a personal article summarizer Assistant who knows how to take a list of article's titles and descriptions and then write a short summary of all the news articles",
#   tools=[
#       {
#           "type": "function",
#           "function": {
#               "name": "get_news",
#               "description": "Get the list of articles/news for the given topic",
#               "parameters": {
#                   "type": "object",
#                   "properties": {
#                       "topic": {
#                           "type": "string",
#                           "description": "The topic for the news, e.g. bitcoin",
#                       }
#                   },
#                   "required": ["topic"],
#               },
#           },
#       }
#   ],
# )
