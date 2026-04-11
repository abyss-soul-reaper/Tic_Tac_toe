from game.board import Board
from players.player import Player

class GameState:
    def __init__(self):
        self.board = Board()
        self.players = [Player(), Player()]
        self.curt_pl_idx = 0
        self.curt_pl = None