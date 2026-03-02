# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from .graph.graph_builder import build_deal_graph
from .graph.state import DealState

app = FastAPI(title="Agentic Deals AI")
graph = build_deal_graph()

class DealRequest(BaseModel):
    customerId: str
    region: str
    intentQuery: str
    velocityType: str
    preferredCategories: list[str] = []

class DealItem(BaseModel):
    skuId: str
    name: str
    price: float
    storeId: str
    score: float

class DealResponse(BaseModel):
    requestId: str
    deals: list[DealItem]
    reasoningSummary: str

@app.post("/agentic/deals", response_model=DealResponse)
def get_deals(req: DealRequest):
    state = DealState(
        request_id=str(uuid.uuid4()),
        customer_id=req.customerId,
        region=req.region,
        intent_query=req.intentQuery,
        velocity_type=req.velocityType,
        preferred_categories=req.preferredCategories,
    )
    final_state = graph.invoke(state)

    deals = []
    for sku in final_state.filtered_skus:
        deals.append(DealItem(
            skuId=sku["_id"],
            name=sku["name"],
            price=sku.get("current_price", 0.0),
            storeId=sku.get("store_id", "UNKNOWN"),
            score=sku.get("score", 0.0)
        ))

    reasoning_summary = final_state.reasoning_trace[-1] if final_state.reasoning_trace else ""
    return DealResponse(
        requestId=final_state.request_id,
        deals=deals,
        reasoningSummary=reasoning_summary
    )
