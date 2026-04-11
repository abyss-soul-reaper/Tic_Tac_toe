from interface.cli import Cli
from game.state import GameState
from helpers import *

class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.game_state = GameState()

    def set_players(self):
        for idx in range(1, 3):
            player = self.cli.player_name(idx)
            symbol = self.cli.player_symbol(player)
            clear_screen()

if __name__ == "__main__":
    game = GameLoop()
    game.set_players()
    game.cli.display_board(game.game_state.board.board, game.game_state.board.size)
