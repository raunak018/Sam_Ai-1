print("Welcome to Chatbot 🤖")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Bot: Hi! How can I help you?")

    elif user.lower() == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")