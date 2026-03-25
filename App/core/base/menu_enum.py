from enum import Enum


# =========================
# 🎮 GAME ACTIONS
# =========================
class GameAction(Enum):

    # 🎮 Game Flow
    START_GAME = "Start Game"
    START_MATCH = "Start Match"
    RESTART_GAME = "Restart Game"
    QUIT_GAME = "Quit Game"

    # 👤 Player Setup
    SET_PLAYER_NAME = "Enter Player Name"
    SET_PLAYER_SYMBOL = "Choose Symbol"

    # ⚙️ Settings
    OPEN_SETTINGS = "Settings"
    CHANGE_BOARD_SIZE = "Change Board Size"
    RESET_SETTINGS = "Reset Settings"

    # ℹ️ Info / Scores
    SHOW_GAME_INFO = "Game Info"
    VIEW_SCORES = "View Scores"

    # 💾 Data (للاستخدام الداخلي بعدين)
    SAVE_GAME = "Save Game"
    LOAD_GAME = "Load Game"
    SAVE_SCORE = "Save Score"

    # 🧭 Navigation
    NAV_BACK = "Back"
    NAV_TO_MAIN = "Back To Main Menu"


# =========================
# 📋 MENU DEFINITIONS
# =========================
MENU_ACTIONS = {

    "main_menu": [
        GameAction.START_GAME,
        GameAction.SHOW_GAME_INFO,
        GameAction.VIEW_SCORES,
        GameAction.OPEN_SETTINGS,
        GameAction.QUIT_GAME,
    ],

    "game_setup": [
        GameAction.SET_PLAYER_NAME,
        GameAction.SET_PLAYER_SYMBOL,
        GameAction.CHANGE_BOARD_SIZE,
        GameAction.START_MATCH,
        GameAction.NAV_BACK,
    ],

    "settings_menu": [
        GameAction.CHANGE_BOARD_SIZE,
        GameAction.RESET_SETTINGS,
        GameAction.NAV_BACK,
    ],

    "end_menu": [
        GameAction.RESTART_GAME,
        GameAction.VIEW_SCORES,
        GameAction.NAV_TO_MAIN,
        GameAction.QUIT_GAME,
    ],
}


# =========================
# 🧭 HELPER
# =========================
def get_menu_actions(menu_name: str):
    if menu_name not in MENU_ACTIONS:
        raise ValueError(f"Invalid menu: {menu_name}")
    return MENU_ACTIONS[menu_name]




    