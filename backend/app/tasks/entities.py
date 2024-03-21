from datetime import datetime
from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel


class CreateTaskEntity(BaseModel):
    name: str
    description: str
    start_datetime: datetime
    due_datetime: datetime
    next_follow_up_datetime: Optional[datetime] = None
    company_id: PydanticObjectId
    asignee_user_id: PydanticObjectId


class UpdateTaskEntity(BaseModel):
    new_comment: Optional[str] = None
    due_datetime: Optional[datetime] = None
    start_datetime: Optional[datetime] = None
    is_completed: Optional[bool] = None
    next_follow_up_datetime: Optional[datetime] = None
