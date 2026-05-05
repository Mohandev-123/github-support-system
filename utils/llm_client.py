"""LLM client supporting both Anthropic and OpenRouter."""
import os
from typing import Optional
from pydantic_settings import BaseSettings


class LLMConfig(BaseSettings):
    """LLM configuration."""

    api_provider: str = "openrouter"  # or "anthropic"
    anthropic_api_key: Optional[str] = None
    openrouter_api_key: Optional[str] = None
    model: str = "claude-opus-4-7"
    temperature: float = 0.7
    max_tokens: int = 2048

    class Config:
        env_file = ".env"


class LLMClient:
    """Unified LLM client for Anthropic or OpenRouter."""

    def __init__(self, config: Optional[LLMConfig] = None):
        self.config = config or LLMConfig()
        self.provider = self.config.api_provider

        if self.provider == "openrouter":
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.config.openrouter_api_key,
                base_url="https://openrouter.ai/api/v1",
            )
        elif self.provider == "anthropic":
            from anthropic import Anthropic
            self.client = Anthropic(
                api_key=self.config.anthropic_api_key
            )
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def generate(self, messages: list) -> str:
        """Generate response from messages."""
        if self.provider == "openrouter":
            response = self.client.chat.completions.create(
                model=self.config.model,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
            )
            return response.choices[0].message.content

        elif self.provider == "anthropic":
            response = self.client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                messages=messages,
            )
            return response.content[0].text

    def stream(self, messages: list):
        """Stream response."""
        if self.provider == "openrouter":
            return self.client.chat.completions.create(
                model=self.config.model,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
                stream=True,
            )
        elif self.provider == "anthropic":
            with self.client.messages.stream(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                messages=messages,
            ) as stream:
                return stream
