import os

def clear_screen():
    os.system("cmd" if os.name == "nt" else "clear")

class Player:
    SYMBOLS = ["X", "O"]

    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        name = input("Enter Your Name (Only Letters!): ").strip().title()
        while not name.isalpha():
            name = input("Invalid name! Make Sure Your Name Is Alphabetic: ")
        self.name = name

    def choose_symbol(self):
        symbol = input(
            f"{self.name} Choose Your Symbol (X OR O DEFAULT({self.SYMBOLS[0]})): "
            ).strip().upper()
        
        while True:
            symbol = input(f"Invalid! Please enter a SINGLE letter: ").strip().upper()

            if not (symbol.isalpha() and len(symbol) == 1 and symbol in self.SYMBOLS):
                symbol = self.SYMBOLS[0]
                self.SYMBOLS.pop(0)

            self.symbol = symbol
            print(self.symbol)
            break


class Menu:
    MAIN_MENU_OPTIONS = {
        "1": "START GAME",
        "2": "GAME INFO",
        "3": "SOCRE RECORD",
        "4": "QUIT GAME"
    }
    
    END_GAME_OPTIONS = {
        "1": "RESTART GAME",
        "2": "QUIT GAME"
    }

    def display_main_menu(self):
        print(f"Welcome to Tic_Tac_Toe!")
        self.display_and_validate(self.MAIN_MENU_OPTIONS)

    def display_end_game_menu(self):
        print("Game Over!")
        self.display_and_validate(self.END_GAME_OPTIONS)
    
    @staticmethod
    def display_and_validate(info_dict):
        while True:
            for idx, option in info_dict.items():
                print(f"-{idx}. --- {option.center(15)} ---")

            choice = input()

            if choice in info_dict.keys(): return info_dict[choice]
            else: print("\ninvalid option!")


class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, len(self.board), 3):
            print("|".join(self.board[i: i+3]))
            if i < (len(self.board) - 3):
                print("_" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()


class Game:
    MAIN_MENU = {
        "START": "",
        "INFO": [
                "Tic-Tac-Toe is a classic two-player strategy game.\n",
                "Opponents take turns marking spaces in a 3x3 grid.\n",
                "The objective is to align three symbols."
            ],
        "SCORE": "",
        "QUIT": ""
    }

    END_GAME_MENU = {
        "RESTART GAME": "",
        "QUIT GAME": ""
    }

    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.curt_pl_idx = 0

    def start_game(self):
        choice = self.menu.display_main_menu()

    def setup_players(self):
        for idx, player in enumerate(self.players, 1):
            print(f"Player{idx}. Enter Your Details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def game(self):
        while True:
            pass

    def play_turn(self):
        pass

    def quit_game(self):
        print("\nThank You For Playing!")


    def play_game(self):
        pass

# Board().display_board()