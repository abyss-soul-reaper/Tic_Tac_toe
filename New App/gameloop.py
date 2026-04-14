from helpers import *
from game_enum import *
from game.logic import check
from interface.cli import Cli
from registry import Registry
from game.state import GameState
from players.player import Player
from game.board import Board

class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.enums = GameEnum
        self.game_state = GameState
        self.registry = Registry(self, self.enums)

    def set_players(self):
        players = []
        for _ in range(2):
            name = self.cli.player_name()
            symbol = self.cli.player_symbol()
            players.append(Player(name, symbol))
            clear_screen()
        return players
        
    # def play_game(self):
    #     self.set_players()
    #     while True:
    #         self.cli.play_turn(self.game_state)
    #         status = check(self.game_state, self.enums)
    #         self.cli.status_message(status.value)

    # def start_game(self):
    #     actions = get_menu_actions(self.game_state.menu)
    #     action = self.cli.select_action(actions)
    #     menu = self.registry.main_menu_actions()
    #     if action in menu.keys():
    #         menu.get(action)()
        
if __name__ == "__main__":
    game = GameLoop()
    # game.start_game()
    # game.play_game()

    
    # game.set_players()
    # game.cli.play_turn(game.game_state)
    # game.cli.display_board(game.game_state.board.board, game.game_state.board.size)

