from App.core.initializer.initializer import Initializer

class GameLoop:
    def __init__(self):
        init = Initializer()

        self.action_flow = init.action_flow

    def choose_action(self, menu_name):
        return self.action_flow.choose_action(menu_name)