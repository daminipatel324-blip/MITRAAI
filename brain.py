from llm.manager import LLMManager

_manager = LLMManager()


def get_ai_response(messages):
    return _manager.generate(messages)