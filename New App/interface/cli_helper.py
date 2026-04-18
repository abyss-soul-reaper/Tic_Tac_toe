from pipeline.game_enum import GameEnum

def menu_map(menu):
    INDEX_MAP = {idx: action.value.replace('_', ' ').title() for idx, action in enumerate(menu, 1)}
    return INDEX_MAP
