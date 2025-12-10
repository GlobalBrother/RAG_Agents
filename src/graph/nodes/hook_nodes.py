# src/graph/nodes/script_nodes.py
from typing import Dict, Any

from ..state import AdPipelineState
from agents.hook_agent import HookAgent

hook_agent = HookAgent()

def run(state: AdPipelineState) -> Dict[str, Any]:
    variables = state.get("client_data").get("hooks") or {}
    variables["ad_scripts"] = state.get("script_output")
    query = state.get(
        "hook_query",
        "Create 7 unique and intriguing hooks for the ads provided.",
    )
    result = hook_agent.invoke({"variables": variables, "query": query})
    report = result.get("research_report") if isinstance(result, dict) else str(result)
    return {"hook_output": report}
