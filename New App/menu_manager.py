from menus import Menus

class MenuManager:
    def __init__(self):
        self.current_menu = Menus.MAIN_MENU

    def navigate_to(self, menu_name):
        self.current_menu = menu_name