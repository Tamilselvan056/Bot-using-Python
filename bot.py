import nltk
import random
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you?", "Hi %1, nice to meet you! How can I help you today?"]
    ],
    [
        r"hello|hi|hey",
        ["Hello!", "Hi there!", "Hey!", "Hi, how can I help you?"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot.", "I'm ChatBot, your virtual assistant."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm just a computer program, but I'm functioning properly.", "I'm here to help!"]
    ],
    [
        r"(.*) (hungry|thirsty|tired)",
        ["I'm just a chatbot, so I don't feel physical sensations like hunger, thirst, or tiredness."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'd be happy to help. How can I assist you?", "Of course, I'm here to help. What do you need assistance with?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day.", "Goodbye! Feel free to return if you have more questions."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I'm a chatbot and I might not fully understand that. Can you please rephrase?", "I'm not quite sure what you mean. Could you provide more details?"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Main loop
print("ChatBot: Hi! I'm here to assist you. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
