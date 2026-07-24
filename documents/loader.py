from pathlib import Path

from tools.file_reader import read_file
from documents.manager import set_current_document


def load_document(file_path: str):

    path = Path(file_path).expanduser()

    if not path.exists():
        return False, "❌ File not found."

    success, text = read_file(str(path))

    if not success:
        return False, text

    set_current_document(str(path), text)

    return (
        True,
        f"✅ Document '{path.name}' loaded successfully."
    )