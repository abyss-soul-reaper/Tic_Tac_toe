from result.base_result import BaseResult

class Dispatcher:
    def __init__(self, registry):
        self.registry = registry

    def execute(self, action):
        res = BaseResult()
        handler = self.registry.main_menu_actions.get(action)

        if not handler:
            return res.fail("Invalid action")
        
        try:
            handler()
            return res.success()
        except Exception as e:
            return res.fail(str(e))
        


