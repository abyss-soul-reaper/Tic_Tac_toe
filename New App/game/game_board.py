class Board:
    def __init__(self, size=3):
        self.size = size
        self.board = [str(i) for i in range(1, self.size**2 + 1)]

    def update_board(self, cell_choice, symbol):
        if 1<= cell_choice <=self.size**2 and self.is_valid_move(cell_choice):
            self.board[cell_choice - 1] = symbol
            return True
        return False

    
    def reset_board(self):
        self.board = [str(i) for i in range(1, self.size**2 + 1)]

    def is_valid_move(self, cell_choice):
        return self.board[cell_choice - 1].isdigit()
    
  