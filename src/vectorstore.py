from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from .config import EMBED_MODEL, OPENAI_API_KEY

def build_vectorstore(chunks, persist_directory="vector_db"):
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    vectordb.persist()
    return vectordb
