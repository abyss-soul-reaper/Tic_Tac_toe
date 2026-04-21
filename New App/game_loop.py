from menus import Menus
from utils.helpers import *
from game.game_logic import *
from interface.cli import Cli
from players.player import Player
from game.game_board import Board
from game.game_state import GameState
from pipeline.registry import Registry
from pipeline.pipeline import Pipeline
from pipeline.game_enum import GameEnum
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

    def start_game(self):
        self.action_service.navigate_to(Menus.GAME_SETUP)

    def settings_menu(self):
        self.action_service.navigate_to(Menus.SETTINGS_MENU)

    def end_menu(self):
        self.action_service.navigate_to(Menus.END_MENU)

    def players_data(self, players_count=2):
        used_symbols = self.action_service.used_symbols

        for idx in range(1, players_count+1):
            name = self.cli.player_name(idx)
            symbol = self.cli.player_symbol(name, used_symbols)

            clear_screen()
            used_symbols.add(symbol)
            self.action_service.players.append(Player(name, symbol))

    def change_players_count(self):
        current_count = self.action_service.players_count
        new_count = self.cli.change_players_count(current_count)

        self.action_service.players_count = new_count

    def change_board_size(self):
        current_size = self.action_service.board_size
        new_size = self.cli.change_board_size(current_size)

        self.action_service.set_board_size(new_size)

    def game_state(self):
        return GameState(self.action_service.players, Board(self.action_service.board_size))

    def play_turn(self):
        game_state = self.game_state()
        while True:
            try:
                self.cli.play_turn(game_state.current_player, game_state.board)
                status = check(game_state.board)

                if status in [GameEnum.WIN, GameEnum.DRAW]:
                    self.cli.status_message(game_state.current_player, status)
                    self.end_menu()
                    break

                game_state.switch_player()
            except:
                self.cli.error_message("An error occurred while playing the turn, Please try again.")
                break

    def restart_game(self):
        self.play_turn()

    def reset_game(self):
        game_state = self.game_state()
        self.action_service.reset()
        game_state.reset()

    def game_info(self):
        self.cli.game_info()

    def navigate_back(self):
        self.action_service.navigate_back()

    def quit_game(self):
        self.action_service.quit_game()

    def play_game(self):
        while True:
            action = self.get_menu_action()
            res = self.dispatcher.execute(action)







GameLoop().play_game()

