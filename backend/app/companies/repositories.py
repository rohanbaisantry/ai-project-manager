from typing import Self

from beanie import PydanticObjectId

from app.companies.entities import CreateCompanyEntity
from app.companies.models import Company


class CompanyRepository:
    def __init__(self: Self):
        pass

    async def create_company(self: Self, data: CreateCompanyEntity):
        return await Company(name=data.name).create()

    async def get_company_by_id(
        self: Self, company_id: PydanticObjectId
    ) -> Company | None:
        return await Company.get(company_id)
