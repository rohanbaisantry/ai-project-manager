from datetime import datetime
from typing import Optional

from app.companies.schemas import CompanySchema
from app.users.schemas import UserSchema
from beanie import PydanticObjectId
from pydantic import BaseModel


class TaskSchema(BaseModel):
    id: PydanticObjectId
    name: str
    description: str
    start_datetime: datetime
    end_datetime: datetime
    next_follow_up_datetime: Optional[datetime] = None
    comments: list[str]
    assignee: Optional[UserSchema] | None = None
    asignee_id: PydanticObjectId
    company: Optional[CompanySchema] = None
    company_id: PydanticObjectId
