from App.core.validation.validators import *

class Registry:
    def validation():
        VALIDATION_MAP = {
            "name": is_non_empty,
            "symbol": is_valid_symbol,
            "board_size": is_valid_size
        }
        return VALIDATION_MAP
    
    def normalization():
        NORMALIZATION_MAP = {
            "name":lambda v: v.strip().title(),
            "symbol":lambda v: v.strip().upper(),
            "board_size":lambda v: int(v)
        }
        return NORMALIZATION_MAP




