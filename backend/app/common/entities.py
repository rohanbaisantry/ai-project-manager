from pydantic import BaseModel


class SignupEntity(BaseModel):
    user_name: str
    user_mobile: str
    company_name: str


class CreateTeamMemberEntity(BaseModel):
    user_name: str
    user_mobile: str


class SaveNewChatEntity(BaseModel):
    message: str
