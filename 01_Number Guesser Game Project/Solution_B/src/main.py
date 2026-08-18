from game_logic.number_generator import generate_random_number
from game_logic.hint_generator import provide_hint
from game_logic.scorer import Scorer
from utils.input_validator import get_valid_input

def main():
    number_to_guess = generate_random_number(1, 100)
    scorer = Scorer()

    while True:
        print("*" * 40)
        guess = get_valid_input(1, 100)
        if guess == number_to_guess:
            print(f"\nCongratulations! Your final score is: {scorer.get_score()}")
            print("*" * 40)
            temp = input("Do you want to play again? (Y/N) : ").lower()
            if temp == "y":
                main()
            else:
                break
        else:
            hint = provide_hint(guess, number_to_guess)
            scorer.decrement_score()

if __name__ == "__main__":
    main()
