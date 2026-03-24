class Board:
    def __init__(self, size=3):
        self.size = size
        self.board = [str(i) for i in range(1, self.size**2 + 1)]

    def display_board(self):
        for i in range(0, len(self.board), self.size):
            print("|".join(self.board[i: i+self.size]))
            if i < (len(self.board) - self.size):
                print("_" * (2 * self.size - 1))

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False
    
    def reset_board(self):
        self.board = [str(i) for i in range(1, self.size**2 + 1)]

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()