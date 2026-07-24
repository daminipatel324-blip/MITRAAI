from pathlib import Path

from tools.txt_reader import read_txt


def read_file(file_path: str):

    path = Path(file_path).expanduser()

    extension = path.suffix.lower()

    if extension == ".txt":
        return read_txt(file_path)

    return (
        False,
        f"❌ '{extension}' files are not supported yet."
    )