from enum import Enum


# =========================
# 🎮 CORE GAME ACTIONS
# =========================
class GameAction(Enum):
    START_GAME = "start_game"
    RESTART_GAME = "restart_game"
    QUIT_GAME = "quit_game"


# =========================
# 📋 MAIN MENU ACTIONS
# =========================
class MainMenuAction(Enum):
    START_GAME = "start_game"
    GAME_INFO = "game_info"
    SCORE_RECORD = "score_record"
    SETTINGS = "settings"          # (اختياري)
    LOAD_GAME = "load_game"        # (اختياري)
    QUIT_GAME = "quit_game"


# =========================
# 🏁 END GAME MENU ACTIONS
# =========================
class EndMenuAction(Enum):
    RESTART_GAME = "restart_game"
    VIEW_SCORE = "view_score"      # (اختياري)
    BACK_TO_MAIN = "back_to_main"  # (مهم)
    QUIT_GAME = "quit_game"


# =========================
# ⚙️ SETTINGS MENU ACTIONS
# =========================
class SettingsAction(Enum):
    CHANGE_BOARD_SIZE = "change_board_size"   # (أنت ناوي تعملها)
    CHANGE_PLAYER_NAME = "change_player_name"
    RESET_SETTINGS = "reset_settings"
    BACK = "back"


# =========================
# 💾 DATA / DATABASE ACTIONS
# =========================
class DataAction(Enum):
    SAVE_GAME = "save_game"
    LOAD_GAME = "load_game"
    SAVE_SCORE = "save_score"
    GET_SCORES = "get_scores"
    CLEAR_SCORES = "clear_scores"


# =========================
# 🤖 (FUTURE) AI / DIFFICULTY
# =========================
class DifficultyLevel(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


# =========================
# 🧱 GAME CONFIG OPTIONS
# =========================
class GameConfig(Enum):
    BOARD_3X3 = "3x3"
    BOARD_4X4 = "4x4"
    BOARD_5X5 = "5x5"


# =========================
# 🧭 GENERIC NAVIGATION
# =========================
class NavigationAction(Enum):
    BACK = "back"
    EXIT = "exit"