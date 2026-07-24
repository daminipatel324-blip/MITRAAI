import re

from documents.manager import get_document_chunks


def _tokenize(text: str):
    """
    Convert text into lowercase words.
    """

    return set(re.findall(r"\w+", text.lower()))


def find_relevant_chunks(query: str, top_k: int = 3):
    """
    Return the most relevant document chunks based on
    keyword overlap.
    """

    chunks = get_document_chunks()

    if not chunks:
        return []

    query_words = _tokenize(query)

    scored_chunks = []

    for chunk in chunks:

        chunk_words = _tokenize(chunk)

        score = len(query_words.intersection(chunk_words))

        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    results = [
        chunk
        for score, chunk in scored_chunks[:top_k]
        if score > 0
    ]

    return results