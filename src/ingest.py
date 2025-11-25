from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

def load_documents(data_path="data"):
    documents = []
    for file in Path(data_path).glob("*.pdf"):
        loader = PyPDFLoader(str(file))
        docs = loader.load()
        documents.extend(docs)
    return documents
