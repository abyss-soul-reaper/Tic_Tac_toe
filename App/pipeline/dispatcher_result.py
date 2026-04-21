from App.result.base_result import BaseResult

class DispatcherResult(BaseResult):
    def __init__(self, stage, action):
        super().__init__()
        self.stage = stage
        self.action = action
        self.payload = {
            "input": None,
            "pipeline": None,
            "system": None,
            "result": None
        }

    def fail(self, error):
        self.ok = False
        self.error = (error)
        return self
