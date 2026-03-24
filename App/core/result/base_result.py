class BaseResult:
    def __init__(self):
        self.ok = False
        self.payload = None
        self.error = None
        self.meta = {"error_type": None}

    def fail(self, error):
        self.ok = False
        self.error = error
        return self
    
    def success(self):
        self.ok = True
        return self
    
    def validatoin_error(self, error):
        self.ok = False
        self.error = error
        self.meta = {"error_type": "ValidationError"}
        return self
