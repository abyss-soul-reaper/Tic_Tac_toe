from App.core.result.base_result import BaseResult

class PlayerResult(BaseResult):
    def __init__(self):
        super().__init__()
        self.payload = {
            "name": None,
            "symbol": None,
            "board_size": None
        }

