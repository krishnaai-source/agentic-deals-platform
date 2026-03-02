# llm/ollama_client.py
import requests
from ..config import OLLAMA_URL, OLLAMA_MODEL

class OllamaClient:
    def __init__(self, base_url=OLLAMA_URL, model=OLLAMA_MODEL):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str) -> str:
        resp = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt}
        )
        resp.raise_for_status()
        return resp.json().get("response", "")

ollama_client = OllamaClient()
