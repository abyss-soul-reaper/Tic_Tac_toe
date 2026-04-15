import re

NAME_PATTERN = re.compile(r"[A-Za-z]+(?:\s[A-Za-z]+)*")
SYMBO_PATTERN = re.compile(r"(X|O)")

def validate_name(name):
    return bool(NAME_PATTERN.fullmatch(name.strip()))

def validate_symbol(symbol):
    return bool(SYMBO_PATTERN.fullmatch(symbol.strip().upper()))

def validate_board_size(size):
    try:
        size_int = int(size)
        return 3 <= size_int <= 10
    except ValueError:
        return False
    
# def validate_cell_choice(cell_choice):

