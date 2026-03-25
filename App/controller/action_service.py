from App.core.base.menu_enum import get_menu_actions

class ActionFlow:
    def __init__(self, collection_helper, game_cli):
        self.collection_helper = collection_helper
        self.game_cli = game_cli

    def choose_action(self, menu_name):
        menu = get_menu_actions(menu_name)
        actions_map = self.collection_helper.index_mapping(menu)
        return self.game_cli.show_menu(actions_map, menu_name)