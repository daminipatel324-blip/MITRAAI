from documents.manager import has_document
from documents.search import find_relevant_chunks


def build_context(user_input: str) -> str:
    """
    Build the prompt sent to the LLM.

    If a document is loaded, include only the most
    relevant chunks instead of the entire document.
    """

    if not has_document():
        return user_input

    chunks = find_relevant_chunks(user_input)

    if not chunks:
        return user_input

    context = "\n\n".join(chunks)

    prompt = f"""
Use the following document context to answer the user's question.

Document Context:
{context}

-------------------------

User Question:
{user_input}
"""

    return prompt.strip()