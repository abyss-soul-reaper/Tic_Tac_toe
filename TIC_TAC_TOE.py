import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

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
        
        while not (symbol.isalpha() and len(symbol) == 1 and symbol in self.SYMBOLS):
            symbol = input(f"Invalid! Please enter a SINGLE letter: ").strip().upper()

        self.symbol = symbol
        print(self.symbol)

class Menu:
    MAIN_MENU_OPTIONS = {
        "1": "START_GAME",
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
        return self.display_and_validate(self.MAIN_MENU_OPTIONS)

    def display_end_game_menu(self):
        print("Game Over!")
        return self.display_and_validate(self.END_GAME_OPTIONS)
    
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
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.curt_pl_idx = 0

    def start_game(self):
        return self.menu.display_main_menu()

    def setup_players(self):
        for idx, player in enumerate(self.players, 1):
            print(f"Player{idx}. Enter Your Details:")
            player.choose_name()
            player.choose_symbol()

    def game(self):
        END_MENU = self.set_end_menu()
        self.setup_players()
        clear_screen()
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                action = self.menu.display_end_game_menu()
                if action in END_MENU.keys():
                    END_MENU.get(action)()

    def play_turn(self):
        player = self.players[self.curt_pl_idx]
        self.board.display_board()

        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                
                if 1<= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move! Try Again.")

            except ValueError:
                print("Please Enter a number between (1-9).")

        self.switch_player()

    def switch_player(self):
        self.curt_pl_idx -= 1

    def quit_game(self):
        print("\nThank You For Playing!")

    def play_game(self):
        MENU = self.set_main_menu()
        action = self.start_game()
        if action in MENU.keys():
            MENU.get(action)()
        else:
            print("fuck")
        
    @staticmethod
    def game_info():
        info = [
            "Tic-Tac-Toe is a classic two-player strategy game.\n",
            "Opponents take turns marking spaces in a 3x3 grid.\n",
            "The objective is to align three symbols."
        ]
        print(''.join(info))

    def check_win(self):
        win_combainations = [
            [0,1,2], [3,4,5], [6,7,8],   # rows
            [0,3,6], [1,4,7], [2,5,8],   # columns
            [0,4,8], [2,4,6]             # diagonals  
        ]

        for combo in win_combainations:
            if (self.board.board[combo[0]] == 
                self.board.board[combo[1]] == 
                self.board.board[combo[2]]):
                return True
            return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.curt_pl_idx = 0
        self.play_game()

    def set_main_menu(self):
        MAIN_MENU = {
            "START_GAME": self.game,
            "GAME INFO": self.game_info,
            "SCORE RECORD": "",
            "QUIT GAME": self.quit_game
        }
        return MAIN_MENU
    
    def set_end_menu(self):
        END_GAME_MENU = {
            "RESTART GAME": self.restart_game,
            "QUIT GAME": self.quit_game
        }
        return END_GAME_MENU


if __name__ == "__main__":
    Game().play_game()