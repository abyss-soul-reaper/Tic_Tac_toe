from config.game_enum import GameEnum

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
