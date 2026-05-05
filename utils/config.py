"""Configuration for the multi-agent system."""
from pydantic_settings import BaseSettings
from typing import Optional


class Config(BaseSettings):
    """Application configuration."""

    # API Provider: "openrouter" or "anthropic"
    api_provider: str = "openrouter"

    # API Keys
    openrouter_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None

    # Model settings
    model: str = "claude-opus-4-7"
    temperature: float = 0.7
    max_tokens: int = 2048

    class Config:
        env_file = ".env"

