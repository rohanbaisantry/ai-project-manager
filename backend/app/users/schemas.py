from datetime import datetime
from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel

from app.companies.schemas import CompanySchema
from app.users.enums import UserChatSentBy


class UserChat(BaseModel):
    content: str
    sent_by: UserChatSentBy
    sent_at: datetime


class UserSchema(BaseModel):
    id: PydanticObjectId
    name: str
    role: str
    mobile: str
    chats: list[UserChat]
    company: Optional[CompanySchema] = None
    company_id: PydanticObjectId
