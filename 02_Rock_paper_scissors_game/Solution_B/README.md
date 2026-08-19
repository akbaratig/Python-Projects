# ✂️ Rock Paper Scissors Game

A CLI-based Rock Paper Scissors game written in Python, where the player competes against the computer. Each game runs for up to 10 rounds, and the final results — including each side's score — are displayed at the end.

---

## 📌 Features

* ✂️ **Three Classic Choices:** Rock, paper, scissor (`rock`, `paper`, `scissor`)
* 🤖 **Random Computer Opponent:** The computer randomly picks one of the three options each round.
* 🛡️ **Input Validation:** Invalid input triggers an error message and prompts the user to try again.
* 🏆 **Scoring System:** Player score, computer score, and ties are tracked separately.
* 🔢 **10-Round Limit:** Each game runs for a maximum of 10 rounds.
* 🚪 **Early Exit:** You can quit the game at any time by entering `q`.
* 🔄 **Replay Option:** After a game ends, you can play again or exit the program with `q`.

---

## 🛠️ Requirements

* **Language:** Python 3.x
* **Modules:** Uses only the standard library (`random`) — no extra packages required.

---

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Download or clone the project file.
3. Run the following command in your terminal:

```bash
python rock_paper_scissors.py
```

---

## 🎮 How to Play

1. Enter your name when prompted.
2. Each round, type one of the options: `rock`, `paper`, or `scissor`.
3. The computer randomly selects an option, and the round's result is displayed.
4. The game continues for up to 10 rounds, unless you exit early by entering `q`.
5. At the end, the final result (win, loss, or tie) is shown along with the scores.
6. You can choose to play again, or exit the program by entering `q`.

---

## 🕹️ Game Preview

```text
PLease Enter a Name : Ali
Welcome to the game of rock, paper, scissors, Ali
****************************************
Round 1
Score: You 0
Computer 0
Ties 0
Please Choose Your Move (['rock', 'paper', 'scissor']) : rock
Player Choice is : rock
Computer Choice is : scissor
You won.
****************************************
Round 2
Score: You 1
Computer 0
Ties 0
Please Choose Your Move (['rock', 'paper', 'scissor']) : q
You are out of the game.

========================================
FINAL RESULTS
========================================
Your Score: 1
Computer Score: 0
Ties: 0
----------------------------------------
🏆 Congratulations Ali! You won the game!

========================================
Do you Want to play again? (Y/n) or enter q to exit() : q
```

---

## 📁 `Rock_Paper_Scissor` Class Overview

| Method | Description |
|---|---|
| `get_user_choice()` | Reads and validates the player's input; recursively re-prompts if the input is invalid. |
| `get_computer_choice()` | Generates a random choice for the computer. |
| `decide_winner()` | Compares the player's and computer's choices, determines the round winner, and updates the scores. |
| `show_final_result()` | Displays the final score summary and overall game outcome. |
| `play()` | Runs the main game loop and manages the rounds. |

---

## 📝 Technical Notes

* Since `get_user_choice()` calls itself recursively on invalid input, it would be better to replace this with a `while` loop in the future to avoid growing the call stack.
* The messages `"You Won."` and `"You won."` in `decide_winner()` are inconsistent in capitalization; unifying them would make the output more consistent.

---

## 📄 License

This project is free to use, modify, and extend.
