import re

NAME_PATTERN = re.compile(r"[A-Za-z]+(?:\s[A-Za-z]+)*")
SYMBO_PATTERN = re.compile(r"(X|O)")

def validate_name(name):
    return bool(NAME_PATTERN.fullmatch(name.strip()))

def validate_symbol(symbol):
    return bool(SYMBO_PATTERN.fullmatch(symbol.strip().upper()))

def check_unique_symbols(used_symbols, symbol):
    return symbol not in used_symbols


def validate_players_count(count, current_count):
    try:
        count_int = int(count)
        return 2 <= count_int <= 4 and count_int != current_count
    except ValueError:
        return False    


def validate_board_size(new_size, current_size):
    try:
        size_int = int(new_size)
        return 3 <= size_int <= 10 and size_int != current_size
    except ValueError:
        return False
    
# def validate_cell_choice(cell_choice):

