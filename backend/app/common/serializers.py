from app.common.schemas import CompanyGlobalDataSchema
from app.companies.models import Company
from app.companies.serializers import serialize_company
from app.tasks.models import Task
from app.tasks.serializers import serialize_task
from app.users.models import User
from app.users.serializers import serialize_user


async def serialize_company_global_data(
    user: User, company: Company, team_members: list[User], tasks: list[Task]
) -> CompanyGlobalDataSchema:
    return CompanyGlobalDataSchema(
        user=await serialize_user(user),
        company=serialize_company(company),
        team_members=[await serialize_user(item) for item in team_members],
        tasks=[await serialize_task(item) for item in tasks],
    )
