# 📇 Contact Book

A simple command-line contact book application built in Python for adding, viewing, updating, and deleting contacts.

## 📚 Table of Contents

* [About This Project](#-about-this-project)
* [Features](#-features)
* [Requirements](#%EF%B8%8F-requirements)
* [Installation](#-installation)
* [Usage](#%EF%B8%8F-usage)
* [Project Structure](#-project-structure)
* [How It Works](#%EF%B8%8F-how-it-works)
* [License](#-license)

## 📌 About This Project

This project is a lightweight, in-memory contact management system with a menu-driven command-line interface. It's a great example of using a Python class to encapsulate data and behavior for a simple CRUD (Create, Read, Update, Delete) application.

## ✨ Features

* ➕ **Add** a new contact with name, phone number, and an optional email
* 👀 **View** all saved contacts in a clean, formatted list
* ✏️ **Update** an existing contact's phone number and/or email
* 🗑️ **Delete** a contact by name
* ☎️ Phone number validation (must be exactly 10 digits)
* 🚫 Prevents duplicate contact names

## 🛠️ Requirements

* Language: Python 3.x
* No external dependencies — uses only the Python standard library

Check your installed Python version:

```bash
python --version
```

## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/python-projects.git
```

2. Move into this project's folder:

```bash
cd python-projects/06_Contact-Book
```

## ▶️ Usage

Run the script from your terminal:

```bash
python main.py
```

You'll see a menu with options to add, view, update, delete, or exit:

```
==================================================


Welcome to the Contact Book !!
1. Add Contact
2. View Contacts
3. Delete Contact
4. Update Contact
5. Exit
Enter your choice (1-5):
```

Follow the prompts to manage your contacts during the session.

> ⚠️ **Note:** Contacts are stored in memory only — they are **not saved to a file** and will be lost when the program exits.

## 📁 Project Structure

```
contact-book/
│
├──src
│       ├── main.py       # Contact_book class and CLI entry point
└── README.md     # Project documentation
```

## ⚙️ How It Works

The core logic lives in the `Contact_book` class, which stores contacts in a dictionary keyed by name:

* **`add_contact(name, phone_number, email=None)`** — Adds a new contact after validating that the phone number is exactly 10 digits, and that the name isn't already taken.
* **`view_contacts()`** — Prints all stored contacts with their phone number and email (if provided).
* **`update_contact(name, phone_number=None, email=None)`** — Updates an existing contact's phone number and/or email.
* **`delete_contact(name)`** — Removes a contact by name.

## 📄 License

This project is licensed under the [MIT License](https://github.com/akbaratig/Python-Projects/blob/main/LICENSE).
