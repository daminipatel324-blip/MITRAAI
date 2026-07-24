from documents.manager import has_document


def detect_intent(user_input: str) -> str:
    """
    Detect the user's intent.

    Returns:
        "tool"
        "document"
        "general"
    """

    text = user_input.lower().strip()

    # -------------------------
    # Tool Intents
    # -------------------------

    if text.startswith("read "):
        return "tool"

    if any(op in user_input for op in ["+", "-", "*", "/", "%", "**"]):
        return "tool"

    if text in ("time", "date"):
        return "tool"

    # Safe system commands
    system_commands = {
        "pwd",
        "ls",
        "whoami",
        "which python3",
        "which pip",
        "python3 --version",
        "pip --version",
    }

    if text in system_commands:
        return "tool"

    if (
        text.startswith("show system")
        or text.startswith("system info")
        or text.startswith("python version")
        or text.startswith("current folder")
        or text.startswith("operating system")
    ):
        return "tool"

    # -------------------------
    # Document Intents
    # -------------------------

    if has_document():

        document_keywords = [
            "document",
            "resume",
            "cv",
            "summary",
            "summarize",
            "skill",
            "skills",
            "experience",
            "education",
            "worked",
            "company",
            "companies",
            "project",
            "projects",
            "operating system",
            "windows",
            "linux",
            "mac",
        ]

        if any(word in text for word in document_keywords):
            return "document"

    # -------------------------
    # Default
    # -------------------------

    return "general"