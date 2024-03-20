from app.chat.entities import SaveNewChatEntity
from app.chat.schemas import UserWithChatsSchema
from app.chat.serializers import serialize_user_with_chats
from app.chat.use_cases import ChatUseCases
from app.users.repositories import UserRepository
from beanie import PydanticObjectId
from fastapi import APIRouter

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/{user_id}")
async def new_chat_received(
    user_id: PydanticObjectId, data: SaveNewChatEntity
) -> UserWithChatsSchema:
    use_cases = ChatUseCases()
    user = await use_cases.save_new_chat(user_id, data)
    # TODO: Trigger AI and update Tasks + follow-up notifications handling.
    return serialize_user_with_chats(user)


@router.get("/{user_id}")
async def get_user_chats(user_id: PydanticObjectId) -> UserWithChatsSchema:
    use_cases = UserRepository()
    user = await use_cases.get_user_by_id(user_id)
    return serialize_user_with_chats(user)
