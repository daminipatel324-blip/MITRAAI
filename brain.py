from ollama import chat
from config import MODEL_NAME


def get_ai_response(messages):

    response = chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response["message"]["content"]