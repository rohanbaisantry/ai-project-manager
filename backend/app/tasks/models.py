from datetime import datetime
from typing import List, Optional

from app.companies.models import Company
from app.users.models import User
from beanie import Document, Link


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
