"""Multi-agent system base class."""
from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    """Base class for all agents."""

    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    async def process(self, input_data: Any) -> Any:
        """Process input and return output."""
        pass

    @abstractmethod
    async def collaborate(self, other_agent: "Agent", message: str) -> Any:
        """Collaborate with another agent."""
        pass
