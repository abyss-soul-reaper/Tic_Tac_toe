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

    # Define End Game options
    RESTART_GAME = "RESTART GAME"
    END_QUIT_GAME = "QUIT GAME"

MENU_ACTIONS = {
    "main_menu": [
        GameEnum.START_GAME,
        GameEnum.GAME_INFO,
        GameEnum.SCORE_RECORD,
        GameEnum.QUIT_GAME,
    ],
    "end_game_menu": [
        GameEnum.RESTART_GAME,
        GameEnum.END_QUIT_GAME,
    ]
}

def get_menu_actions(menu_name: str):
    if menu_name not in MENU_ACTIONS:
        raise ValueError(f"Invalid menu: {menu_name}")
    return MENU_ACTIONS[menu_name]
