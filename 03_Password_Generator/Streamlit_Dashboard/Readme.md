# Password Generator 🔐

A simple Python password generator application with a **Streamlit web interface**. The project provides three different password-generation modes:

- Random Password Generator
- Memorable Password Generator
- PIN Generator

The password-generation logic is implemented with Python classes in `main.py`, while `dashboard.py` provides the interactive Streamlit user interface.

## Features

### Random Password Generator

Generates a password using ASCII letters, with optional numbers and symbols.

Users can configure:

- Password length: 1–100 characters
- Include numbers
- Include symbols

### Memorable Password Generator

Generates a password by combining randomly selected words from the NLTK English word corpus.

Users can configure:

- Number of words: 2–10
- Separator between words
- Random capitalization

### PIN Generator

Generates a numeric PIN using randomly selected digits.

Users can configure:

- PIN length: 1–10 digits

## Project Structure

```text
project/
│
├── main.py            # Password generator classes and generation logic
├── dashboard.py       # Streamlit web application
├── images/
│   └── images.png     # Application image/logo used by the dashboard
└── README.md          # Project documentation
```

## Architecture

The project separates the password-generation logic from the user interface.

```text
                ┌─────────────────────┐
                │     dashboard.py    │
                │   Streamlit UI      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       main.py       │
                │ Password Generators │
                └──────────┬──────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        RandomPassword  Memorable     Pingenerator
          Generator     Generator
```

## Main Classes

### `PasswordGenerator`

`PasswordGenerator` is an abstract base class that defines the common `generate()` method for password generators.

```python
class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass
```

### `RandomPasswordGenerator`

Creates passwords from ASCII letters and optionally adds digits and punctuation.

```python
generator = RandomPasswordGenerator(
    length=12,
    include_numbers=True,
    include_symbols=True
)

password = generator.generate()
```

### `MemorablePasswordGenerator`

Creates a password by randomly selecting words from the NLTK word corpus and joining them with a configurable separator.

```python
generator = MemorablePasswordGenerator(
    number_of_words=4,
    seperator="-",
    capitalization=True
)

password = generator.generate()
```

### `Pingenerator`

Creates a numeric PIN with the requested length.

```python
generator = Pingenerator(length=6)
pin = generator.generate()
```

## Requirements

Python 3.9 or newer is recommended.

Install the required packages with:

```bash
pip install streamlit nltk
```

The project uses the NLTK English word corpus for memorable passwords. Download the corpus once before using that generator:

```python
import nltk
nltk.download("words")
```

You can also run it directly from Python:

```bash
python -c "import nltk; nltk.download('words')"
```

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

2. Create and activate a virtual environment (recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install streamlit nltk
```

4. Download the NLTK `words` corpus:

```bash
python -c "import nltk; nltk.download('words')"
```

## Running the Streamlit Application

Start the web application with:

```bash
streamlit run dashboard.py
```

Streamlit will start a local development server and provide a URL in the terminal, typically similar to:

```text
http://localhost:8501
```

Open that address in your browser to use the password generator.

## How the Dashboard Works

The Streamlit application presents a radio-button menu where the user selects one of the three generators.

### Random Password Generator

The dashboard asks for the desired password length and whether numbers and symbols should be included. When **Generate Password** is clicked, it creates a `RandomPasswordGenerator` object and displays the generated password.

### Memorable Password Generator

The dashboard asks for the number of words, separator, and whether words should be randomly capitalized. It then creates a `MemorablePasswordGenerator` object and displays the result.

### PIN Generator

The dashboard asks for the PIN length. Pressing **Generate PIN** creates a `Pingenerator` object and displays the generated PIN.

## Example Usage

After running the application, select:

```text
Random Password Generator
```

Then choose settings such as:

```text
Length: 12
Include numbers: Yes
Include symbols: Yes
```

The application will generate and display a password.

## Command-Line Mode

`main.py` also contains a command-line interface that can be executed directly:

```bash
python main.py
```

The command-line interface provides the following options:

```text
1. Random Password Generator
2. Memorable Password Generator
3. Pin Generator
4. Exit
```

This allows the password generators to be tested without Streamlit.

## Technologies Used

- **Python** — application logic
- **Streamlit** — web interface
- **NLTK** — English word corpus for memorable passwords
- **ABC / Abstract Base Class** — common interface for password generator classes
- **random** — random character and word selection
- **string** — ASCII letters, digits, and punctuation

## Security Note

This project is intended as a learning/project application. The generators use Python's `random` module, which is **not intended for security-sensitive cryptographic password generation**.

For passwords that must provide strong security guarantees, use a cryptographically secure random generator such as Python's `secrets` module and apply an appropriate password-generation policy.

## Possible Improvements

Some useful future improvements include:

- Use Python's `secrets` module for security-sensitive password generation.
- Add a **Copy to Clipboard** button.
- Add password-strength estimation.
- Add a password history section using Streamlit Session State.
- Add custom word-list support.
- Improve error handling and input validation.
- Add automated tests for all generator classes.
- Add a requirements file such as `requirements.txt`.
- Improve the visual design with custom Streamlit CSS.
- Deploy the application using Streamlit Community Cloud or another hosting platform.

## License

Add your preferred license here, for example **MIT License**, if you plan to publish this project publicly.

## Author

Created as a Python and Streamlit password-generator project.
