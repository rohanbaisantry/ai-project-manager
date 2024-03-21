from app.companies.models import Company
from app.companies.schemas import CompanySchema


def serialize_company(company: Company) -> CompanySchema:
    return CompanySchema(
        id=company.id,
        name=company.name,
    )
