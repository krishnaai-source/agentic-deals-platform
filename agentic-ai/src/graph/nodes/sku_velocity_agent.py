# graph/nodes/sku_velocity_agent.py
from ..rag.retriever import sku_retriever
from ..embeddings.model import encode_query

def sku_velocity_node(state):
    state.reasoning_trace.append("Running SKU velocity analysis.")
    embedding = encode_query(state.intent_query)
    docs = sku_retriever.search_by_embedding(
        embedding,
        region=state.region,
        categories=state.preferred_categories
    )
    state.candidate_skus = docs
    return state
