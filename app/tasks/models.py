from datetime import datetime
from typing import List, Optional

from beanie import Document, Link

from app.companies.models import Company
from app.users.models import User


class Task(Document):
    name: str
    description: str
    start_datetime: datetime
    end_datetime: datetime
    next_follow_up_datetime: Optional[datetime]
    comments: List[str] = []
    is_completed: bool = False
    company: Link[Company]
    asignee: Link[User]

    class Settings:
        name = "tasks"
