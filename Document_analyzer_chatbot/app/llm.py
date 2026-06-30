from __future__ import annotations

from app.config import settings


class LLMClient:
    def __init__(self) -> None:
        self.provider = settings.llm_provider

    def generate(self, prompt: str) -> str:
        if self.provider == "openai":
            return "OpenAI integration is not configured in this starter build."
        return (
            "Mock LLM response: the system is ready for a real LLM provider integration."
        )
