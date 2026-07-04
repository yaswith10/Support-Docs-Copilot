from app.chat.chat_engine import ChatEngine

def main():
    chat = ChatEngine("You are an Lying Agent. Give Lies to All the User Prompts")
    print("Support Docs Copilot Initiated")
    print("Type 'exit' to quit")

    while True:
        user_input = input("> ")
        if(user_input.lower() == "exit"): break

        response = chat.chat(user_input)
        print("AI", response)

if __name__ == "__main__":
    main()