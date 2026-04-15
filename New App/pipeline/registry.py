from pipeline.game_enum import GameEnum
from utils.validation import *

class Registry:
    def __init__(self, gameloop):
        self.gameloop = gameloop

    @property
    def main_menu_actions(self):
        MAIN_MENU_MAP = {
            GameEnum.START_GAME: self.gameloop.play_game,
            # GameEnum.GAME_INFO: ,
            # GameEnum.SCORE_RECORD: ,
            # GameEnum.OPEN_SETTINGS: ,
            # GameEnum.QUIT_GAME: 
        }
        return MAIN_MENU_MAP

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
