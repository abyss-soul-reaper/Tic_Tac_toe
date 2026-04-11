from helpers import *
from interface.cli import Cli
from game.state import GameState
from game.logic import check
from game_enum import *
from registry import Registry

class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.game_state = GameState()
        self.enums = GameResult
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
            if status in [self.enums.WIN, self.enums.DRAW]:
                print(self.registry.check_map().get(status))
                break

if __name__ == "__main__":
    game = GameLoop()
    game.play_game()

    
    # game.set_players()
    # game.cli.play_turn(game.game_state)
    # game.cli.display_board(game.game_state.board.board, game.game_state.board.size)
