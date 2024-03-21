from typing import Self

from app.tasks.entities import CreateTaskEntity, UpdateTaskEntity
from app.tasks.models import Task
from beanie import PydanticObjectId, exceptions


class TaskRepository:
    def __init__(self: Self):
        pass

    async def create_task(self: Self, data: CreateTaskEntity) -> Task:
        return await Task(
            name=data.name,
            description=data.description,
            start_datetime=data.start_datetime,
            end_datetime=data.end_datetime,
            next_follow_up_datetime=data.next_follow_up_datetime,
            company=data.company_id,
            asignee=data.asignee_user_id,
        ).create()

    async def get_task_by_id(self: Self, task_id: PydanticObjectId) -> Task | None:
        return await Task.get(task_id)

    async def get_tasks_by_user_id(self: Self, user_id: PydanticObjectId) -> list[Task]:
        return await Task.find_many(Task.asignee == user_id)

    async def get_tasks_by_company_id(
        self: Self, company_id: PydanticObjectId
    ) -> list[Task]:
        return await Task.find_many(Task.company == company_id).to_list()

    async def update_task(
        self: Self, task_id: PydanticObjectId, updates: UpdateTaskEntity
    ) -> Task:
        task = await self.get_task_by_id(task_id)
        if not task:
            raise exceptions.DocumentNotFound()

        mongo_updates = {}
        if updates.new_comment:
            mongo_updates["$push"] = {"comments": updates.new_comment}
        if updates.is_completed:
            mongo_updates["$set"] = {"is_completed": updates.is_completed}
        if updates.start_datetime or updates.end_datetime:
            mongo_updates["$set"] = {}
        if updates.start_datetime:
            mongo_updates["$set"]["start_datetime"] = updates.start_datetime
        if updates.next_follow_up_datetime:
            mongo_updates["$set"]["next_follow_up_datetime"] = updates.start_datetime
        if updates.end_datetime:
            mongo_updates["$set"]["end_datetime"] = updates.end_datetime
        await task.set(mongo_updates)
        return await self.get_task_by_id(task_id)
