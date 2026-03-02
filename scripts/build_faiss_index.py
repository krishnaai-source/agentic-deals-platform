import numpy as np
import faiss
from agentic_ai.src.db.mongo_client import skus_collection
from agentic_ai.src.embeddings.model import encode_query
from agentic_ai.src.config import FAISS_INDEX_PATH

if __name__ == "__main__":
    skus = list(skus_collection().find({}))
    vectors = []
    for sku in skus:
        # For demo, reuse query encoder on SKU name
        vec = encode_query(sku["name"])
        vectors.append(vec)
    vectors = np.stack(vectors).astype("float32")
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    faiss.write_index(index, FAISS_INDEX_PATH)
    print(f"FAISS index written to {FAISS_INDEX_PATH}")
