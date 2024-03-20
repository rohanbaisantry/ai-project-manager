from app.common.enums import Environments
from app.config import settings
from app.factories.api import setup_api
from app.factories.logging import configure_logging
from beanie.exceptions import DocumentAlreadyCreated, DocumentNotFound
from fastapi.responses import PlainTextResponse
from starlette.middleware.cors import CORSMiddleware


def get_allowed_origins() -> list[str]:
    match settings.ENVIRONMENT:
        case Environments.PRODUCTION:
            return ["*"]
        case Environments.STAGING:
            return ["*"]
        case Environments.LOCAL:
            return ["*"]
    return []


api = setup_api()

api.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

configure_logging()


@api.exception_handler(DocumentNotFound)
async def not_found_exception_handler(_request, _exc):
    return PlainTextResponse("The requested resource was not found.", status_code=404)


@api.exception_handler(DocumentAlreadyCreated)
async def already_created_exception_handler(_request, _exc):
    return PlainTextResponse("The resource already exists.", status_code=409)
