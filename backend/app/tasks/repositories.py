from typing import Self

from beanie import PydanticObjectId, exceptions

from app.tasks.entities import CreateTaskEntity, UpdateTaskEntity
from app.tasks.models import Task


class TaskRepository:
    def __init__(self: Self):
        pass

    async def create_task(self: Self, data: CreateTaskEntity) -> Task:
        return await Task(
            name=data.name,
            description=data.description,
            start_datetime=data.start_datetime,
            due_datetime=data.due_datetime,
            next_follow_up_datetime=data.next_follow_up_datetime,
            company=data.company_id,
            assignee=data.assignee_user_id,
        ).create()

    async def get_task_by_id(self: Self, task_id: PydanticObjectId) -> Task | None:
        return await Task.get(task_id)

    async def get_tasks_by_user_id(self: Self, user_id: PydanticObjectId) -> list[Task]:
        return await Task.find_many(Task.assignee.id == user_id)

    async def get_tasks_by_company_id(
        self: Self, company_id: PydanticObjectId
    ) -> list[Task]:
        return await Task.find_many(Task.company.id == company_id).to_list()

    async def update_task(
        self: Self, task_id: PydanticObjectId, updates: UpdateTaskEntity
    ) -> Task:
        task = await self.get_task_by_id(task_id)
        if not task:
            raise exceptions.DocumentNotFound()

        mongo_updates = {}
        if updates.new_comment:
            await task.update({"$push": {"comments": updates.new_comment}})

        if (
            updates.start_datetime
            or updates.due_datetime
            or updates.is_completed is not None
        ):
            mongo_updates = {}
            if updates.start_datetime:
                mongo_updates["start_datetime"] = updates.start_datetime
            if updates.next_follow_up_datetime:
                mongo_updates["next_follow_up_datetime"] = updates.start_datetime
            if updates.due_datetime:
                mongo_updates["due_datetime"] = updates.due_datetime
            if updates.is_completed is not None:
                mongo_updates["is_completed"] = updates.is_completed
            await task.set(mongo_updates)

        return await self.get_task_by_id(task_id)
