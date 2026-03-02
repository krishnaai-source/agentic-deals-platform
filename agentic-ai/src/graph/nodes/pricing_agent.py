# graph/nodes/pricing_agent.py
from ..db.mongo_client import pricing_collection

def pricing_node(state):
    state.reasoning_trace.append("Enriching SKUs with pricing data.")
    price_col = pricing_collection()
    for sku in state.candidate_skus:
        price = price_col.find_one({"sku_id": sku["_id"]})
        if price:
            sku["current_price"] = price.get("current_price", price.get("base_price", 0.0))
    return state
