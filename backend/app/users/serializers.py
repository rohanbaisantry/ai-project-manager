from app.users.models import User
from app.users.schemas import UserSchema


def serialize_user(user: User) -> UserSchema:
    return UserSchema(
        name=user.name,
        role=user.role.value,
        mobile=user.mobile,
    )
