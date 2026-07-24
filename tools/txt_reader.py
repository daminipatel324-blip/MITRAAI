from pathlib import Path


def read_txt(file_path: str):

    path = Path(file_path).expanduser()

    if not path.exists():
        return False, "❌ File not found."

    if not path.is_file():
        return False, "❌ Path is not a file."

    try:
        content = path.read_text(encoding="utf-8")

        return True, content

    except UnicodeDecodeError:
        return False, "❌ Unable to read text file (encoding error)."

    except Exception as e:
        return False, f"❌ {e}"