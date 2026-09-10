import random
from typing import Tuple


def monty_hall_game(switch_doors : bool) -> bool:
    doors = ['goat', 'car', 'goat']
    random.shuffle(doors)
    
    # Player makes an initial choice
    initial_choice = random.choice(range(3))
    
    # Host opens a door with a goat
    doors_revealed = [i for i in range(3) if (i != initial_choice and doors[i] != 'car')]
    door_revealed = random.choice(doors_revealed)
    
    if switch_doors:
        final_choice = [i for i in range(3) if (i != initial_choice and i != door_revealed)][0]
    else:
        final_choice = initial_choice
    
    
    return doors[final_choice] == 'car'


def simulate_game(number_of_game : int) -> Tuple[int, int]:
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(number_of_game)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(number_of_game)])
    
    return num_wins_with_switching/number_of_game, num_wins_without_switching/number_of_game



if __name__ == "__main__":
    print("=" * 50)
    print("Welcome to the Monty Hall Simulation")
    
    number_of_game = int(input("Enter the number of games to simulate: "))
    win_rate_with_switching, win_rate_without_switching = simulate_game(number_of_game)
    
    print(f"Win rate with switching: {win_rate_with_switching * 100} %")
    print(f"Win rate without switching: {win_rate_without_switching * 100} %")
    
    print("=" * 50)