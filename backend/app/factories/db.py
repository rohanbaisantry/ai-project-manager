from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.companies.models import Company
from app.config import settings
from app.tasks.models import Task
from app.users.models import User


async def setup_db():
    client = AsyncIOMotorClient(settings.DATABASE_URI)
    await init_beanie(
        database=client.db_name,
        document_models=[Company, User, Task],
        allow_index_dropping=True,
    )
