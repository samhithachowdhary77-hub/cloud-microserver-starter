from dotenv import load_dotenv
load_dotenv()

import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
import os

DATA_PATH = "data/runbooks"

def build_vectorstore():
    docs = []

    for file in os.listdir(DATA_PATH):
        loader = TextLoader(os.path.join(DATA_PATH, file))
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local("faiss_index")