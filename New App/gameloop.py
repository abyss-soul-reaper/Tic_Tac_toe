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
        self.enums = GameEnum
        self.cli = Cli(self.enums)
        self.game_state = GameState
        self.registry = Registry(self, self.enums)
        self.current_menu = "main_menu"

    def set_players(self):
        players = []
        for _ in range(2):
            name = self.cli.player_name()
            symbol = self.cli.player_symbol()
            players.append(Player(name, symbol))
            clear_screen()
        return players
        
    def play_game(self):
        players = self.set_players()
        self.game_state = GameState(players, Board())

        player = self.game_state.current_player
        board = self.game_state.board

        while True:
            self.cli.play_turn(player, board)
            status = check(board, self.enums)
            self.cli.status_message(player, status)
            self.game_state.switch_player()
            player = self.game_state.current_player


    def start_game(self):
        actions = get_menu_actions(self.current_menu)
        action = self.cli.select_action(actions)
        clear_screen()
        menu = self.registry.main_menu_actions()
        if action in menu.keys():
            menu.get(action)()
        
if __name__ == "__main__":
    game = GameLoop()
    game.start_game()
    # game.play_game()

    
    # game.set_players()
    # game.cli.play_turn(game.game_state)
    # game.cli.display_board(game.game_state.board.board, game.game_state.board.size)

