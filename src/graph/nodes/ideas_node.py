# src/graph/nodes/ideas_node.py
from typing import Dict, Any

from ..state import AdPipelineState
from agents.ideas_agent import IdeaAgent

ideas_agent = IdeaAgent()

def run(state: AdPipelineState) -> Dict[str, Any]:
    variables = state.get("client_data").get("ideas") or {}
    query = state.get("ideas_query", "Propose 10 new ad concepts tailored to the audiences.")
    result = ideas_agent.invoke({"variables": variables, "query": query})
    report = result.get("research_report") if isinstance(result, dict) else str(result)
    return {"idea_output": report}
