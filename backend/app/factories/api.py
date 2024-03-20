from contextlib import asynccontextmanager

from app.auth.routes import router as auth_router
from app.chat.routes import router as chat_router
from app.factories.db import setup_db
from app.health.routes import router as health_router
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await setup_db()
    yield


def setup_api() -> FastAPI:
    api = FastAPI(docs_url="/docs", redoc_url="/redoc", lifespan=lifespan)
    api.include_router(health_router)
    api.include_router(auth_router)
    api.include_router(chat_router)

    return api
