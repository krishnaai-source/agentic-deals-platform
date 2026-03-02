# graph/nodes/reflection_agent.py
from ..llm.ollama_client import ollama_client

def reflection_node(state):
    state.reasoning_trace.append("Reflecting on candidate SKUs and applying VT/UT filters.")
    filtered = [
        sku for sku in state.candidate_skus
        if "VT_HIGH" in sku.get("velocity_tags", [])
    ]
    state.filtered_skus = filtered[:20]

    prompt = f"""
You are a retail deals expert.
Explain in 3–4 sentences why these SKUs are good deals for region {state.region}
and intent "{state.intent_query}". Focus on price, availability, and relevance.
"""
    summary = ollama_client.generate(prompt)
    state.reasoning_trace.append(summary)
    return state
