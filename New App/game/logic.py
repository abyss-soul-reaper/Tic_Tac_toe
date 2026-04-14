def check(board, enums):
    if check_win(board.board):
        return enums.WIN
    elif check_draw(board.board):
        return enums.DRAW
    return enums.CONTINUE

def check_win(board):
    win_combainations = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals  
    ]

    for combo in win_combainations:
        if (board[combo[0]] == 
            board[combo[1]] == 
            board[combo[2]]):
            return True
    return False

def check_draw(board):
    return all(not cell.isdigit() for cell in board)