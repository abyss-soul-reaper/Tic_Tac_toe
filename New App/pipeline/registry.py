from pipeline.game_enum import GameEnum
from utils.validation import *

class Registry:
    def __init__(self, gameloop):
        self.gameloop = gameloop



    def input_actions_map(self):
        INPUT_ACTION_MAP = {
            GameEnum.SET_PLAYERS_NAME: self.gameloop.cli.player_name,
            GameEnum.SET_PLAYERS_SYMBOL: self.gameloop.cli.player_symbol
        }
        return INPUT_ACTION_MAP

    def system_actions_map(self):
        SYSTEM_ACTION_MAP = {
            GameEnum.START_GAME: self.gameloop.start_game,
            # GameEnum.SET_PLAYERS: self.gameloop.setup_players
        }
        return SYSTEM_ACTION_MAP

    # ---- Pipeline Action Maps ----
    def validate_map(self):
        VALIDATE_MAP = {
            "name": validate_name,
            "symbol": validate_symbol,
            "board_size": validate_board_size
        }
        return VALIDATE_MAP
    
    def normalize_map(self):
        NORMALIZE_MAP = {
            "name": lambda v: v.strip().title(),
            "symbol": lambda v: v.strip().upper(),
            "board_size": lambda v: v.strip()
        }
        return NORMALIZE_MAP
