from app.common.serializers import serialize_company_global_data
from app.common.use_cases import CommonUseCases
from app.users.repositories import UserRepository
from app.users.schemas import UserSchema
from app.users.serializers import serialize_user
from beanie import PydanticObjectId
from fastapi import APIRouter

from backend.app.common.schemas import CompanyGlobalDataSchema
from backend.app.tasks.entities import CreateTaskEntity, UpdateTaskEntity

router = APIRouter(prefix="", tags=["common"])


@router.post("/signup")
async def signup(data: SignupEntity) -> CompanyGlobalDataSchema:
    use_cases = CommonUseCases()
    user, company = await use_cases.signup(data)
    return serialize_company_global_data(user, company, [user], [])


@router.post("/login/{mobile}")
async def login(data: SignupEntity) -> CompanyGlobalDataSchema:
    use_cases = CommonUseCases()
    user, company, team_members, tasks = await use_cases.get_company_global_data(data)
    return serialize_company_global_data(user, company, team_members, tasks)


@router.post("/team-members/{company_id}")
async def add_team_member(
    company_id: PydanticObjectId, data: CreateTeamMemberRequestEntity
) -> list[UserSchema]:
    use_cases = CommonUseCases()
    team_members = await use_cases.add_team_members_to_company(company_id, [data])
    return [serialize_user(item) for item in team_members]


@router.post("/tasks/{company_id}")
async def add_task(
    company_id: PydanticObjectId, data: CreateTaskEntity
) -> list[UserSchema]:
    use_cases = CommonUseCases()
    team_members = await use_cases.add_team_members_to_company(
        company_id, data.team_members
    )
    return [serialize_user(item) for item in team_members]


@router.post("/tasks/{task_id}")
async def edit_task(
    company_id: PydanticObjectId, data: UpdateTaskEntity
) -> list[UserSchema]:
    use_cases = CommonUseCases()
    team_members = await use_cases.add_team_members_to_company(
        company_id, data.team_members
    )
    return [serialize_user(item) for item in team_members]


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/chats/{user_id}")
async def new_chat_received(
    user_id: PydanticObjectId, data: SaveNewChatEntity
) -> UserWithChatsSchema:
    use_cases = ChatUseCases()
    user = await use_cases.save_new_chat(user_id, data)
    # TODO: Trigger AI and update Tasks + follow-up notifications handling.
    return serialize_user_with_chats(user)


@router.get("/global-data/{company_id}")
async def get_company_global_data(
    company_id: PydanticObjectId,
) -> CompanyGlobalDataSchema:
    use_cases = UserRepository()
    user = await use_cases.get_user_by_id(user_id)
    return serialize_user_with_chats(user)
