from menus import Menus

class ActionService:
    def __init__(self):
        self.players = []
        self.board_size = 3
        self.players_count = 2
        self.used_symbols = set()
        self.current_menu = Menus.MAIN_MENU

    def navigate_to(self, menu_name):
        self.current_menu = menu_name

    def set_board_size(self, size):
        self.board_size = size