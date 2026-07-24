from brain import get_ai_response
from memory import load_facts, save_facts, extract_facts
from prompts import build_system_prompt
from core.router import run_tool


class MITRAAgent:

    def __init__(self):

        # Load memory
        self.facts = load_facts()

        # Conversation history
        self.messages = [
            {
                "role": "system",
                "content": build_system_prompt(self.facts)
            }
        ]

    def chat(self, user_input):

        # -----------------------
        # Update Memory
        # -----------------------
        new_facts = extract_facts(user_input)

        if new_facts:

            self.facts.update(new_facts)
            save_facts(self.facts)

            self.messages[0]["content"] = build_system_prompt(self.facts)

            print("✅ Memory Updated!")

        # Save user message
        self.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # -----------------------
        # Tool Router
        # -----------------------
        tool_used, tool_response = run_tool(user_input)

        if tool_used:

            self.messages.append(
                {
                    "role": "assistant",
                    "content": tool_response
                }
            )

            return tool_response

        # -----------------------
        # AI Response
        # -----------------------
        ai_reply = get_ai_response(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": ai_reply
            }
        )

        return ai_reply