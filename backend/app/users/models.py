from typing import List, Optional

from beanie import Document, Indexed, Link

from app.companies.models import Company
from app.users.enums import UserRoles
from app.users.schemas import UserChat


class User(Document):
    name: str
    role: UserRoles
    mobile: Indexed(str, unique=True)  # type: ignore
    chats: List[UserChat] = []
    company: Link[Company]
    openai_thread_id: Optional[str] = None

    class Settings:
        name = "users"
