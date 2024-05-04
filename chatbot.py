from userrespond import respond_to_user

def run_chatbot():
    print("Welcome to the sentiment analysis chatbot!")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = respond_to_user(user_input)
        print(f"Chatbot: {response}")

run_chatbot()