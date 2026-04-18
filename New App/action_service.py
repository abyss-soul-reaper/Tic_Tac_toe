from menus import Menus

class ActionService:
    def __init__(self):
        self.current_menu = Menus.MAIN_MENU
        self.used_symbols = set()
        self.players = []
        self.board_size = 3

    def navigate_to(self, menu_name):
        self.current_menu = menu_name

    def set_board_size(self, size):
        self.board_size = size