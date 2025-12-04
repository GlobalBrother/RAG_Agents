# src/graph/state/state_schema.py

from typing import TypedDict, Optional, Dict, Any


class AdPipelineState(TypedDict, total=False):
    """
    Shared state structure for the entire LangGraph ads pipeline.
    Every node reads/writes from this structure.
    """
    # Core client data
    client_data: Dict[str, Any]

    # Ideation & creativity
    ideas_output: Optional[str]
    audience_output: Optional[str]

    # Final structured output
    final_output: Optional[Dict[str, Any]]
