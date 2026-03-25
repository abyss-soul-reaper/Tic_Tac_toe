from App.core.validation.validators import *
from App.core.base.menu_enum import *

class Registry:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl

    def main_menu_actions():
        ACTIONS_MAP = {
            GameAction.START_GAME: '',
            GameAction.SHOW_GAME_INFO: '',
            GameAction.VIEW_SCORES: '',
            GameAction.OPEN_SETTINGS: '',
            GameAction.QUIT_GAME: ''
        }
        return ACTIONS_MAP

    def game_setup_actions():
        ACTIONS_MAP = {
            GameAction.SET_PLAYER_NAME: '',
            GameAction.SET_PLAYER_SYMBOL: '',
            GameAction.CHANGE_BOARD_SIZE: '',
            GameAction.START_MATCH: '',
            GameAction.NAV_BACK: ''
        }
        return ACTIONS_MAP
    
    def settings_menu_actions():
        ACTIONS_MAP = {
            GameAction.CHANGE_BOARD_SIZE: '',
            GameAction.RESET_SETTINGS: '',
            GameAction.NAV_BACK: ''
        }
        return ACTIONS_MAP
    
    def end_menu_actions():
        ACTIONS_MAP = {
            GameAction.RESTART_GAME: '',
            GameAction.VIEW_SCORES: '',
            GameAction.NAV_TO_MAIN: '',
            GameAction.QUIT_GAME: ''
        }
        return ACTIONS_MAP

    def get_validation_map():
        VALIDATION_MAP = {
            "name": is_non_empty,
            "symbol": is_valid_symbol,
            "board_size": is_valid_size
        }
        return VALIDATION_MAP
    
    def get_normalization_map():
        NORMALIZATION_MAP = {
            "name":lambda v: v.strip().title(),
            "symbol":lambda v: v.strip().upper(),
            "board_size":lambda v: v.strip()
        }
        return NORMALIZATION_MAP

