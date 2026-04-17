from menus import Menus

class ActionService:
    def __init__(self):
        self.current_menu = Menus.MAIN_MENU
        self.current_player_data = []
        self.players = []

    def navigate_to(self, menu_name):
        self.current_menu = menu_name