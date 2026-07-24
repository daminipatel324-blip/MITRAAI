from tools.calculator import calculate
from tools.time_tool import get_current_time, get_current_date
from tools.system_tool import get_system_info
from tools.file_reader import read_file


def run_tool(user_input):

    text = user_input.lower().strip()

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
    # File Reader
    # -------------------------
    if text.startswith("read "):

        file_path = user_input[5:].strip()

        success, result = read_file(file_path)

        return True, result

    return False, None