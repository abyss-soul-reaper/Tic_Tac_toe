import re

NAME_PATTERN = re.compile(r"[A-Za-z]+(?:\s[A-Za-z]+)*")
SYMBO_PATTERN = re.compile(r"(X|O)")

def validate_name(name):
    return bool(NAME_PATTERN.fullmatch(name.strip()))

def validate_symbol(symbol):
    return bool(SYMBO_PATTERN.fullmatch(symbol.strip().upper()))


# def validate_players (players):
#     if not isinstance(players, list):
#         raise ValueError("Players should be provided as a list.")

#     if len(players) < 2:
#         raise ValueError("At least two players are required.")

# def validate_board(board):
#     if not isinstance(board, Board):
#         raise ValueError("Invalid board object.")
    
#     if not isinstance(board.size, int) or board.size <= 3:
#         raise ValueError("Board size must be an integer greater than 3.")
    
#     if not isinstance(board.board, list) or len(board.board) != board.size**2:
#         raise ValueError("Board state is invalid.")