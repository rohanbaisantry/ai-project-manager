from typing import List

from app.companies.models import Company
from app.users.enums import UserRoles
from app.users.schemas import UserChat
from beanie import Document, Indexed, Link


class User(Document):
    name: str
    role: UserRoles
    mobile: Indexed(str, unique=True)  # type: ignore
    chats: List[UserChat] = []
    company: Link[Company]

    class Settings:
        name = "users"
