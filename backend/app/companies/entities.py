from pydantic import BaseModel


class CreateCompanyEntity(BaseModel):
    name: str
