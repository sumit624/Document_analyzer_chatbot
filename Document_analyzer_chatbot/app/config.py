import os
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "Document Analyzer Chatbot"
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


settings = Settings()
