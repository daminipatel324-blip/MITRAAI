import re


def clean_text(text: str) -> str:
    """
    Clean extracted text from PDF/TXT.

    - Removes repeated spaces
    - Fixes words like 'D A M I N I'
    - Removes excessive blank lines
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    cleaned_lines = []

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            cleaned_lines.append("")
            continue

        # Join letters separated by spaces
        # Example:
        # D A M I N I  -> DAMINI
        line = re.sub(
            r"\b(?:[A-Za-z]\s){2,}[A-Za-z]\b",
            lambda m: m.group(0).replace(" ", ""),
            line,
        )

        # Collapse multiple spaces
        line = re.sub(r"\s{2,}", " ", line)

        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Collapse too many blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()