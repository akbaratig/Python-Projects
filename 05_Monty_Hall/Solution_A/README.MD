# 🎲 Monty Hall Problem Simulation

A Python project that simulates the famous **Monty Hall problem**, both as a command-line tool and as an interactive **Streamlit dashboard**, to empirically prove why switching doors gives you a better chance of winning than sticking with your original choice.

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

It includes:
* 🖥️ A **command-line version** (`monty_hall.py`) for a quick simulation and summary stats.
* 📊 An **interactive Streamlit dashboard** (`dashboard.py`) that visualizes the win percentages converging live, round by round.

## 🧠 What is the Monty Hall Problem?

The Monty Hall problem is a classic probability puzzle based on a game show scenario:

1. There are 3 doors. Behind one is a **car** 🚗, behind the other two are **goats** 🐐.
2. You pick one door at random.
3. The host, who knows what's behind each door, opens one of the **remaining doors that has a goat** behind it.
4. You're then given the choice to **stick** with your original door or **switch** to the other unopened door.

Counter-intuitively, **switching doubles your odds of winning** — from 1/3 to 2/3. This project proves it through simulation rather than theory.

## ✨ Features

* 🎯 Simulates any number of Monty Hall games for both strategies: switching and not switching
* 📊 Calculates and displays the win rate (%) for each strategy
* 📈 Live, animated line charts in the Streamlit dashboard showing win rates converge in real time
* 💻 Simple, interactive command-line interface
* 🐍 Pure Python — minimal dependencies

## 🛠️ Requirements

* Language: Python 3.6 or higher (uses type hints)
* [Streamlit](https://streamlit.io/) — only required for the dashboard version

Check your installed Python version:

```bash
python --version
```

## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/python-projects.git
```

2. Move into this project's `src` folder:

```bash
cd python-projects/05_Monty_Hall/Solution_A/src
```

3. Install the dashboard dependency:

```bash
pip install streamlit
```

## ▶️ Usage

Run all commands from inside the `src/` folder, so the dashboard's relative path to `images/monty_hall.png` resolves correctly.

### Command-Line Version

```bash
python monty_hall.py
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

### Streamlit Dashboard

```bash
streamlit run dashboard.py
```

Set the number of simulations with the input box, then watch the two live charts converge toward **~66%** (switching) and **~33%** (not switching) as more rounds are simulated.

## 📁 Project Structure

```
Solution_A/
│
├── images/
│   └── monty_hall.png     # Image displayed in the dashboard header
│
├── src/
│   ├── monty_hall.py       # Core simulation logic and CLI entry point
│   ├── dashboard.py        # Streamlit dashboard for live visualization
│   └── monty_hall.ipynb    # Notebook for exploring/prototyping the simulation
│
└── README.md
```

## ⚙️ How It Works

* **`monty_hall_game(switch_doors)`** — Simulates a single round of the game. It randomly places the car behind one of three doors, makes a random initial choice, has the "host" reveal a goat door (never the car, never the player's pick), and returns whether the final choice (after switching or staying) wins the car.
* **`simulate_game(number_of_game)`** — Runs the simulation `number_of_game` times for both strategies (switching and not switching) and returns their respective win rates.
* **`dashboard.py`** — Wraps the simulation in a Streamlit app, running one game at a time in a loop and streaming the running win percentage of each strategy into two live-updating line charts.

## 📄 License

This project is licensed under the [MIT License](https://github.com/akbaratig/Python-Projects/blob/main/LICENSE).
