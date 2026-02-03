class ContextRequest:
    def __init__(self, agent_id: str, query: str):
        self.agent_id = agent_id
        self.query = query

    # class ContextResponse:
    #     def __init__(self, documents, memory, metadata:None):
    #         self.documents = documents
    #         self.memory = memory
    #         self.metadata = metadata or {}

class ContextResponse:
    def __init__(self, sections: dict):
        self.sections = sections