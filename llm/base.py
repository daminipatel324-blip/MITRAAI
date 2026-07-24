from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Base class for all LLM providers.
    Every provider (Ollama, Gemini, Groq, etc.)
    must implement the generate() method.
    """

    @abstractmethod
    def generate(self, messages):
        """
        Generate a response from the LLM.

        Args:
            messages (list): Conversation messages.

        Returns:
            str: Model response.
        """
        pass