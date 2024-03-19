from app.chat.schemas import UserWithChatsSchema
from app.users.models import User


def serialize_user_with_chats(user: User) -> UserWithChatsSchema:
    return UserWithChatsSchema(
        name=user.name, role=user.role.value, mobile=user.mobile, chats=user.chats
    )
