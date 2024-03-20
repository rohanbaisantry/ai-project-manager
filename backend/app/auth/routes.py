from app.auth.entities import CreateTeamMembersRequestEntity, SignupEntity
from app.auth.schemas import SignupSchema
from app.auth.serializers import serialize_signup_response
from app.auth.use_cases import AuthUseCases
from app.users.schemas import UserSchema
from app.users.serializers import serialize_user
from beanie import PydanticObjectId
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
async def signup(data: SignupEntity) -> SignupSchema:
    use_cases = AuthUseCases()
    user, company = await use_cases.signup(data)
    return serialize_signup_response(user, company)


@router.post("/team-members/{company_id}")
async def add_team_members(
    company_id: PydanticObjectId, data: CreateTeamMembersRequestEntity
) -> list[UserSchema]:
    use_cases = AuthUseCases()
    team_members = await use_cases.add_team_members_to_company(
        company_id, data.team_members
    )
    return [serialize_user(item) for item in team_members]
