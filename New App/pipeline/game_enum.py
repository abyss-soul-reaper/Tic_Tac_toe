from enum import Enum

class GameEnum(Enum):
    # Define game result states
    WIN = "win"
    DRAW = "draw"
    CONTINUE = "continue"

    # Define Menu options
    START_GAME = "START GAME"
    GAME_INFO = "GAME INFO"
    SCORE_RECORD = "SCORE RECORD"
    QUIT_GAME = "QUIT GAME"

    # ⚙️ Settings
    OPEN_SETTINGS = "Settings"
    CHANGE_BOARD_SIZE = "Change Board Size"
    RESET_SETTINGS = "Reset Settings"

    RESTART_GAME = "RESTART GAME"

    # 🧭 Navigation
    NAV_BACK = "Back"

MENU_ACTIONS = {
    "main_menu": [
        GameEnum.START_GAME,
        GameEnum.GAME_INFO,
        GameEnum.SCORE_RECORD,
        GameEnum.OPEN_SETTINGS,
        GameEnum.QUIT_GAME,
    ],

    "settings_menu": [
        GameEnum.CHANGE_BOARD_SIZE,
        GameEnum.RESET_SETTINGS,
        GameEnum.NAV_BACK,
    ],

    "end_menu": [
        GameEnum.RESTART_GAME,
        GameEnum.SCORE_RECORD,
        GameEnum.NAV_BACK,
        GameEnum.QUIT_GAME,
    ],
}

def get_menu_actions(menu_name: str):
    if menu_name not in MENU_ACTIONS:
        raise ValueError(f"Invalid menu: {menu_name}")
    return MENU_ACTIONS[menu_name]
