class AgentController:
    def __init__(self, workflow):
        self.workflow = workflow

    def run_agent(self, context):
        return self.workflow.execute(context)