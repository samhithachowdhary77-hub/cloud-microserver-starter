from app.rag.ingest import build_vectorstore

if __name__ == "__main__":
    print("Building vectorstore...")
    build_vectorstore()
    print("Done.")