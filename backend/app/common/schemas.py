from app.companies.schemas import CompanySchema
from app.tasks.schemas import TaskSchema
from app.users.schemas import UserSchema
from pydantic import BaseModel


class CompanyGlobalDataSchema(BaseModel):
    user: UserSchema
    company: CompanySchema
    team_members: list[UserSchema]
    tasks: list[TaskSchema]
