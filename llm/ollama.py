from ollama import chat

from config import MODEL_NAME
from llm.base import BaseLLM


class OllamaLLM(BaseLLM):
    """
    Ollama language model provider.
    """

    def generate(self, messages):
        response = chat(
            model=MODEL_NAME,
            messages=messages
        )

        return response["message"]["content"]