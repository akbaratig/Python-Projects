# 🔐 Password Generator

A CLI-based password generator written in Python, offering three different generation modes — random passwords, memorable passwords, and numeric PINs — through a simple interactive menu.

---

## 📌 Features

* 🔑 **Random Password Generator:** Generates a random password from letters, with optional digits and symbols.
* 🧠 **Memorable Password Generator:** Builds a human-friendly password from a sequence of real English words, with optional random capitalization and a custom separator.
* 🔢 **PIN Generator:** Generates a numeric PIN of any custom length.
* 🧩 **Extensible Design:** All generators share a common abstract base class (`PasswordGenerator`), making it easy to add new generator types.
* 🔁 **Looping Menu:** After each generation, the menu is shown again until the user chooses to exit.

---

## 🛠️ Requirements

* **Language:** Python 3.7+
* **Modules:**
  * Standard library — `random`, `string`
  * Third-party — [`nltk`](https://www.nltk.org/) (used for the word corpus behind the memorable password generator)

### Install dependencies

```bash
pip install nltk
```

### Download the NLTK word corpus

Run this once before using the memorable password generator:

```python
import nltk
nltk.download('words')
```

---

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone the project file.
3. Run the following command in your terminal:

```bash
python main.py
```

---

## 🎮 How to Use

1. Choose a generator from the menu: Random Password (`1`), Memorable Password (`2`), PIN (`3`), or Exit (`4`).
2. Depending on the generator, enter the requested details (length, whether to include numbers/symbols, number of words, separator, capitalization).
3. The generated password or PIN is printed to the screen.
4. The menu reappears, letting you generate more passwords or exit with option `4`.

---

## 🕹️ Program Preview

```text
==================================================
Select password generator:
1. Random Password Generator
2. Memorable Password Generator
3. Pin Generator
4. Exit

Enter your choice (1-4): 1
Enter the length of the password: 12
Include numbers? (y/n): y
Include symbols? (y/n): n
Generated Password: hTqLpXo3Zk9A

==================================================
Select password generator:
1. Random Password Generator
2. Memorable Password Generator
3. Pin Generator
4. Exit

Enter your choice (1-4): 2
Enter the number of words: 4
Enter the separator (default is '-'):
Randomly capitalize words? (y/n): y
Generated Password: Apple-mountain-RIVER-glass

==================================================
Select password generator:
1. Random Password Generator
2. Memorable Password Generator
3. Pin Generator
4. Exit

Enter your choice (1-4): 4
```

---

## 📁 Class Overview

| Class | Description |
|---|---|
| `PasswordGenerator` | Abstract base class defining the `generate()` interface implemented by all generators. |
| `RandomPasswordGenerator` | Builds a password from letters, optionally extended with digits and/or symbols. |
| `MemorablePasswordGenerator` | Joins a number of randomly chosen words (optionally capitalized) using a custom separator. |
| `Pingenerator` | Produces a random numeric string of a given length, suitable as a PIN. |

---

## 📄 License

This project is free to use, modify, and extend.
