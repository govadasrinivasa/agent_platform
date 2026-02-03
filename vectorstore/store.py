import json
import math
from vectorstore.mysql_connection import get_connection

class VectorStore:

    def add(self, embedding: list[float], content: str):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO document_vectors (content, embedding) VALUES (%s, %s)",
            (content, json.dumps(embedding))
        )

        conn.commit()
        cursor.close()
        conn.close()

    def _cosine_similarity(self, v1, v2):
        dot = sum(a*b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a*a for a in v1))
        mag2 = math.sqrt(sum(b*b for b in v2))
        return dot / (mag1 * mag2 + 1e-9)

    def search(self, query_embedding: list[float], k=3):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT content, embedding FROM document_vectors")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        scored = []
        for row in rows:
            stored_embedding = json.loads(row["embedding"])
            score = self._cosine_similarity(query_embedding, stored_embedding)
            scored.append((score, row["content"]))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [content for _, content in scored[:k]]
