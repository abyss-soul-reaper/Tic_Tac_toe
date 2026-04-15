from result.base_result import BaseResult

class Dispatcher:
    def __init__(self, registry, pipeline, action_config):
        self.pipeline = pipeline
        self.registry = registry
        self.action_config = action_config

    # ---- Input Handling Method ----
    def execute_input(self, config, action):
        res = BaseResult()
        
        try:
            pass
        except Exception as e:
            return res.fail(str(e))

    # ---- Pipeline Methods ----
    def execute_pipeline(self, action, data):
        res = BaseResult()

        if self.pipeline.validate_input(action, data):
            return self.pipeline.normalize_input(action, data)
        else:
            return res.fail(f"Invalid input for {action}")
        
    # ---- Action Execution Method ----
    def execute(self, action):
        res = BaseResult()
        enum_action, config = self.action_config.resolve(action)

        if not config:
            return res.fail("Action configuration not found")
        
        current_data = None

        # INPUT
        if config.get("requires_input"):
            input_res = self.execute_input(config, enum_action)
            if not input_res.ok:
                return input_res
            current_data = input_res.payload

        # PIPELINE
        if config.get("requires_pipeline"):
            pipeline_res = self.execute_pipeline(enum_action, current_data)
            if not pipeline_res.ok:
                return pipeline_res
            current_data = pipeline_res.payload
            
            


        # handler = self.registry.main_menu_actions.get(enum_action)
        # if not handler:
        #     return res.fail("Invalid action")
        

        # try:
        #     handler()
        #     return res.success()
        # except Exception as e:
        #     return res.fail(str(e))
        


