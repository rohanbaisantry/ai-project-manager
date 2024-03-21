from app.users.models import User
from app.users.schemas import UserSchema


async def serialize_user(user: User, get_company=False) -> UserSchema:
    user_schema = UserSchema(
        id=user.id,
        name=user.name,
        role=user.role.value,
        mobile=user.mobile,
        chats=user.chats,
        company_id=user.company.to_ref().id,
    )
    if get_company:
        user_schema.company = await user.fetch_link("company")
    return user_schema
