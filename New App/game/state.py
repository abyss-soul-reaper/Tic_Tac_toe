class GameState:
    def __init__(self, players, board):
        self.board = board
        self.players = players
        self.current_idx = 0

    @property
    def current_player(self):
        return self.players[self.current_idx]

    def switch_player(self):
        self.current_idx = 1 - self.current_idx