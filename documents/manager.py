from pathlib import Path

from documents.chunker import chunk_text


_current_document = None


def set_current_document(file_path: str, text: str):
    """
    Store the currently loaded document along with its chunks.
    """

    global _current_document

    path = Path(file_path).expanduser()

    _current_document = {
        "name": path.name,
        "path": str(path),
        "text": text,
        "chunks": chunk_text(text),
    }


def get_current_document():
    return _current_document


def has_document():
    return _current_document is not None


def get_document_chunks():
    """
    Return all chunks of the current document.
    """

    if not has_document():
        return []

    return _current_document["chunks"]


def clear_document():
    """
    Remove the current document from memory.
    """

    global _current_document

    _current_document = None