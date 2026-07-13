from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """Contract that every LLM provider must implement."""

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """
        Generate text from the given prompt.
        """
        pass