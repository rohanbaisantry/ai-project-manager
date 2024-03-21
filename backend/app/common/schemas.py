from backend.app.companies.schemas import CompanySchema
from backend.app.tasks.schemas import TaskSchema
from backend.app.users.schemas import UserSchema


class CompanyGlobalDataSchema(BaseModel):
    user: UserSchema
    company: CompanySchema
    team_members: list[UserSchema]
    tasks: list[TaskSchema]
