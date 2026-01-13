class WorkflowEngine:
    def __init__(self, executor):
        self.executor = executor

    def execute(self, context):
        return self.executor.execute(context)