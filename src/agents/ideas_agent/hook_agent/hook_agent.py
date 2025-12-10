from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI

from .hook_agent_prompt import hook_agent_prompt

import json
from dotenv import load_dotenv
load_dotenv()

class HookAgent(Runnable):
    """
    Research Agent implemented as a LangChain Runnable.
    Compatible with LangGraph as a graph node.
    """

    def __init__(self, model: str = "gpt-5.1"):
        self.llm = ChatOpenAI(model=model, temperature=0.8)

        # LangChain chain: prompt -> llm
        self.chain = hook_agent_prompt | self.llm

    def invoke(self, state:dict):
        """
        LangGraph calls this directly.
        Input `state` must contain:
           state["query"]
           state["variables"]
        """
        variables = state["variables"]
        query = state["query"]

        # Merge into final template input
        final_vars = {**variables, "query": query}

        # Run chain
        result = self.chain.invoke(final_vars)

        # LangGraph expects a dict mapping to state keys
        return {"research_report": result.content}

# ---------------------------------------------------------
# Optional: Quick test
# ---------------------------------------------------------

if __name__ == "__main__":
    agent = HookAgent()

    with open("./src/datasets/products/FHA/JSON/forgotten_home_apothecary.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        variables = data.get("script")

    state = {
        "variables": variables,
        "query": "Analyze this brand's strategic opportunities."
    }
    print(agent.invoke(state))
