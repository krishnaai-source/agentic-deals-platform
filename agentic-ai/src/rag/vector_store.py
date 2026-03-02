# rag/vector_store.py
import faiss
import numpy as np
from ..config import FAISS_INDEX_PATH

class FaissVectorStore:
    def __init__(self, index_path: str):
        self.index = faiss.read_index(index_path)

    def search(self, embedding, k=50):
        D, I = self.index.search(
            np.array([embedding]).astype("float32"),
            k
        )
        return I[0], D[0]

vector_store = FaissVectorStore(FAISS_INDEX_PATH)
