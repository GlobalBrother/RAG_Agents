from langchain_community.vectorstores import Chroma

def load_retriever(persist_directory="vector_db"):
    vectordb = Chroma(persist_directory=persist_directory)
    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    return retriever
