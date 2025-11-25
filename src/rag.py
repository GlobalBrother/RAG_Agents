from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from .retriever import load_retriever

def build_rag():
    retriever = load_retriever()

    template = """
    You are an expert assistant. Use ONLY the context below.
    If the answer is not found, say "The document does not include this information."

    Context:
    {context}

    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-4.1-mini")

    rag_chain = (
        {"context": retriever, "question": lambda x: x["question"]} 
        | prompt 
        | llm
    )

    return rag_chain
