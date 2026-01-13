import math

class VectorStore:
    def __init__(self):
        self.vectors = []

    def add(self, embedding:list[float], content: str):
        self.vectors.append({
        "embedding":embedding,
        "content":content
        })

    def cosine_similarity(self, v1, v2):
        dot = sum(a * b for a, b in zip(v1,v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        return dot / (mag1 * mag2 + 1e-9)
    
    def search(self, query_embedding:list[float], k=3):
        scored =[
            (self.cosine_similarity(query_embedding, item["embedding"]), item["content"])
            for item in self.vectors
        ]
        scored.sort(reverse=True,key=lambda x: x[0])
        return [content for _, content in scored[:k]]