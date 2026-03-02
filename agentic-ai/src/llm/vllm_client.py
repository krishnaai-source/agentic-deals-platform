# llm/vllm_client.py
import requests
from ..config import VLLM_URL, VLLM_MODEL

class VllmClient:
    def __init__(self, url=VLLM_URL, model=VLLM_MODEL):
        self.url = url
        self.model = model

    def chat(self, messages):
        payload = {"model": self.model, "messages": messages}
        resp = requests.post(self.url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]

vllm_client = VllmClient()
