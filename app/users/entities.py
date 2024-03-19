from datetime import datetime

from beanie import PydanticObjectId
from pydantic import BaseModel

from app.users.enums import UserChatSentBy, UserRoles


class UserChatEntity(BaseModel):
    content: str
    sent_by: UserChatSentBy
    sent_at: datetime


class CreateUserEntity(BaseModel):
    name: str
    role: UserRoles
    mobile: str
    company: PydanticObjectId
