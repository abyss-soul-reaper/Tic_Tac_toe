from App.core.state.user_state import UserState

class Context:
    def __init__(self):
        self.users_state = UserState.GUESTS
        self.symbols_state = None
        self.board_state = None
        self.game_state = None

    def reset(self):
        self.users_state = None
        self.symbols_state = None
        self.board_state = None
        self.game_state = None
        