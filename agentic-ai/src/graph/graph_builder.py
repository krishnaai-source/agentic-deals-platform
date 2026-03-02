# graph/graph_builder.py
from langgraph.graph import StateGraph
from .state import DealState
from .nodes.sku_velocity_agent import sku_velocity_node
from .nodes.inventory_agent import inventory_node
from .nodes.pricing_agent import pricing_node
from .nodes.reflection_agent import reflection_node

def build_deal_graph():
    graph = StateGraph(DealState)
    graph.add_node("sku_velocity", sku_velocity_node)
    graph.add_node("inventory", inventory_node)
    graph.add_node("pricing", pricing_node)
    graph.add_node("reflection", reflection_node)

    graph.set_entry_point("sku_velocity")
    graph.add_edge("sku_velocity", "inventory")
    graph.add_edge("inventory", "pricing")
    graph.add_edge("pricing", "reflection")
    graph.set_finish_point("reflection")

    return graph.compile()
