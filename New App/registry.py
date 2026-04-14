class Registry:
    def __init__(self, gameloop, enums):
        self.gameloop = gameloop
        self.enums = enums


    def main_menu_actions(self):
        MAIN_MENU_MAP = {
            self.enums.START_GAME: self.gameloop.play_game,
            # self.enums.GAME_INFO: ,
            # self.enums.SCORE_RECORD: ,
            # self.enums.QUIT_GAME: 
        }
        return MAIN_MENU_MAP

    # def check_map(self):
    #     MAP = {
    #         self.enums.WIN: "Congratulations! You win!",
    #         self.enums.DRAW: "It's a draw!"
    #     }
    #     return MAP