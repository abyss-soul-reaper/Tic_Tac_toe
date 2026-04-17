from menus import Menus
from utils.helpers import *
from game.board import Board
from interface.cli import Cli
from game.game_logic import *
from players.player import Player
from game.game_state import GameState
from pipeline.registry import Registry
from pipeline.pipeline import Pipeline
from action_service import ActionService
from pipeline.dispatcher import Dispatcher
from pipeline.action_config import Resolver



class GameLoop:
    def __init__(self):
        self.cli = Cli()
        self.registry = Registry(self)
        self.action_service = ActionService()
        self.pipeline = Pipeline(self.registry)
        self.dispatcher = Dispatcher(self.registry, self.pipeline, Resolver)

    def get_menu_action(self):
        return self.cli.select_action(self.action_service.current_menu)

    def players_data(self, players_count=2):
        players_data = []

        for idx in range(1,players_count+1):
            name = self.cli.player_name(idx)
            symbol = self.cli.player_symbol(name)
            players_data.append({"name": name, "symbol": symbol})

            clear_screen()
        print(players_data)        

        # for idx in range(1,players_count+1):
        #     name = self.cli.player_name(idx)
        #     symbol = self.cli.player_symbol(name)
        #     clear_screen()
            
        # return {"name": name, "symbol": symbol}

    def set_players(self, players_data):
        Player(players_data.get("name"), players_data.get("symbol"))

    def play_game(self):
        while True:
            action = self.get_menu_action()
            self.dispatcher.execute(action)

    def start_game(self):
        self.action_service.navigate_to(Menus.GAME_SETUP)





GameLoop().players_data()

