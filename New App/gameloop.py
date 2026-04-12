from helpers import *
from game_enum import *
from game.logic import check
from interface.cli import Cli
from registry import Registry
from game.state import GameState

class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.enums = GameEnum
        self.game_state = GameState()
        self.registry = Registry(self.enums)

    def set_players(self):
        for idx, player in enumerate(self.game_state.players,1):
            player.name = self.cli.player_name(idx)
            player.symbol = self.cli.player_symbol(player.name)
            clear_screen()

    def play_game(self):
        self.set_players()
        while True:
            self.cli.play_turn(self.game_state)
            status = check(self.game_state, self.enums)
            self.cli.status_message(status.value)


if __name__ == "__main__":
    game = GameLoop()
    game.play_game()

    
    # game.set_players()
    # game.cli.play_turn(game.game_state)
    # game.cli.display_board(game.game_state.board.board, game.game_state.board.size)
