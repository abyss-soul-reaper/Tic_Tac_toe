class InputPipeline:
    def init__(self, registry):
        self.registry = registry

    def dsp_pipeline(self, info, schema):
        pass



    def clean_input(self, value):
        return value.strip() if isinstance(value, str) else value

    def dsp_valid(self, field, value):
        validators = self.registry.validators_handler()
        return validators.get(field, lambda _: False)(value)

    def dsp_normalize(self, field, value):
        normalizers = self.registry.normalizers_handler()
        return normalizers.get(field, lambda x: x)(value)