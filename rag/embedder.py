import requests

class Embedder:
    def __init__(self, model="llama3.2", host="http://localhost:11434"):
        self.model = model
        self.host = host

    def embed(self, text: str) -> list[float]:
        response = requests.post(
            f"{self.host}/api/embeddings",
            json={
                "model":self.model,
                "prompt":text
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["embedding"]