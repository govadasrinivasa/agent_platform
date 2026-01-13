# model/llm.py
import requests
import json

class LLMClient:
    def __init__(self, model="llama3.2", host="http://localhost:11434"):
        self.model = model
        self.host = host

    def generate(self, prompt: str) -> str:
        response = requests.post(
            f"{self.host}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()
        return response.json()["response"].strip()