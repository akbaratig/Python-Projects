import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10
        self.player_turn = self.get_random_player_first()
    
    def get_random_player_first(self):
        return random.choice(['X', 'O'])

    def show_board(self):
        print("\n")
        print(f"{self.board[1]}  |  {self.board[2]}  |  {self.board[3]}")
        print("-" * 13)
        print(f"{self.board[4]}  |  {self.board[5]}  |  {self.board[6]}")
        print("-" * 13)
        print(f"{self.board[7]}  |  {self.board[8]}  |  {self.board[9]}")
        print("\n")
    
    def fix_spot(self, cell, player):
        self.board[cell] = player
    
    def is_board_filled(self):
        if ' ' not in self.board[1:]:
            return True
    
    def swap_player_turn(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        else:
            self.player_turn = 'X'
        
    def has_player_won(self, player):
        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        for combination in win_combinations:
            if all([self.board[cell] == player for cell in combination]):
                return True
            
        return False
        
    def start(self):
        while True:
            self.show_board()
            try:
                cell = int(input(f"Player {self.player_turn},\nEnter the cell number from (1 to 9): "))

                if cell in range(1, 10) and self.board[cell] == ' ':
                    self.fix_spot(cell, self.player_turn)

                    if self.has_player_won(self.player_turn):
                        self.show_board()
                        print(f"Player {self.player_turn} wins!")
                        break

                    if self.is_board_filled():
                        print("It's a Draw!")
                        break

                    self.swap_player_turn()

                else:
                    print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")
                
            print("-" * 40)
                


if __name__ == "__main__":
    print("=" * 40)
    print("Welcome to Tic Tac Toe Game!")
    print("=" * 40)
    game = TicTacToe()
    game.start()