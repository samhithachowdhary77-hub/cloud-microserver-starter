from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

VECTOR_PATH = "vectorstore"

def get_retriever():

    embeddings = OpenAIEmbeddings()

    db = FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever()