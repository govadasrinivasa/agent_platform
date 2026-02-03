class ContextProvider:
    def __init__(self, rag_retriever, memory_manager, azure_migrate_provider):
        self.rag = rag_retriever
        self.memory = memory_manager
        self.azure = azure_migrate_provider

    def provide(self, query: str):
        return {
            "rag_knowledge": self.rag.retrieve(query),
            "memory": self.memory.recall(),
            "azure_migrate":self.azure.provide_context()
        }