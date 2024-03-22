from beanie import PydanticObjectId

from app.tasks.entities import CreateTaskEntity, UpdateTaskEntity
from app.tasks.repositories import TaskRepository


async def update_task(task_id: PydanticObjectId, updates: UpdateTaskEntity) -> str:
    task_repo = TaskRepository()
    updated_task = await task_repo.update_task(task_id, updates)
    return f"The task was updated and here is the updated task details:\n{updated_task.to_readable_string()}"


async def create_new_task_for_self(data: CreateTaskEntity) -> str:
    task_repo = TaskRepository()
    new_task = await task_repo.create_task(data)
    return f"A New task was created and here are the details:\n{new_task.to_readable_string()}"


async def get_tasks_assigned_to_a_user(user_id: PydanticObjectId) -> str:
    task_repo = TaskRepository()
    tasks = await task_repo.get_tasks_by_user_id(user_id)
    return "\n----\n".join([task.to_readable_string() for task in tasks])
