from pipeline.game_enum import get_menu_actions
from interface.cli_helper import *
from utils.helpers import *

class Cli:
    """A class to handle command-line interactions for the Tic Tac Toe game.
    """
    # ----- Player Interaction Methods -----
    @staticmethod
    def player_name(player_idx):
        name = input(f"Player {player_idx} enter your name (Only Letters!): ")
        return name
    @staticmethod
    def player_symbol(name):
        symbol = input(f"{name} choose your symbol (X OR O): ")
        return symbol

    @staticmethod
    def change_board_size():
        size = input("Enter New Board Size (e.g., 3 for 3x3): ")
        return  {"board_size": size}

    def play_turn(self, player, board):
        self.display_board(board.board, board.size)

        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input(f"Choose a cell (1-{board.size ** 2}): "))
                if board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move! Try Again.")

            except ValueError:
                print(f"Please Enter a number between (1-{board.size ** 2}).")
        clear_screen()

    # def status_message(self, player, status):
    #     if status == GameEnum.WIN:
    #         print(f"Congratulations! {player.name} wins!")
    #     elif status == GameEnum.DRAW:
    #         print("It's a draw!")


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

    def show_menu(self, menu):
        menu_actions = get_menu_actions(menu)
        INDEX_MAP = menu_map(menu_actions)

        print(f"\n--- {menu.replace('_', ' ').title()} ---\n")
        for idx, action in INDEX_MAP.items():
            print(f"{idx}. {action.center(20, '-')}")
            print("-" * 30)
        return INDEX_MAP
    
    def select_action(self, menu):
        INDEX_MAP = self.show_menu(menu)
        while True:
            try:
                choice = int(input("\nSelect an option: "))
                clear_screen()

                if choice in INDEX_MAP:
                    return INDEX_MAP[choice].replace(' ', '_').upper()
                else:
                    print("Invalid choice! Please select a valid option.")

            except ValueError:
                print("Please enter a number corresponding to the options.")



