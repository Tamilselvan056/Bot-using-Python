import tkinter as tk
from tkinter import scrolledtext, END
import nltk
import random
from nltk.chat.util import Chat, reflections


# Function to send a message and receive a response
def send_message():
    user_message = user_input.get("1.0", "end-1c")
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    user_input.delete("1.0", tk.END)
    
    # Replace this with your actual chatbot logic to generate a response
    bot_response = generate_response(user_message)  # Call your chatbot function here
    
    chat_display.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_display.see(END)

# Function that simulates chatbot logic
def generate_response(user_input):
    # Replace this with your chatbot logic
    # Process user_input and generate a response
    response = "This is a sample response from the chatbot."
    return response

# Create the main window
root = tk.Tk()
root.title("Chatbot UI Example")

# Create a scrolled text widget to display the chat
chat_display = scrolledtext.ScrolledText(root, width=50, height=20)
chat_display.pack(padx=10, pady=10)

# Create an entry widget for user input
user_input = tk.Text(root, width=40, height=3)
user_input.pack(padx=10)

# Create a button to send the user's message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the main event loop
root.mainloop()

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
