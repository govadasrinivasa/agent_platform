from mcp.schema import ContextRequest

class AgentRuntime:
    def __init__(self, llm, mcp_server):
        self.llm = llm
        self.mcp = mcp_server

    def run(self, agent_id: str, query: str):
        context = self.mcp.get_context(
            ContextRequest(agent_id, query)
        )

        prompt = f"""
You are a cloud migration expert.

Azure Migrate Discovery:
{context.sections['azure_migrate']}

Historical Knowledge:
{context.sections['rag_knowledge']}

Conversation Memory:
{context.sections['memory']}

User Question:
{query}

Provide migration guidance.
"""

        return self.llm.generate(prompt)
