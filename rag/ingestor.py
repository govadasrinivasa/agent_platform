class DocumentIngestor:
    def __init__(self, store, embedder):
        self.store = store
        self.embedder = embedder

    def ingest(self, docs: list[str]):
        for doc in docs:
            embedding = self.embedder.embed(doc)
            self.store.add(embedding, doc)