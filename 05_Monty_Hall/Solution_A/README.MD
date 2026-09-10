# 🎲 Monty Hall Problem Simulation

A Python program that simulates the famous **Monty Hall problem** to empirically prove why switching doors gives you a better chance of winning than sticking with your original choice.

## 📚 Table of Contents

* [About This Project](#-about-this-project)
* [What is the Monty Hall Problem?](#-what-is-the-monty-hall-problem)
* [Features](#-features)
* [Requirements](#%EF%B8%8F-requirements)
* [Installation](#-installation)
* [Usage](#%EF%B8%8F-usage)
* [Project Structure](#-project-structure)
* [How It Works](#%EF%B8%8F-how-it-works)
* [License](#-license)

## 📌 About This Project

This project simulates thousands of rounds of the Monty Hall game show scenario to show — through raw data instead of theory — that **switching doors** wins roughly **2 out of 3 times**, while sticking with your original door wins only about **1 out of 3 times**.

## 🧠 What is the Monty Hall Problem?

The Monty Hall problem is a classic probability puzzle based on a game show scenario:

1. There are 3 doors. Behind one is a **car** 🚗, behind the other two are **goats** 🐐.
2. You pick one door at random.
3. The host, who knows what's behind each door, opens one of the **remaining doors that has a goat** behind it.
4. You're then given the choice to **stick** with your original door or **switch** to the other unopened door.

Counter-intuitively, **switching doubles your odds of winning** — from 1/3 to 2/3. This program proves it through simulation rather than theory.

## ✨ Features

* 🎯 Simulates any number of Monty Hall games for both strategies: switching and not switching
* 📊 Calculates and displays the win rate (%) for each strategy
* 💻 Simple, interactive command-line interface
* 🐍 Pure Python — no external dependencies beyond the standard library

## 🛠️ Requirements

* Language: Python 3.6 or higher (uses type hints)
* No external dependencies — only `random` and `typing` from the standard library

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
cd python-projects/monty-hall-simulation
```

## ▶️ Usage

Run the script from your terminal:

```bash
python main.py
```

You'll be prompted to enter how many games to simulate:

```
==================================================
Welcome to the Monty Hall Simulation
Enter the number of games to simulate: 10000
Win rate with switching: 66.79 %
Win rate without switching: 33.21 %
==================================================
```

💡 The larger the number of simulated games, the closer the results converge to the theoretical probabilities of **1/3 (no switch)** and **2/3 (switch)**.

## 📁 Project Structure

```
monty-hall-simulation/
│
├── main.py       # Core simulation logic and CLI entry point
└── README.md     # Project documentation
```

## ⚙️ How It Works

* **`monty_hall_game(switch_doors)`** — Simulates a single round of the game. It randomly places the car behind one of three doors, makes a random initial choice, has the "host" reveal a goat door (never the car, never the player's pick), and returns whether the final choice (after switching or staying) wins the car.
* **`simulate_game(number_of_game)`** — Runs the simulation `number_of_game` times for both strategies (switching and not switching) and returns their respective win rates.

## 📄 License

This project is licensed under the [MIT License](https://github.com/akbaratig/Python-Projects/blob/main/LICENSE).
