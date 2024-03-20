from typing import Self

from app.config import settings
from openai import OpenAI


class OpenAiUtils:
    def __init__(self: Self):
        self.client = OpenAI(
            base_url=settings.OPENAI_BASE_URL, api_key=settings.OPENAI_API_KEY
        )
