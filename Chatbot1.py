responses = {
    "hello": "Hi there! ",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm doing great! ",
    "your name": "I am a Rule-Based AI Chatbot ",
    "who created you": "Vangala Sri charan created me! ",
    "python": "Python is a popular programming language.",
    "c++": "C++ is powerful for system and application development.",
    "ai": "Artificial Intelligence helps machines simulate human intelligence.",
    "help": "You can ask me about AI, Python, C++, or greet me.",
    "college": "I am studying B.Tech.",
    "github": "I have projects on GitHub.",
    "linkedin": "Connect with me on LinkedIn.",
    "good morning": "Good Morning! ",
    "good night": "Good Night! "
}

print(" AI Chatbot Started!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! ")
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that. "
    )

    print("Bot:", reply)