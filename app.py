from core.agent import MITRAAgent

print("=" * 40)
print("        Welcome to MITRAAI")
print("=" * 40)

agent = MITRAAgent()

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":

        print("\nMITRAAI: Goodbye! 👋")
        break

    reply = agent.chat(user_input)

    print(f"\nMITRAAI: {reply}")