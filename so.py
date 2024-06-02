

# Define chatbot responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thank you.", "Doing well, thanks."]),
    (r"what's your name?", ["I'm a chatbot.", "You can call me Chatbot."]),
    (r"bye|goodbye", ["Goodbye!", "See you later.", "Take care!"]),
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
print("Welcome to the chatbot. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chatbot.respond(user_input)
    print("Bot:", response)
