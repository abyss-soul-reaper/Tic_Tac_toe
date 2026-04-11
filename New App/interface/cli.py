from interface.cli_helper import *

class Cli:
    """A class to handle command-line interactions for the Tic Tac Toe game.
    """
    SYMBOLS = ['X', 'O']

    # ----- Player Interaction Methods -----
    def player_name(self, idx):
        name = input(f"Player {idx} enter your name (Only Letters!): ").strip().title()
        while not name.isalpha():
            name = input("Invalid name! Make Sure Your Name Is Alphabetic: ")
        return name

    def player_symbol(self, name):
        symbol = input(
            f"{name} choose your symbol (X OR O): ").strip().upper()
        while not symbol in self.SYMBOLS:
            symbol = input(f"Invalid! please enter a Valid symbol: ").strip().upper()

        self.SYMBOLS.remove(symbol)
        return symbol

    def change_board_size(self):
        size = input("Enter New Board Size (e.g., 3 for 3x3): ")
        return {"board_size": size}

    def play_turn(self, game_state):
        player = game_state.players[game_state.curt_pl_idx]
        self.display_board(game_state.board.board, game_state.board.size)

        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
                self.curt_pl_idx = player
                cell_choice = int(input("Choose a cell (1-9): "))
                
                if 1<= cell_choice <=9 and game_state.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid Move! Try Again.")

            except ValueError:
                print("Please Enter a number between (1-9).")

        switch_player(game_state)


    # ----- Board Interaction Methods -----
    def display_board(self, board, size):
        for i in range(0, len(board), size):
            print("|".join(board[i: i+size]))
            if i < (len(board) - size):
                print("_" * (2 * size - 1))




