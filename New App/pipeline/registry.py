from pipeline.game_enum import GameEnum
from utils.validation import *

class Registry:
    def __init__(self, gameloop):
        self.gameloop = gameloop

    def input_actions_map(self):
        INPUT_ACTION_MAP = {
            GameEnum.START_MATCH: self.gameloop.play_turn,
            GameEnum.SET_PLAYERS: self.gameloop.players_data,
            GameEnum.CHANGE_BOARD_SIZE: self.gameloop.change_board_size,
            GameEnum.CHANGE_PLAYERS_COUNT: self.gameloop.change_players_count,
            GameEnum.GAME_INFO: self.gameloop.game_info

        }
        return INPUT_ACTION_MAP

    def system_data_actions_map(self):
        SYSTEM_ACTION_MAP = {
            GameEnum.START_GAME: self.gameloop.start_game,
            GameEnum.NAV_BACK: self.gameloop.navigate_back,
            GameEnum.QUIT_GAME: self.gameloop.quit_game,
            GameEnum.SETTINGS: self.gameloop.settings_menu,
            GameEnum.RESET_SETTINGS: self.gameloop.reset_game,
            GameEnum.RESTART_GAME: self.gameloop.restart_game
        }
        return SYSTEM_ACTION_MAP


