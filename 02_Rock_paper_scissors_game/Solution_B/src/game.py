import random

class Rock_Paper_Scissor:
    def __init__(self, name):
        self.choice = ["rock", "paper", "scissor"]
        self.player_name = name
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
    
    def get_user_choice(self):
        player_choice = input(f"Please Choose Your Move ({self.choice}) : ")
        if player_choice.lower() in self.choice:
            print(f"Player Choice is : {player_choice}")
            return player_choice.lower()
        elif player_choice.lower() == 'q':
            return False
        
        print("The input you entered is incorrect, please try again !!!!")
        return self.get_user_choice()
    
    def get_computer_choice(self):
        computer_choice = random.choice(self.choice)
        print(f"Computer Choice is : {computer_choice}")
        return computer_choice
    
    def decide_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            self.tie_score += 1
            return f"The game was tied."
        elif (user_choice == "rock") and (computer_choice == "paper"):
            self.computer_score += 1
            return f"Computer Won."
        elif (user_choice == "rock") and (computer_choice == "scissor"):
            self.player_score += 1
            return f"You won."
        elif (user_choice == 'paper') and (computer_choice == "rock"):
            self.player_score += 1
            return f"You won."
        elif (user_choice == "paper") and (computer_choice == "scissor"):
            self.computer_score += 1
            return f"Computer Won."
        elif (user_choice == "scissor") and (computer_choice == "paper"):
            self.player_score += 1
            return f"You Won."
        elif (user_choice == "scissor") and (computer_choice == "rock"):
            self.computer_score += 1
            return f"Computer Won."
    
    def show_final_result(self):
        print("\n" + "=" * 40)
        print("FINAL RESULTS")
        print("=" * 40)
        print(f"Your Score: {self.player_score}")
        print(f"Computer Score: {self.computer_score}")
        print(f"Ties: {self.tie_score}")
        print("-" * 40)
        
        if self.player_score > self.computer_score:
            print(f"🏆 Congratulations {self.player_name}! You won the game!")
            print()
        elif self.computer_score > self.player_score:
            print("💻 Computer won the game! Better luck next time!")
            print()
        else:
            print("🤝 The game ended in a tie!")
            print()
        print("=" * 40)
    
    def play(self):
        print(f"Welcome to the game of rock, paper, scissors, {self.player_name}")
        for item in range(10):
            print("*" * 40)
            print(f"Round {item + 1}") 
            print(f"Score: You {self.player_score}\nComputer {self.computer_score}\nTies {self.tie_score}")
            
            user_choice = self.get_user_choice()
            if user_choice == False:
                print("You are out of the game.")
                break
            computer_choice = self.get_computer_choice()
            print(self.decide_winner(user_choice, computer_choice))
        
        
        self.show_final_result()



if __name__ == "__main__":
    name = input("PLease Enter a Name : ")
    
    while True:
        g = Rock_Paper_Scissor(name)
        g.play()
        
        continue_game = input("Do you Want to play again? (Y/n) or enter q to exit() : ").lower()
        if continue_game.lower() == "q":
            break