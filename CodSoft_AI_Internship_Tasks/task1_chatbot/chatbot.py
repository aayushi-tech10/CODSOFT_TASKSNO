"""Task 1: Rule-Based Chatbot."""
def get_response(message):
    text = message.strip().lower()
    if not text:
        return "I didn't catch that. Could you type something?"
    if any(w in text for w in ("hello", "hi", "hey")):
        return "Hello! I'm a simple rule-based chatbot. How can I help?"
    if "your name" in text or "who are you" in text:
        return "I'm a rule-based chatbot created for an AI internship task."
    if "how are you" in text:
        return "I'm doing well, thank you! How are you?"
    if "help" in text:
        return "Try greeting me, asking my name, or asking how I am."
    if "thank" in text:
        return "You're welcome!"
    if any(w in text for w in ("bye", "goodbye", "exit", "quit")):
        return "Goodbye! Have a nice day."
    return "I only know a few simple rules. Try 'hello', 'help', or 'what is your name?'"

def main():
    print("RULE-BASED CHATBOT — type 'bye' to exit")
    while True:
        message = input("You: ")
        print("Bot:", get_response(message))
        if any(w in message.strip().lower() for w in ("bye", "goodbye", "exit", "quit")):
            break

if __name__ == "__main__":
    main()
