from app.auth.schemas import SignupSchema
from app.companies.models import Company
from app.users.models import User


def serialize_signup_response(user: User, company: Company) -> SignupSchema:
    return SignupSchema(
        user_id=user.id,
        user_mobile=user.mobile,
        user_role=user.role,
        user_name=user.name,
        company_id=company.id,
        company_name=company.name,
    )
