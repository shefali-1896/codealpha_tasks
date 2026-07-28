# Basic Chatbot Project

# Display welcome message
print("Welcome to Basic Chatbot!")

# Tell the user how to exit the chat
print("Type 'bye' to exit the chat.\n")

# Keep the chatbot running until the user exits
while True:

    # Ask the user to enter a message
    user = input("You: ").lower().strip()

    # Check if the user wants to end the chat
    if user == "bye":
        print("Chatbot: Goodbye! Have a nice day.\n")
        break

    # Respond to 'hello'
    elif user == "hello":
        print("Chatbot: Hello! How are you?\n")

    # Respond when the user says they are fine
    elif user == "i am fine, how about you":
        print("Chatbot: I am doing great! Thanks for asking.\n")

    # Respond to 'what is your name?'
    elif user == "what is your name?":
        print("Chatbot: My name is CodeAlpha Bot.\n")

    # Respond to 'who created you'
    elif user == "who created you":
        print("Chatbot: I was created using Python.\n")

    # Respond to 'thank you'
    elif user == "thank you":
        print("Chatbot: You're Welcome!\n")

    # Respond to any other message
    else:
        print("Chatbot: Sorry, I don't understand that.\n")
