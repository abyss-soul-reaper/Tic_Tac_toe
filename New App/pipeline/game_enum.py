from enum import Enum

class GameEnum(Enum):
    # Define game result states
    WIN = "win"
    DRAW = "draw"
    CONTINUE = "continue"

    # 🎮 Game Flow
    START_GAME = "START_GAME"
    START_MATCH = "START_MATCH"
    RESTART_GAME = "RESTART_GAME"
    QUIT_GAME = "QUIT_GAME"

    # 👤 Player Setup
    SET_PLAYERS = "SET_PLAYERS"
    
    # ⚙️ Settings
    SETTINGS = "SETTINGS"
    CHANGE_BOARD_SIZE = "CHANGE_BOARD_SIZE"
    RESET_SETTINGS = "RESET_SETTINGS"

    # ℹ️ Info / Scores
    GAME_INFO = "GAME_INFO"
    SCORE_RECORD = "SCORE_RECORD"

    # 💾 Data (للاستخدام الداخلي بعدين)
    SAVE_GAME = "SAVE_GAME"
    LOAD_GAME = "LOAD_GAME"
    SAVE_SCORE = "SAVE_SCORE"

    # 🧭 Navigation
    NAV_BACK = "NAV_BACK"

MENU_ACTIONS = {
    "main_menu": [
        GameEnum.START_GAME,
        GameEnum.GAME_INFO,
        GameEnum.SCORE_RECORD,
        GameEnum.SETTINGS,
        GameEnum.QUIT_GAME,
    ],

    "game_setup": [
        GameEnum.SET_PLAYERS,
        GameEnum.CHANGE_BOARD_SIZE,
        GameEnum.START_MATCH,
        GameEnum.NAV_BACK,
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
