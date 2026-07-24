from pathlib import Path

from tools.txt_reader import read_txt
from tools.pdf_reader import read_pdf


def read_file(file_path: str):

    path = Path(file_path).expanduser()

    extension = path.suffix.lower()

    readers = {
        ".txt": read_txt,
        ".pdf": read_pdf,
    }

    reader = readers.get(extension)

    if reader is None:
        return (
            False,
            f"❌ '{extension}' files are not supported yet."
        )

    return reader(file_path)