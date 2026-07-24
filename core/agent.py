from brain import get_ai_response
from memory import load_facts, save_facts, extract_facts
from prompts import build_system_prompt

from core.router import run_tool
from core.history import save_chat
from core.context import build_context


class MITRAAgent:

    def __init__(self):

        self.facts = load_facts()

        self.messages = [
            {
                "role": "system",
                "content": build_system_prompt(self.facts),
            }
        ]

    def chat(self, user_input):

        # -------------------------
        # Update Memory
        # -------------------------
        new_facts = extract_facts(user_input)

        if new_facts:

            self.facts.update(new_facts)

            save_facts(self.facts)

            self.messages[0]["content"] = build_system_prompt(
                self.facts
            )

            print("✅ Memory Updated!")

        # -------------------------
        # Check Tools
        # -------------------------
        tool_used, tool_response = run_tool(user_input)

        if tool_used:

            self.messages.append(
                {
                    "role": "user",
                    "content": user_input,
                }
            )

            self.messages.append(
                {
                    "role": "assistant",
                    "content": tool_response,
                }
            )

            save_chat(user_input, tool_response)

            return tool_response

        # -------------------------
        # Build Context
        # -------------------------
        prompt = build_context(user_input)

        self.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        ai_reply = get_ai_response(self.messages)

        self.messages.append(
            {
                "role": "assistant",
                "content": ai_reply,
            }
        )

        save_chat(user_input, ai_reply)

        return ai_reply