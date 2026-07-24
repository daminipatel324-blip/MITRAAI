from pathlib import Path

from pypdf import PdfReader

from tools.text_cleaner import clean_text


def read_pdf(file_path: str):

    path = Path(file_path).expanduser()

    if not path.exists():
        return False, "❌ File not found."

    if not path.is_file():
        return False, "❌ Path is not a file."

    try:

        reader = PdfReader(str(path))

        pages = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                pages.append(page_text)

        if not pages:
            return False, "❌ No readable text found in PDF."

        full_text = "\n\n".join(pages)

        full_text = clean_text(full_text)

        return True, full_text

    except Exception as e:

        return False, f"❌ {e}"