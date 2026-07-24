from llm.ollama import OllamaLLM


class LLMManager:
    """
    Manages the active LLM provider.
    """

    def __init__(self):
        self.providers = {
            "ollama": OllamaLLM(),
        }

        self.current_provider = "ollama"

    def get_current_model(self):
        return self.current_provider

    def set_current_model(self, provider_name):
        provider_name = provider_name.lower()

        if provider_name not in self.providers:
            raise ValueError(f"Unsupported model: {provider_name}")

        self.current_provider = provider_name

    def generate(self, messages):
        provider = self.providers[self.current_provider]
        return provider.generate(messages)