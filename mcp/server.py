from mcp.schema import ContextRequest, ContextResponse

class MCPServer:
    def __init__(self, context_provider):
        self.context_provider = context_provider

    def get_context(self, reqeust: ContextRequest) -> ContextResponse:
        sections = self.context_provider.provide(reqeust.query)
        return ContextResponse(sections)