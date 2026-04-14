from interface.cli_helper import *
from validation import *
from helpers import *

class Cli:
    """A class to handle command-line interactions for the Tic Tac Toe game.
    """

    # ----- Player Interaction Methods -----
    @staticmethod
    def player_name():
        name = input(f"Enter your name (Only Letters!): ").strip().title()
        while not validate_name(name):
            name = input("Invalid name! Enter a valid name (Only Letters!): ").strip().title()
        return name

    @staticmethod
    def player_symbol():
        symbol = input(f"choose your symbol (X OR O): ").strip().upper()
        while not validate_symbol(symbol):
            symbol = input("Invalid symbol! Please enter 'X' or 'O': ").strip().upper()
        return symbol


    def change_board_size(self):
        size = input("Enter New Board Size (e.g., 3 for 3x3): ")
        return size

    def play_turn(self, player, board):
        self.display_board(board.board, board.size)

        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if update_cell(board, player.symbol, cell_choice):
                    break
                else:
                    print("Invalid Move! Try Again.")

            except ValueError:
                print("Please Enter a number between (1-9).")
        clear_screen()

    def status_message(self, status):
        if status == "win":
            print(f"Congratulations! {self.curt_pl.name} wins!")
            exit()
        elif status == "draw":
            print("It's a draw!")
            exit()


    # ----- Board Interaction Methods -----
    def display_board(self, board, size):
        for i in range(0, len(board), size):
            print("|".join(board[i: i+size]))
            if i < (len(board) - size):
                print("_" * (2 * size - 1))

    # ----- Menu Interaction Methods -----
    @staticmethod
    def game_info():
        info = [
            "Tic-Tac-Toe is a classic two-player strategy game.\n",
            "\nOpponents take turns marking spaces in a 3x3 grid.\n",
            "\nThe objective is to align three symbols."
        ]
        print("\n--- GAME INFO ---\n")
        print(''.join(info))
        print("\n","-"*30)

        
    @staticmethod
    def select_action(menu):
        INDEX_MAP = mapping(menu)
        for idx, action in INDEX_MAP.items():
            print(f"{idx}. {action}")
            
        while True:
            try:
                choice = int(input("Select an option: "))
                if choice in INDEX_MAP:
                    return resolver(INDEX_MAP[choice])
                else:
                    print("Invalid choice! Please select a valid option.")
            except ValueError:
                print("Please enter a number corresponding to the options.")




