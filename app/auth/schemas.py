from openai import BaseModel

from app.users.entities import UserChatEntity
from app.users.enums import UserRoles


class SignupSchema(BaseModel):
    user_name: str
    user_role: UserRoles
    user_mobile: str
    company_name: str
    chats: list[UserChatEntity] = []
