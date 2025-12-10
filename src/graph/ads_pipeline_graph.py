# src/graph/ads_pipeline_graph.py

from pathlib import Path
import json

from langgraph.graph import StateGraph, END
from graph.state import AdPipelineState

from .nodes import audience_node
from .nodes import ideas_node
from .nodes import script_node
from .nodes import hook_node

# -----------------------------------------------------------
# 1. Load Client Data From JSON
# -----------------------------------------------------------
def load_client_data(client_name: str) -> dict:
    base = Path(__file__).resolve().parents[2] / "datasets" / "products" / "FHA" / "JSON"
    with open(base / f"{client_name}.json", "r", encoding="utf-8") as f:
        return json.load(f)


# -----------------------------------------------------------
# 2. Node Definitions (Stub Implementations)
# -----------------------------------------------------------
def load_client_node(state: AdPipelineState) -> AdPipelineState:
    client_name = state.get("client_name", "forgotten_home_apothecary")
    client = load_client_data(client_name)
    return {"client_data": client}

# -----------------------------------------------------------
# Build the LangGraph Pipeline
# -----------------------------------------------------------
def build_graph():
    graph = StateGraph(AdPipelineState)

    graph.add_node("load_client", load_client_node)
    graph.add_node("angles", audience_node)
    graph.add_node("ideas", ideas_node)
    graph.add_node("script", script_node)
    graph.add_node("hook", hook_node)

    graph.set_entry_point("load_client")
    graph.add_edge("load_client", "angles")
    graph.add_edge("angles", "ideas")
    graph.add_edge("ideas", "script")
    graph.add_edge("script", END)

    return graph.compile()


# -----------------------------------------------------------
# Optional: Quick Runner
# -----------------------------------------------------------
if __name__ == "__main__":
    graph = build_graph()
    result = graph.invoke({})
