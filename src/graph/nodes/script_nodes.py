# src/graph/nodes/script_nodes.py
from typing import Dict, Any

from ..state import AdPipelineState
from agents.script_agent import ScriptAgent

scripts_agent = ScriptAgent()

def run(state: AdPipelineState) -> Dict[str, Any]:
    variables = state.get("client_data").get("scripts") or {}
    variables["audiences"] = state.get("audience_output")
    variables["ideas"] = state.get("idea_output")
    query = state.get(
        "script_query",
        "Analyze the 10 target audiences as well as the 10 ad concepts and see which concept matches which audience the best. Create a script for each possible pair",
    )
    result = scripts_agent.invoke({"variables": variables, "query": query})
    report = result.get("research_report") if isinstance(result, dict) else str(result)
    return {"script_output": report}
