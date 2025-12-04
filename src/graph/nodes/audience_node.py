# src/graph/nodes/audience_node.py
from typing import Dict, Any

from ..state import AdPipelineState
from agents.audience_agent import AnglesAgent

audience_agent = AnglesAgent()

def run(state: AdPipelineState) -> Dict[str, Any]:
    variables = state.get("client_data").get("angles") or {}
    query = state.get("angles_query", "Identify 10 precise target audiences with reasons.")
    result = audience_agent.invoke({"variables": variables, "query": query})
    report = result.get("research_report") if isinstance(result, dict) else str(result)
    return {"audience_output": report}
