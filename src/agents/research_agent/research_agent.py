from langchain_core.runnables import Runnable

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


from research_agent_prompt import research_agent_prompt, research_agent_news_prompt

from dotenv import load_dotenv
load_dotenv()

class ResearchAgent(Runnable):
    """
    Research Agent implemented as a LangChain Runnable.
    Compatible with LangGraph as a graph node.
    """

    def __init__(self, model: str = "gpt-5.1"):

        self.llm = ChatGoogleGenerativeAI(model='gemini-3-pro-preview', temperature=0.8)
        # self.llm = ChatOpenAI(model=model, temperature=0.8)

        # LangChain chain: prompt -> llm
        self.chain = research_agent_news_prompt | self.llm

    def invoke(self, state:dict):
        """
        LangGraph calls this directly.
        Input `state` must contain:
           state["query"]
        """
        query = state["query"]

        # Merge into final template input
        final_vars = {"query": query}

        # Run chain
        result = self.chain.invoke(final_vars)

        # LangGraph expects a dict mapping to state keys
        return {"research_report": result.content}

# ---------------------------------------------------------
# Optional: Quick test
# ---------------------------------------------------------

if __name__ == "__main__":
    agent = ResearchAgent()

    state = {
        "query": "Create an ad similar to the one provided."
    }
    agent.invoke(state)
