import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_FILE = os.path.join(BASE_DIR, "data", "history.json")


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except Exception:
        return []


def save_chat(user, assistant):

    history = load_history()

    history.append(
        {
            "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "user": user,
            "assistant": assistant,
        }
    )

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)