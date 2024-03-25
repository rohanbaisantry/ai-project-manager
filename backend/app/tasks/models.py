from datetime import datetime
from typing import List, Optional, Self

from beanie import Document, Link

from app.companies.models import Company
from app.users.models import User


class Task(Document):
    name: str
    description: str
    start_datetime: datetime
    due_datetime: datetime
    next_follow_up_datetime: Optional[datetime]
    comments: List[str] = []
    is_completed: bool = False
    company: Link[Company]
    assignee: Link[User]

    class Settings:
        name = "tasks"

    def to_readable_string(self: Self) -> str:
        return f"""
Task Name: {self.name}
Task Description: {self.description}
Start Date and Time: {self.start_datetime.strftime()}
Due Date and Time: {self.due_datetime.strftime()}
Next Follow Up Date and Time: {self.next_follow_up_datetime.strftime() if self.next_follow_up_datetime else "-"}
Is Completed: {self.is_completed}
Assignee ID: {self.assignee.to_ref().id}
Company ID: {self.company.to_ref().id}
Comments: {"|".join([item for item in self.comments])}
"""
