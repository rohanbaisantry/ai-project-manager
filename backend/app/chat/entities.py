from pydantic import BaseModel


class SaveNewChatEntity(BaseModel):
    message: str
