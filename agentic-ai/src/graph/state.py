# graph/state.py
from typing import List, Dict, Any
from pydantic import BaseModel

class DealState(BaseModel):
    request_id: str
    customer_id: str
    region: str
    intent_query: str
    velocity_type: str
    preferred_categories: List[str] = []
    candidate_skus: List[Dict[str, Any]] = []
    filtered_skus: List[Dict[str, Any]] = []
    reasoning_trace: List[str] = []
