from datetime import datetime
from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel

from app.companies.schemas import CompanySchema
from app.users.schemas import UserSchema


class TaskSchema(BaseModel):
    id: PydanticObjectId
    name: str
    description: str
    start_datetime: datetime
    due_datetime: datetime
    next_follow_up_datetime: Optional[datetime] = None
    comments: list[str]
    assignee: Optional[UserSchema] | None = None
    assignee_id: PydanticObjectId
    company: Optional[CompanySchema] = None
    company_id: PydanticObjectId
    is_completed: bool
