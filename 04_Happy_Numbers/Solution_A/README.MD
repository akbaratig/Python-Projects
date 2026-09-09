# Happy Number Checker

A simple command-line Python program that checks whether a given positive integer is a **happy number**.

## What is a Happy Number?

A happy number is defined by the following process:

1. Start with any positive integer.
2. Replace the number by the sum of the squares of its digits.
3. Repeat the process until the number equals `1` (a happy number), or it loops endlessly in a cycle that does not include `1` (not a happy number).

For example:
- `19` is happy: `1² + 9² = 82` → `8² + 2² = 68` → `6² + 8² = 100` → `1² + 0² + 0² = 1` ✅
- `4` is not happy: it eventually falls into the repeating cycle `4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...` ❌

## Features

- Checks whether any positive integer is a happy number.
- Interactive command-line loop — check multiple numbers in one session.
- Input validation for non-numeric input and non-positive integers.
- Type `q` or `exit` at any time to quit the program.

## Requirements

- Python 3.x
- No external dependencies (uses only the Python standard library)

## Usage

Run the script from your terminal:

```bash
python main.py
```

You'll be prompted to enter a positive integer:

```
Welcome to the Happy Number Checker!
==================================================
Enter a positive integer to check if it's a happy number (or type 'exit' to quit): 19
19 is a happy number.
```

Enter `q` or `exit` to stop the program.

## Project Structure

```
.
├── main.py       # Contains the check_happy_number function and CLI entry point
└── README.md     # Project documentation
```

## How It Works

The core logic lives in `check_happy_number(n)`:

```python
def check_happy_number(n):
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
```

It repeatedly replaces `n` with the sum of the squares of its digits, tracking previously seen values in a set. If `n` reaches `1`, the number is happy. If a previously seen value reappears, the sequence has entered a cycle and the number is not happy.

## License

This project is free to use and modify for personal or educational purposes.
