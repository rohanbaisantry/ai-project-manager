from app.users.entities import UserChatEntity
from app.users.schemas import UserSchema


class UserWithChatsSchema(UserSchema):
    chats: list[UserChatEntity] = []
