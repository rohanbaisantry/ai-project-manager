from beanie import PydanticObjectId
from pydantic import BaseModel


class CompanySchema(BaseModel):
    id: PydanticObjectId
    name: str
