def chunk_text(text: str, chunk_size: int = 1000):
    """
    Split text into fixed-size chunks.

    Args:
        text: Document text.
        chunk_size: Maximum characters per chunk.

    Returns:
        List of text chunks.
    """

    if not text:
        return []

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start = end

    return chunks