class Retriever:
    def __init__(self, store, embedder):
        self.store = store
        self.embedder = embedder

    def retrieve(self, query: str, k=3):
        query_embedding = self.embedder.embed(query)
        return self.store.search(query_embedding, k)