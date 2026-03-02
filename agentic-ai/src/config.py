import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
MONGO_DB = os.getenv("MONGO_DB", "dealsdb")

FAISS_INDEX_PATH = "data/embeddings/sku_embeddings.faiss"

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

VLLM_URL = os.getenv("VLLM_URL", "http://vllm:8001/v1/chat/completions")
VLLM_MODEL = os.getenv("VLLM_MODEL", "meta-llama/Meta-Llama-3-8B")
