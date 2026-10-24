"""
CodeBot — Rule-Based Chatbot
CodeAlpha Python Programming Internship | Task 4

A beginner-friendly console chatbot that matches user messages to predefined
rules and replies with fixed responses. It does not use machine learning or AI.
"""

import string

BOT_NAME = "CodeBot"

GREETINGS = {"hello", "hi", "hey"}
GOODBYES = {"bye", "goodbye", "exit", "quit"}
THANKS = {"thanks", "thank", "thankyou"}
HOW_ARE_YOU = {"how are you", "how are you doing"}
NAME_QUESTIONS = {"what is your name", "whats your name", "who are you"}
MOOD_QUESTIONS = {"what can you do", "how can you help", "help me"}
JOKES = {"tell me a joke", "make me laugh"}


def clean_text(message):
    """Normalize a message to lowercase words without punctuation."""
    message = message.lower().strip()
    return " ".join(message.translate(str.maketrans("", "", string.punctuation)).split())


def contains_phrase(text, phrases):
    """Check whether any known phrase occurs as a complete phrase."""
    padded_text = f" {text} "
    return any(f" {phrase} " in padded_text for phrase in phrases)


def is_goodbye(message):
    """Return True if the message contains a goodbye command."""
    words = clean_text(message).split()
    return any(word in GOODBYES for word in words)


def get_response(message):
    """Choose a predefined response based on the normalized message."""
    text = clean_text(message)
    words = set(text.split())

    if not text:
        return "Please type a message and I'll do my best to respond."

    if is_goodbye(text):
        return "Goodbye! It was nice chatting with you."

    if contains_phrase(text, HOW_ARE_YOU):
        return "I'm doing well, thanks for asking! How are you?"

    if contains_phrase(text, NAME_QUESTIONS):
        return f"I'm {BOT_NAME}, a simple rule-based chatbot written in Python."

    if contains_phrase(text, MOOD_QUESTIONS) or "help" in words:
        return (
            "I can respond to greetings, answer how I am, tell you my name, "
            "say thanks, and tell a simple joke. Try: 'hello' or 'tell me a joke'."
        )

    if contains_phrase(text, JOKES):
        return "Why do Python programmers prefer dark mode? Because light attracts bugs!"

    if words.intersection(GREETINGS):
        return "Hello! How can I help you today?"

    if words.intersection(THANKS) or "thankyou" in words:
        return "You're welcome!"

    return "I'm not sure how to answer that yet. Type 'help' to see what I understand."


def main():
    """Run the chatbot until the user requests to exit."""
    print("=" * 42)
    print(f"{BOT_NAME.upper()} — RULE-BASED CHATBOT")
    print("=" * 42)
    print("Hi! Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        try:
            user_message = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        response = get_response(user_message)
        print(f"{BOT_NAME}: {response}\n")

        if is_goodbye(user_message):
            break


if __name__ == "__main__":
    main()
