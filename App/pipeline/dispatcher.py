from App.pipeline.dispatcher_result import DispatcherResult


class Dispatcher:
    def __init__(self, registry, pipeline, action_config):
        self.pipeline = pipeline
        self.registry = registry
        self.action_config = action_config

    # ---- Input Handling Method ----
    def execute_input(self, config, action):
        res = DispatcherResult("INPUT_EXECUTION", action)

        if not config:
            return res.fail("No configuration for input")
        
        handler = self.registry.input_actions_map()
        if action not in handler:
            return res.fail("No input handler for action")
        
        try:
            res.payload["input"] = handler[action]()
            return res.success()
        except Exception as e:
            return res.fail(str(e))
        
    # ---- System Data Methods ----
    def execute_system(self, config, action, data=None):
        res = DispatcherResult("SYSTEM_DATA", action)

        if not config:
            return res.fail("No configuration for system action")
        
        handler = self.registry.system_data_actions_map()
        if action not in handler:
            return res.fail("No system handler for action")
        
        try:
            res.payload["system"] = (handler[action](data) if data else handler[action]())
            return res.success()
        except Exception as e:
            return res.fail(str(e))

    # # ---- Pipeline Methods ----
    # def execute_pipeline(self, data, config, action):
    #     res = DispatcherResult("PIPELINE_EXECUTION", action)

    #     pipe = self.pipeline.input_pipeline(data)
    #     if not pipe:
    #         return res.fail("Pipeline execution failed")
    #     res.payload["pipeline"] = pipe
    #     return res.success()

    # ---- Action Execution Method ----
    def execute(self, action):
        res = DispatcherResult("FINAL_EXECUTION", action)
        enum_action, config = self.action_config.resolve(action)

        if not config:
            return res.fail("Action configuration not found")
        
        current_data = None

        # INPUT
        if config.get("requires_input"):
            input_res = self.execute_input(config, enum_action)
            if not input_res.ok:
                return input_res
            current_data = input_res.payload["input"]

        # # PIPELINE
        # if config.get("requires_pipeline"):
        #     pipeline_res = self.execute_pipeline(current_data, config, enum_action)
        #     if not pipeline_res.ok:
        #         return pipeline_res
        #     current_data = pipeline_res.payload["pipeline"]

        # SYSTEM
        if config.get("requires_system_data"):
            system_res = self.execute_system(config, enum_action, current_data)
            if not system_res.ok:
                return system_res
            current_data = system_res.payload["system"]


        


