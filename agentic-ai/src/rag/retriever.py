# rag/retriever.py
from .vector_store import vector_store
from ..db.mongo_client import skus_collection

class SkuRetriever:
    def search_by_embedding(self, embedding, region, categories):
        ids, scores = vector_store.search(embedding, k=50)
        sku_ids = [f"SKU-{i}" for i in ids]  # demo mapping
        query = {"_id": {"$in": sku_ids}}
        if categories:
            query["category"] = {"$in": categories}
        docs = list(skus_collection().find(query))
        for d, s in zip(docs, scores):
            d["score"] = float(s)
        return docs

sku_retriever = SkuRetriever()
