from menus import Menus

class ActionService:
    def __init__(self):
        self.players = []
        self.board_size = 3
        self.back_menu = None
        self.players_count = 2
        self.used_symbols = set()
        self.current_menu = Menus.MAIN_MENU

    def navigate_to(self, menu_name):
        self.back_menu = self.current_menu
        self.current_menu = menu_name

    def navigate_back(self, menu_name=None):
        if menu_name:
            self.current_menu = menu_name

        elif self.back_menu:
            self.current_menu = self.back_menu
            self.back_menu = None

    def set_board_size(self, size):
        self.board_size = size

    def reset(self):
        self.players = []
        self.board_size = 3
        self.back_menu = None
        self.players_count = 2
        self.used_symbols = set()
        self.current_menu = Menus.MAIN_MENU

    def quit_game(self):
        exit()