import os
from uuid import uuid4
import sqlite3

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

conn = sqlite3.connect("game_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id TEXT PRIMARY KEY,
        player_name TEXT,
        score INTEGER
    )
""")

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

        self.SYMBOLS.remove(symbol)
        self.symbol = symbol

class Menu:
    MAIN_MENU_OPTIONS = {
        "1": "START GAME",
        "2": "GAME INFO",
        "3": "SCORE RECORD",
        "4": "QUIT GAME"
    }
    
    END_GAME_OPTIONS = {
        "1": "RESTART GAME",
        "2": "QUIT GAME"
    }

    def display_main_menu(self):
        return self.display_and_validate(self.MAIN_MENU_OPTIONS)

    def display_end_game_menu(self):
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
        self.main_act = self.main_actions()
        self.end_act = self.end_actions()
        self.curt_pl_idx = 0
        self.player_ids = []
        self.curt_pl = None

    def main_actions(self):
        MAIN_MENU = {
            "START GAME": self.play_game,
            "GAME INFO": self.game_info,
            "SCORE RECORD": "",
            "QUIT GAME": self.quit_game
        }
        return MAIN_MENU

    def end_actions(self):
        END_MENU = {
            "RESTART GAME": self.restart_game,
            "QUIT GAME": self.quit_game
        }
        return END_MENU

    def setup_players(self):
        for idx, player in enumerate(self.players, 1):
            print(f"Player{idx}. Enter Your Details:")
            player.choose_name()
            player.choose_symbol()
            self.set_id(player.name)
        clear_screen()

    def start_game(self):
        action = self.menu.display_main_menu()
        if action in self.main_act.keys():
            self.main_act.get(action)()
        
    def play_game(self):
        self.setup_players()
        while True:
            self.play_turn()
            if self.check():
                action = self.menu.display_end_game_menu()
                if action in self.end_act.keys():
                    self.end_act.get(action)()

    def check(self):
        if self.check_win():
            print(f"{self.curt_pl.name} Wins!")
            self.save_score(self.get_id(self.curt_pl))
            return True
        elif self.check_draw():
            print("It's a Draw!")
            return True
        return False

    def play_turn(self):
        player = self.players[self.curt_pl_idx]
        self.board.display_board()

        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                self.curt_pl = player
                cell_choice = int(input("Choose a cell (1-9): "))
                
                if 1<= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move! Try Again.")

            except ValueError:
                print("Please Enter a number between (1-9).")

        self.switch_player()

    def get_id(self, player):
        cursor.execute("SELECT id FROM scores WHERE player_name = ?", (player.name,))
        return cursor.fetchone()[0]

    def set_id(self, player):
        pl_id = str(uuid4())
        self.player_ids.append(pl_id)

        cursor.execute("INSERT INTO scores (id, player_name) VALUES (?, ?)", (pl_id, player))
        self.commit()

    def save_score(self, id):
        cursor.execute("UPDATE scores SET score = score + 1 WHERE id == ?", (id,))
        self.commit()

    def commit(self):
        conn.commit()

    def switch_player(self):
        self.curt_pl_idx = 1 - self.curt_pl_idx
      
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
        clear_screen
        self.board.reset_board()
        self.curt_pl_idx = 0
        self.play_turn()

    def quit_game(self):
        print("\nThank You For Playing!")
        exit()

    def run_cycle(self):
        print(f"\nWelcome to Tic_Tac_Toe!")
        while True:
            self.start_game()

if __name__ == "__main__":
    Game().run_cycle()








# def set_id(self, player):
#     pl_id = str(uuid4())
#     self.player_ids.append(pl_id)

#     cursor.execute("INSERT INTO scores (id, player_name) VALUES (?, ?)", (pl_id, player.name))
#     self.commit()
