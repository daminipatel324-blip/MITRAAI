from config import DATA_FILE


def load_facts():

    facts = {}

    try:

        with open(DATA_FILE, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if "=" in line:

                    key, value = line.split("=", 1)

                    facts[key] = value

    except FileNotFoundError:

        pass

    return facts


def save_facts(facts):

    with open(DATA_FILE, "w", encoding="utf-8") as file:

        for key, value in facts.items():

            file.write(f"{key}={value}\n")


def extract_facts(user_input):

    facts = {}

    text = user_input.lower().strip()

    if text.startswith("my name is"):

        facts["Name"] = user_input[11:].strip()

    elif text.startswith("i live in"):

        facts["City"] = user_input[10:].strip()

    elif text.startswith("i am learning"):

        facts["Learning"] = user_input[13:].strip()

    return facts