from menus import Menus
from game.board import Board
from interface.cli import Cli
from game.game_logic import *
from players.player import Player
from menu_manager import MenuManager
from game.game_state import GameState
from pipeline.registry import Registry
from pipeline.pipeline import Pipeline
from pipeline.game_enum import get_menu_actions
from pipeline.dispatcher import Dispatcher
from pipeline.action_config import Resolver



class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.registry = Registry(self)
        self.menu_manager = MenuManager()
        self.pipeline = Pipeline(self.registry)
        self.dispatcher = Dispatcher(self.registry, self.pipeline, Resolver)

    def get_menu_action(self):
        return self.cli.select_action(self.menu_manager.current_menu)
        
    def play_game(self):
        while True:
            action = self.get_menu_action()
            self.dispatcher.execute(action)

    def start_game(self):
        self.menu_manager.navigate_to(Menus.GAME_SETUP)









    # def setup_player_name(self, name):
    #     return Player(name)
    
    # def setup_player_symbol(self, symbol):
    #     return Player(symbol)

    # def start_game(self, player_data):
    #     GameState(player_data, Board())
    #     while True:
    #         self.cli.play_turn(GameState.current_player, GameState.board)
    #         status = check(GameState.board)




    

    # def set_players(self):
    #     players = []
    #     for _ in range(2):
    #         name = self.cli.player_name()
    #         symbol = self.cli.player_symbol()
    #         players.append(Player(name, symbol))
    #         clear_screen()
    #     return players
        
    # def play_game(self):
    #     players = self.set_players()
    #     self.game_state = GameState(players, Board())

    #     player = self.game_state.current_player
    #     board = self.game_state.board
    #     while True:
    #         self.cli.play_turn(player, board)
    #         status = check(board, self.enums)
    #         self.cli.status_message(player, status)
    #         self.game_state.switch_player()
    #         player = self.game_state.current_player


    # def start_game(self):
    #     actions = get_menu_actions(self.current_menu)
    #     action = self.cli.select_action(actions)
    #     clear_screen()
    #     menu = self.registry.main_menu_actions()
    #     if action in menu.keys():
    #         menu.get(action)()

    # def restart_game(self):
    #     clear_screen()
    #     self.game_state.Reset()
    #     self.cli.play_turn(self.game_state.current_player, self.game_state.board)
        
# if __name__ == "__main__":


# GameLoop().dispatcher.execute("START_GAME")

# GameLoop().dispatcher.execute("SET_PLAYERS")


GameLoop().play_game()