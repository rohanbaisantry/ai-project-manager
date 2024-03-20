from pydantic_settings import BaseSettings

from app.common.enums import Environments


class CommonSettings(BaseSettings):
    APP_NAME: str = "AI-PM"
    DEBUG_MODE: bool = False
    ENVIRONMENT: Environments = Environments.LOCAL


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class OpenAiSettings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str


class DataBaseSettings(BaseSettings):
    DATABASE_URI: str


class Settings(CommonSettings, ServerSettings, OpenAiSettings, DataBaseSettings):
    pass


settings = Settings()
