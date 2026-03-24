VALID_SYMBOLS = {'X', 'O'}

def is_non_empty(value: str) -> bool:
    return bool(value and value.strip())

def is_valid_symbol(value: str) -> bool:
    return value in VALID_SYMBOLS

def is_valid_size(value: str) -> bool:
    try:
        size = int(value)
        return size >= 3
    except ValueError:
        return False

def is_any(value: str) -> bool:
    return True
