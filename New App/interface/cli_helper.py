from pipeline.game_enum import GameEnum

# def update_cell(board, symbol, cell_choice):
#     if 1<= cell_choice <=board.size**2 and board.update_board(cell_choice, symbol):
#         return True

def menu_map(menu):
    INDEX_MAP = {}
    for idx, action in enumerate(menu, 1):
        INDEX_MAP[idx] = action.value
    return INDEX_MAP


def resolver(action):
    if isinstance(action, GameEnum):
        enum_action = action
    elif isinstance(action, str):
        try:
                enum_action = GameEnum[action.replace(' ', '_').upper()]
        except KeyError:
            raise ValueError(f"Unknown feature: {action}")
    else:
        raise TypeError("Invalid feature type")

    return enum_action


    