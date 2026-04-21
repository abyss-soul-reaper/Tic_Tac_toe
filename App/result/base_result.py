class BaseResult:
    def __init__(self):
        self.ok = False
        self.payload = None
        self.error = None
        self.meta = None

    def fail(self, error_message):
        self.ok = False
        self.error = error_message
        return self
    
    def success(self):
        self.ok = True
        return self