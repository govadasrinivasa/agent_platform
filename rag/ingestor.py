# rag/ingestor.py
class DocumentIngestor:
    def __init__(self, store, embedder):
        self.store = store
        self.embedder = embedder

    def ingest(self, documents: list[str]):
        for doc in documents:
            embedding = self.embedder.embed(doc)
            self.store.add(embedding, doc)