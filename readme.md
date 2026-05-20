# 🤖 AI-Powered Codebase Summarizer

Have you ever looked at a folder full of programming code and wished someone could just explain what it all does in plain English? That is exactly what this tool does!

This is a simple smart assistant that looks at a folder of Python programming files, reads through the code, and hands it over to **Google Gemini AI**. The AI analyzes the code and automatically writes a clean, easy-to-read summary report (`README-AI.md`) for you.

---

## 🧭 How the Tool Works

The application works like a mini assembly line broken into 4 simple steps:

1. **The Scanner (`main.py`):** Asks you which folder or file you want to look at, checks to make sure the folder exists, and picks out only the Python files.
2. **The Reader (`models.py`):** Opens the files up behind the scenes, reads the text inside them, and notes down how big the files are.
3. **The Brain (`analyzer.py`):** Takes that code text, sends it securely to Google Gemini AI, and asks the AI to explain it clearly.
4. **The Writer (`exporter.py`):** Collects all of the AI's explanations and packages them into a beautifully formatted document called `README-AI.md`.

---

## 🗂️ Project Folders Explained

Here is a map of how the project is organized:

```text
ai-code-summarizer/
│
├── .env                    # A hidden text file that stores your secret Google API key
├── .gitignore              # A safety file telling Git not to share your secret key online
├── README.md               # The file you are reading right now!
├── README-AI.md            # The final summary report created by the AI
│
└── src/                    # The folder holding the actual software parts
    ├── __init__.py         # A connector link that strings the parts together
    ├── main.py             # The main control switch and user menu
    ├── models.py           # The file reader and data organizer
    ├── analyzer.py         # The bridge connecting to Google Gemini AI
    └── exporter.py         # The document writer that saves the final report