class Pipeline:
    def __init__(self, registry):
        self.registry = registry

    def input_pipeline(self, data):
        for field, value in data.items():
            if not self.validate_input(field, value):
                return False
            return self.normalize_input(field, value)

    def validate_input(self, field, value):
        validate_map = self.registry.validate_map()
        return validate_map.get(field, lambda _: False)(value)
    
    def normalize_input(self, field, value):
        normalize_map = self.registry.normalize_map()
        return normalize_map.get(field, lambda x: x)(value)