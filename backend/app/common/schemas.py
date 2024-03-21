from app.companies.schemas import CompanySchema
from app.tasks.schemas import TaskSchema
from app.users.schemas import UserSchema


class CompanyGlobalDataSchema(BaseModel):
    user: UserSchema
    company: CompanySchema
    team_members: list[UserSchema]
    tasks: list[TaskSchema]
