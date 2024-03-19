from typing import List

from beanie import Document, Indexed, Link

from app.companies.models import Company
from app.users.entities import UserChatEntity
from app.users.enums import UserRoles


class User(Document):
    name: str
    role: UserRoles
    mobile: Indexed(str, unique=True)  # type: ignore
    chats: List[UserChatEntity] = []
    company: Link[Company]

    class Settings:
        name = "users"
