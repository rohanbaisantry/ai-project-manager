from datetime import datetime
from typing import Self

from beanie import PydanticObjectId

from app.chat.entities import SaveNewChatEntity
from app.users.entities import UserChatEntity
from app.users.enums import UserChatSentBy
from app.users.models import User
from app.users.repositories import UserRepository


class ChatUseCases:
    def __init__(self: Self, user_repo=UserRepository()):
        self.user_repo = user_repo

    async def save_new_chat(
        self: Self, user_id: PydanticObjectId, data: SaveNewChatEntity
    ) -> User:
        return await self.user_repo.update_user_chats(
            user_id,
            UserChatEntity(
                content=data.message,
                sent_by=UserChatSentBy.USER,
                sent_at=datetime.now(),
            ),
        )
