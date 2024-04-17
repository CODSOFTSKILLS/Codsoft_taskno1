def respond_to_user_input(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but thanks for asking!"
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure, I'm here to help. What do you need assistance with?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting with me. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Thanks for chatting.")
            break
        response = respond_to_user_input(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
