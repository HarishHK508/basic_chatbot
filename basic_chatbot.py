import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created to help you. You can call me ChatBuddy!"]
    ],
    [
        r"how are you ?",
        ["I'm just a program, but I'm doing great!"]
    ],
    [
        r"sorry (.*)",
        ["No worries", "It's okay", "Don't mention it"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Glad to know you're doing well."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "It was nice talking to you. See you soon!"]
    ],
    [
        r"(.*) (help|support|assist)(.*)",
        ["Sure! I'm here to help. What do you need assistance with?"]
    ],
    [
        r"(.*)",
        ["I’m not sure I understand. Can you say that differently?"]
    ]
]


def chatbot():
    print("Hi, I'm ChatBuddy. Type 'exit' to end the conversation.\n")
    chat = Chat(pairs, reflections)
    chat.converse()


chatbot()
