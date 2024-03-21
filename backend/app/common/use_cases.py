from asyncio import Task
from datetime import datetime
from typing import Self

from app.common.entities import SignupEntity
from app.companies.entities import CreateCompanyEntity
from app.companies.models import Company
from app.companies.repositories import CompanyRepository
from app.tasks.entities import CreateTaskEntity, UpdateTaskEntity
from app.tasks.repositories import TaskRepository
from app.users.entities import CreateUserEntity
from app.users.enums import UserChatSentBy, UserRoles
from app.users.models import User
from app.users.repositories import UserRepository
from app.users.schemas import UserChat
from beanie import PydanticObjectId
from beanie.exceptions import DocumentAlreadyCreated


class CommonUseCases:
    def __init__(
        self: Self,
        user_repo=UserRepository(),
        company_repo=CompanyRepository(),
        task_repo=TaskRepository(),
    ):
        self.user_repo = user_repo
        self.company_repo = company_repo
        self.task_repo = task_repo

    async def signup(self: Self, data: SignupEntity) -> tuple[User, Company]:
        existing_user = await self.user_repo.get_user_by_mobile(data.user_mobile)
        if existing_user:
            raise DocumentAlreadyCreated()

        company = await self.company_repo.create_company(
            CreateCompanyEntity(name=data.company_name)
        )
        user = await self.user_repo.create_user(
            CreateUserEntity(
                name=data.user_name,
                mobile=data.user_mobile,
                role=UserRoles.ADMIN,
                company=company.id,
            )
        )
        return user, company

    async def get_company_global_data_from_user_mobile(
        self: Self, mobile: str
    ) -> tuple[User, Company, list[User], list[Task]]:
        user = await self.user_repo.get_user_by_mobile(mobile)
        company = await self.company_repo.get_company_by_id(user.company)
        team_members = await self.user_repo.get_users_of_a_company(company.id)
        tasks = await self.task_repo.get_tasks_by_company_id(company.id)

        return (user, company, team_members, tasks)

    async def add_team_member_to_company(
        self: Self, data: CreateUserEntity
    ) -> list[User]:
        return await self.user_repo.create_user(data)

    async def create_task(self: Self, data: CreateTaskEntity) -> Task:
        return await self.task_repo.create_task(data)

    async def update_task(
        self: Self, task_id: PydanticObjectId, updates: UpdateTaskEntity
    ) -> Task:
        return await self.task_repo.update_task(task_id, updates)

    async def save_new_chat_and_get_response(
        self: Self, user_id: PydanticObjectId, message: str
    ) -> UserChat:
        new_chat = UserChat(
            sent_at=datetime.now(), sent_by=UserChatSentBy.USER, content=message
        )
        await self.user_repo.add_chat(user_id, new_chat)
        # TODO: Trigger AI and update Tasks + follow-up notifications handling.
        response_from_system = UserChat(
            sent_at=datetime.now(), sent_by=UserChatSentBy.SYSTEM, content=message
        )
        await self.user_repo.add_chat(user_id, response_from_system)
        # TODO: Take action based on the response
        return response_from_system