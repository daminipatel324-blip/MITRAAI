from tools.calculator import calculate
from tools.time_tool import get_current_time, get_current_date
from tools.system_tool import (
    get_system_info,
    run_system_command,
)
from documents.loader import load_document


def run_tool(user_input):

    text = user_input.lower().strip()

    # -------------------------
    # System Commands
    # -------------------------
    system_result = run_system_command(text)

    if system_result is not None:
        return True, system_result

    # -------------------------
    # Time
    # -------------------------
    if "time" in text:
        return True, get_current_time()

    # -------------------------
    # Date
    # -------------------------
    if "date" in text:
        return True, get_current_date()

    # -------------------------
    # System Information
    # -------------------------
    if (
        "python version" in text
        or "system" in text
        or "operating system" in text
        or "current folder" in text
    ):
        return True, get_system_info()

    # -------------------------
    # Calculator
    # -------------------------
    operators = ["+", "-", "*", "/", "%", "**"]

    if any(op in user_input for op in operators):

        answer = calculate(user_input)

        if answer is not None:
            return True, answer

    # -------------------------
    # Document Loader
    # -------------------------
    if text.startswith("read "):

        file_path = user_input[5:].strip()

        success, result = load_document(file_path)

        return True, result

    return False, None