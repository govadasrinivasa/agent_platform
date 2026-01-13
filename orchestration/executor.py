class AgentExecutor:
    def __init__(self, runtime):
        self.runtime = runtime

    def execute(self, context):
        return self.runtime.run(context)