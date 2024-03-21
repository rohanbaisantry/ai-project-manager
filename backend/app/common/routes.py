from beanie import PydanticObjectId
from fastapi import APIRouter

from app.common.entities import CreateTeamMemberEntity, SaveNewChatEntity, SignupEntity
from app.common.schemas import CompanyGlobalDataSchema
from app.common.serializers import serialize_company_global_data
from app.common.use_cases import CommonUseCases
from app.tasks.entities import CreateTaskEntity, UpdateTaskEntity
from app.tasks.schemas import TaskSchema
from app.tasks.serializers import serialize_task
from app.users.entities import CreateUserEntity
from app.users.enums import UserRoles
from app.users.schemas import UserChat, UserSchema
from app.users.serializers import serialize_user

router = APIRouter(prefix="", tags=["common"])

# AUTH ROUTES


@router.post("/auth/signup")
async def signup(data: SignupEntity) -> CompanyGlobalDataSchema:
    use_cases = CommonUseCases()
    user, company = await use_cases.signup(data)
    return await serialize_company_global_data(user, company, [user], [])


@router.post("/auth/login/{mobile}")
async def login(mobile: str) -> CompanyGlobalDataSchema:
    use_cases = CommonUseCases()
    (
        user,
        company,
        team_members,
        tasks,
    ) = await use_cases.get_company_global_data_from_user_mobile(mobile)
    return await serialize_company_global_data(user, company, team_members, tasks)


# COMPANY ROUTES


@router.post("/company/team-members/{company_id}")
async def create_team_member(
    company_id: PydanticObjectId, data: CreateTeamMemberEntity
) -> UserSchema:
    use_cases = CommonUseCases()
    team_member = await use_cases.add_team_member_to_company(
        CreateUserEntity(
            name=data.name,
            mobile=data.mobile,
            company=company_id,
            role=UserRoles.TEAM_MEMBER,
        )
    )
    return await serialize_user(team_member)


# TASK ROUTES


@router.post("/tasks")
async def create_task(data: CreateTaskEntity) -> TaskSchema:
    use_cases = CommonUseCases()
    task = await use_cases.create_task(data)
    return serialize_task(task)


@router.post("/tasks/{task_id}")
async def edit_task(task_id: PydanticObjectId, data: UpdateTaskEntity) -> TaskSchema:
    use_cases = CommonUseCases()
    updated_task = await use_cases.update_task(task_id, data)
    return serialize_task(updated_task)


# CHAT ROUTES


@router.post("/chats/{user_id}")
async def new_chat_received(
    user_id: PydanticObjectId, data: SaveNewChatEntity
) -> UserChat:
    use_cases = CommonUseCases()
    system_response = await use_cases.save_new_chat_and_get_response(
        user_id, data.message
    )
    return system_response
