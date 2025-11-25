from src.ingest import load_documents
from src.chunk import chunk_documents
from src.vectorstore import build_vectorstore
from src.rag import build_rag

def build_rag_database():
    docs = load_documents('C:/Work/LangChain/data')
    chunks = chunk_documents(docs)
    build_vectorstore(chunks)

def query_rag(question):
    rag_chain = build_rag()
    answer = rag_chain.invoke({"question": question})
    return answer

if __name__ == "__main__":
    # 1. Build database once
    build_rag_database()

    # 2. Query RAG
    print(query_rag("What is the main idea of Onion Socks?"))
