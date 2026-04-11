from game.board import Board

class GameState:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.curt_player = 0