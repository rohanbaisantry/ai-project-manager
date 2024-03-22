from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.common.routes import router as common_router
from app.factories.db import setup_db
from app.health.routes import router as health_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await setup_db()
    yield


def setup_api() -> FastAPI:
    api = FastAPI(docs_url="/docs", redoc_url="/redoc", lifespan=lifespan)
    api.include_router(health_router)
    api.include_router(common_router)

    return api
