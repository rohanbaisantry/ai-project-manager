from typing import Self

from beanie import PydanticObjectId, exceptions

from app.users.entities import CreateUserEntity
from app.users.models import User
from app.users.schemas import UserChat


class UserRepository:
    def __init__(self: Self):
        pass

    async def create_user(self: Self, data: CreateUserEntity) -> User:
        return await User(
            name=data.name, role=data.role, mobile=data.mobile, company=data.company
        ).create()

    async def create_users(self: Self, data: list[CreateUserEntity]) -> list[User]:
        insert_many_result = await User.insert_many(
            [User(name=item.name, role=item.role, mobile=item.mobile) for item in data]
        )
        return await User.find_many(
            User.id in insert_many_result.inserted_ids
        ).to_list()

    async def get_user_by_id(self: Self, user_id: PydanticObjectId) -> User | None:
        return await User.get(user_id)

    async def get_user_by_mobile(self: Self, mobile: str):
        return await User.find({"mobile": mobile}).first_or_none()

    async def get_users_of_a_company(
        self: Self, company_id: PydanticObjectId
    ) -> list[User]:
        return await User.find_many(User.company.id == company_id).to_list()

    async def add_chat(
        self: Self, user_id: PydanticObjectId, new_chat: UserChat
    ) -> User:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise exceptions.DocumentNotFound()

        await user.update({"$push": {"chats": new_chat}})
        return await self.get_user_by_id(user_id)
