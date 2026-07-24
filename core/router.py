from tools.calculator import calculate
from tools.time_tool import get_current_time, get_current_date
from tools.system_tool import get_system_info


def run_tool(user_input):

    text = user_input.lower()

    if "time" in text:
        return True, get_current_time()

    if "date" in text:
        return True, get_current_date()

    if (
        "python version" in text
        or "system" in text
        or "operating system" in text
        or "current folder" in text
    ):
        return True, get_system_info()

    operators = ["+", "-", "*", "/", "%", "**"]

    if any(op in user_input for op in operators):

        answer = calculate(user_input)

        if answer is not None:
            return True, answer

    return False, None