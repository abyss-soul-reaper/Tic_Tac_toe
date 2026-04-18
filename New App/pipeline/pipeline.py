class Pipeline:
    def __init__(self, registry):
        self.registry = registry

    def input_pipeline(self, data):
        result = {"correct_data": {}, "errors": {}}
        data = data if isinstance(data, list) else [data]
        for item in data:
            for field, value in item.items():
                if not self.validate_input(field, value):
                    result["errors"][field] = f"Invalid value for {field} - {value}."
                else:
                    result["correct_data"][field] = self.normalize_input(field, value)
        return result


    def validate_input(self, field, value):
        validate_map = self.registry.validate_map()
        return validate_map.get(field, lambda _: False)(value)
    
    def normalize_input(self, field, value):
        normalize_map = self.registry.normalize_map()
        return normalize_map.get(field, lambda x: x)(value)