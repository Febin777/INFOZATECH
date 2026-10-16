import random
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)

lemmatizer = WordNetLemmatizer()


def preprocess_text(text: str) -> set[str]:
    """Tokenize, lowercase, and lemmatize user input to handle varied phrasing."""
    text_clean = re.sub(r"[^\w\s]", "", text.lower())
    tokens = word_tokenize(text_clean)
    return {lemmatizer.lemmatize(token) for token in tokens}


INTENTS = {
    "greeting": {
        "keywords": {"hello", "hi", "hey", "greetings", "morning", "afternoon"},
        "responses": [
            "Hello, How can I assist you today?",
            "Hi there! What can I help you with?",
            "Hey! Glad you reached out.",
        ],
    },
    "farewell": {
        "keywords": {"bye", "goodbye", "exit", "quit", "see", "later"},
        "responses": [
            "Goodbye! Have a great day ahead.",
            "Take care! Feel free to return if you have more questions.",
        ],
    },
    "faq_services": {
        "keywords": {"service", "solution", "offer", "provide", "product"},
        "responses": [
            "We offer software development, cloud infrastructure, and IT consulting.",
            "Our primary offerings include digital transformation, tech support, and custom software.",
        ],
    },
    "faq_hours": {
        "keywords": {"hour", "timing", "time", "open", "available", "schedule"},
        "responses": [
            "Our support desk operates Monday through Friday, 9:00 AM to 6:00 PM.",
            "We are available on business days from 9 AM to 6 PM.",
        ],
    },
    "small_talk_mood": {
        "keywords": {"doing", "status", "feeling", "well"},
        "responses": [
            "I'm operating smoothly! How are things with you?",
            "All systems normal and ready to assist you!",
        ],
    },
    "small_talk_identity": {
        "keywords": {"who", "bot", "robot", "name"},
        "responses": [
            "I am InfozaBot, an automated rule-based assistant.",
            "I'm the virtual assistant here to help answer common inquiries.",
        ],
    },
}

FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that, or ask about our services, hours, or contact info?",
    "Sorry, I didn't catch that. Type 'help' or inquire about our services, support hours, or contact channels.",
]


def get_response(user_input: str) -> tuple[str, str]:
    """Matches processed user input against intent keywords and returns (intent, reply)."""
    tokens = preprocess_text(user_input)

    for intent, data in INTENTS.items():
        if tokens & data["keywords"]:
            return intent, random.choice(data["responses"])

    return "fallback", random.choice(FALLBACK_RESPONSES)


def run_chatbot():
    print("=" * 60)
    print("InfozaBot Online. (Type 'bye', 'exit', or 'quit' to end)")
    print("=" * 60)

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nInfozaBot: Goodbye!")
            break

        if not user_input:
            continue

        intent, reply = get_response(user_input)
        print(f"InfozaBot: {reply}")

        if intent == "farewell":
            break


if __name__ == "__main__":
    run_chatbot()