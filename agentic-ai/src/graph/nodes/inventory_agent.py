# graph/nodes/inventory_agent.py
from ..db.mongo_client import inventory_collection

def inventory_node(state):
    state.reasoning_trace.append("Enriching SKUs with inventory data.")
    inv_col = inventory_collection()
    enriched = []
    for sku in state.candidate_skus:
        inv = inv_col.find_one({"sku_id": sku["_id"], "region": state.region})
        if inv:
            sku["stock_on_hand"] = inv.get("stock_on_hand", 0)
            sku["velocity_tags"] = inv.get("velocity_tags", [])
            enriched.append(sku)
    state.candidate_skus = enriched
    return state
