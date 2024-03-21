import asyncio
import os
from datetime import datetime, timedelta

import motor.motor_asyncio
from app.companies.models import Company
from app.tasks.models import Task
from app.users.enums import UserRoles
from app.users.models import User
from beanie import init_beanie
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

company_seed_data = [{"name": "Company", "id": ObjectId()}]
user_seed_data = [
    {
        "id": ObjectId(),
        "name": "User1",
        "role": UserRoles.ADMIN,
        "mobile": "+911234567890",
        "chats": [],
        "company": company_seed_data[0]["id"],
    },
    {
        "id": ObjectId(),
        "name": "User2",
        "role": UserRoles.ADMIN,
        "mobile": "+911234567891",
        "chats": [],
        "company": company_seed_data[0]["id"],
    },
    {
        "id": ObjectId(),
        "name": "User3",
        "role": UserRoles.ADMIN,
        "mobile": "+911234567892",
        "chats": [],
        "company": company_seed_data[0]["id"],
    },
]
task_seed_data = [
    {
        "id": ObjectId(),
        "name": "Task1",
        "description": "Task1's Description",
        "start_datetime": datetime.now(),
        "end_datetime": datetime.now() + timedelta(hours=3),
        "comments": [],
        "is_completed": False,
        "company": company_seed_data[0]["id"],
        "asignee": user_seed_data[0]["id"],
    },
    {
        "id": ObjectId(),
        "name": "Task1",
        "description": "Task1's Description",
        "start_datetime": datetime.now(),
        "end_datetime": datetime.now() + timedelta(hours=3),
        "comments": [],
        "is_completed": False,
        "company": company_seed_data[0]["id"],
        "asignee": user_seed_data[1]["id"],
    },
    {
        "id": ObjectId(),
        "name": "Task1",
        "description": "Task1's Description",
        "start_datetime": datetime.now(),
        "next_follow_up_datetime": datetime.now() + timedelta(hours=3),
        "end_datetime": datetime.now() + timedelta(hours=3),
        "comments": [],
        "is_completed": False,
        "company": company_seed_data[0]["id"],
        "asignee": user_seed_data[2]["id"],
    },
]
seed_data = {
    Company: company_seed_data,
    User: user_seed_data,
    Task: task_seed_data,
}


async def connect_to_db():
    print("Connecting to:", os.getenv("DATABASE_URI"))
    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("DATABASE_URI"))
    await init_beanie(
        client.db_name,
        document_models=[User, Company, Task],
        allow_index_dropping=True,
    )


async def delete_all_documents():
    print("Deleting all existing documents:")
    await User.delete_all()
    await Company.delete_all()
    await Task.delete_all()


async def add_seed_documents():
    print("Seeding the database with data.")
    documents_to_insert = []
    for table, documents in seed_data.items():
        for document in documents:
            documents_to_insert.append(table(**document))
        await table.insert_many(documents_to_insert)


async def seed_db_with_data():
    print("seed_db_with_data - Process Started.")
    await connect_to_db()
    await delete_all_documents()
    await add_seed_documents()
    print("seed_db_with_data - Process Completed.")


if __name__ == "__main__":
    asyncio.run(seed_db_with_data())
