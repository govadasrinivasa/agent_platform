class MCPManager:
    def __init__(self, mcps: dict):
        self.mcps = mcps

    def resolve_tools(self, mcp_id: str):
        return self.mcps[mcp_id].tools