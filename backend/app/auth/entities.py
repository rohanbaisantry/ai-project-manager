from pydantic import BaseModel


class SignupEntity(BaseModel):
    user_name: str
    user_mobile: str
    company_name: str


class CreateTeamMembersEntity(BaseModel):
    user_name: str
    user_mobile: str


class CreateTeamMembersRequestEntity(BaseModel):
    team_members: list[CreateTeamMembersEntity]
