# AI Flashcards

A simple and smart command-line flashcard program built in Python to help you learn effectively using spaced repetition and fuzzy answer matching.

---

## Features

- Add custom flashcards (question-answer pairs)  
- Review flashcards due for study with fuzzy string matching to accept approximate answers  
- Automatically adjusts review intervals based on your performance (spaced repetition)  
- List all saved flashcards  
- Delete flashcards you no longer need  

---

## Requirements

- Python 3.7 or higher  
- [nltk](https://www.nltk.org/)  
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)  
- [python-Levenshtein](https://github.com/ztane/python-Levenshtein) (optional but recommended for faster fuzzywuzzy)  

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main program:

```bash
python flashcards.py
```

You will see a menu:

```
📚 AI Flashcards
1️⃣ Add a flashcard
2️⃣ Review flashcards
3️⃣ List all flashcards
4️⃣ Delete a flashcard
0️⃣ Exit
👉 Your choice:
```

* Choose **1** to add a new flashcard.
* Choose **2** to review flashcards that are due today.
* Choose **3** to list all flashcards.
* Choose **4** to delete a flashcard.
* Choose **0** to exit.

---

## How It Works

* Flashcards are stored locally in `flashcards_data.json`.
* When reviewing, the program calculates similarity between your answer and the correct answer using fuzzy matching.
* If your answer is very close, the review interval increases, so you see that card less often.
* If your answer is incorrect, the interval resets so you review it sooner.
* This approach helps you focus on cards you find difficult and save time on cards you know well.

---

## Notes

* The program downloads the NLTK tokenizer data (`punkt`) the first time it runs.
* Make sure you have an active internet connection for the initial run.
* The review interval is capped at 30 days.
* Answers are compared case-insensitively.

---

## License

This project is open-source and free to use.  
Licensed under the [MIT License](LICENSE).

---

## Author

**Hadi Dadashzade**

---

Feel free to open issues or contribute to improve this project!
