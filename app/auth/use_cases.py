from typing import Self

from beanie import PydanticObjectId
from beanie.exceptions import DocumentAlreadyCreated

from app.auth.entities import CreateTeamMembersEntity, SignupEntity
from app.companies.entities import CreateCompanyEntity
from app.companies.models import Company
from app.companies.repositories import CompanyRepository
from app.users.entities import CreateUserEntity
from app.users.enums import UserRoles
from app.users.models import User
from app.users.repositories import UserRepository


class AuthUseCases:
    def __init__(
        self: Self, user_repo=UserRepository(), company_repo=CompanyRepository()
    ):
        self.user_repo = user_repo
        self.company_repo = company_repo

    async def signup(self: Self, data: SignupEntity) -> tuple[User, Company]:
        existing_user = await self.user_repo.get_user_by_mobile(data.user_mobile)
        if existing_user:
            raise DocumentAlreadyCreated()

        company = await self.company_repo.create_company(
            CreateCompanyEntity(name=data.company_name)
        )
        user = await self.user_repo.create_user(
            CreateUserEntity(
                name=data.user_name,
                mobile=data.user_mobile,
                role=UserRoles.ADMIN,
                company=company.id,
            )
        )
        return user, company

    async def add_team_members_to_company(
        self: Self, company_id: PydanticObjectId, data: list[CreateTeamMembersEntity]
    ) -> list[User]:
        return await self.user_repo.create_users(
            [
                CreateUserEntity(
                    name=item.user_name,
                    mobile=item.user_mobile,
                    role=UserRoles.TEAM_MEMBER,
                    company=company_id,
                )
                for item in data
            ]
        )
