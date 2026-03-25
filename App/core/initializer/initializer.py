from App.ui.game.game_cli import GameCli
from App.core.helpers import collection_helpers
from App.controller.action_service import ActionFlow

class Initializer:
    def __init__(self):
        self.game_cli = GameCli()
        self.collection_helpers = collection_helpers
        self.action_flow = ActionFlow(self.collection_helpers, self.game_cli)
