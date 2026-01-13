class AgentRuntime:
    def __init__(self, llm, tool_registry):
        self.llm = llm
        self.tool_registry = tool_registry

    def run(self, context):
        prompt = f"""
        You are an AI agent.

        RULES:
        - If a calculation is required, respond EXACTLY as:
        TOOL:calculator:<expression>
        - Otherwise, respond with plain text.
        Context: {context.knowledge}
        Memory: {context.memory}
        Question: {context.query}
        """
        output = self.llm.generate(prompt)

        if output.startswith("TOOL:"):
            _, tool_name, tool_input=output.split(":",2)
            tool = self.tool_registry.get(tool_name)
            if not tool:
                return f"Tool {tool_name} not found"
            return tool.execute(tool_input)
        
        return output