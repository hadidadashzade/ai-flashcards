import json
import os
import datetime
import random
from fuzzywuzzy import fuzz  # For fuzzy string matching
import nltk  # Natural Language Toolkit

# Downloading the punkt tokenizer (required by nltk)
nltk.download('punkt')

DATA_FILE = "flashcards_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(cards):
    with open(DATA_FILE, "w") as f:
        json.dump(cards, f, indent=2)

def add_card():
    question = input("📝 Enter the question: ").strip()
    answer = input("✅ Enter the correct answer: ").strip()
    card = {
        "question": question,
        "answer": answer,
        "last_review": str(datetime.date.today()),
        "interval": 1
    }
    cards = load_data()
    cards.append(card)
    save_data(cards)
    print("✔️ Flashcard saved successfully.")

def similarity(a, b):
    return fuzz.ratio(a.lower(), b.lower())

def review_cards():
    today = datetime.date.today()
    cards = load_data()
    due_cards = []

    # Find cards due for review
    for card in cards:
        last_review = datetime.datetime.strptime(card["last_review"], "%Y-%m-%d").date()
        interval = datetime.timedelta(days=card.get("interval", 1))
        if last_review + interval <= today:
            due_cards.append(card)

    if not due_cards:
        print("📭 No flashcards to review today.")
        return

    random.shuffle(due_cards)

    for card in due_cards:
        print(f"\n❓ {card['question']}")
        user_answer = input("✍️ Your answer: ").strip()

        score = similarity(user_answer, card["answer"])
        print(f"📊 Similarity: {score}%")

        if score >= 80:
            print("✅ Correct! Interval increased.")
            card["interval"] = min(card.get("interval", 1) * 2, 30)
        elif score >= 50:
            print("🟡 Almost correct. Will review again soon.")
            card["interval"] = 2
        else:
            print(f"❌ Incorrect. Correct answer: {card['answer']}")
            card["interval"] = 1

        card["last_review"] = str(today)

    save_data(cards)
    print("\n💾 All flashcards updated.")

def delete_card():
    cards = load_data()
    if not cards:
        print("⚠️ No flashcards to delete.")
        return

    print("\n🗑️ Flashcards:")
    for idx, card in enumerate(cards, 1):
        print(f"{idx}. {card['question']} → {card['answer']}")

    try:
        choice = int(input("👉 Enter the number of the flashcard to delete: ").strip())
        if 1 <= choice <= len(cards):
            removed = cards.pop(choice - 1)
            save_data(cards)
            print(f"🗑️ Flashcard '{removed['question']}' deleted successfully.")
        else:
            print("❗ Invalid number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def list_cards():
    cards = load_data()
    if not cards:
        print("⚠️ No flashcards found.")
        return
    for idx, card in enumerate(cards, 1):
        print(f"{idx}. {card['question']} → {card['answer']}")

def menu():
    print("\n📚 AI Flashcards")
    print("1️⃣ Add a flashcard")
    print("2️⃣ Review flashcards")
    print("3️⃣ List all flashcards")
    print("4️⃣ Delete a flashcard")
    print("0️⃣ Exit")

    choice = input("👉 Your choice: ").strip()

    if choice == "1":
        add_card()
    elif choice == "2":
        review_cards()
    elif choice == "3":
        list_cards()
    elif choice == "4":
        delete_card()
    elif choice == "0":
        print("👋 Goodbye!")
        return
    else:
        print("❗ Invalid choice.")

    menu()

if __name__ == "__main__":
    menu()
