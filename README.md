# InfoBot 🤖

A lightweight, rule-based conversational assistant built in Python using the **Natural Language Toolkit (NLTK)**. **InfoBot** demonstrates fundamental Natural Language Processing (NLP) concepts such as tokenization, lowercasing, and lemmatization to match user inputs against defined intent patterns with fallback handling.

---

## 📌 Features

- **Text Normalization & Preprocessing**: Cleans input strings, converts text to lowercase, and utilizes NLTK's `WordNetLemmatizer` to reduce words to their base lexical forms.
- **Intent Recognition Engine**: Maps lemmatized tokens against predefined domain keywords (`greeting`, `services`, `hours`, `identity`, `farewell`).
- **Dynamic Response Selection**: Returns random variations of pre-configured responses for matching intents.
- **Graceful Fallback Handling**: Automatically catches unmapped/out-of-scope queries and prompts the user with supported topics.
- **Interactive CLI Loop**: Terminal-based conversational interface with exit trigger support (`bye`, `quit`, `exit`).

---

## 🛠️ Project Structure

```text
├── chat.py          # Main application script containing NLP logic & CLI loop
├── README.md        # Project documentation
└── requirements.txt # Project dependencies
