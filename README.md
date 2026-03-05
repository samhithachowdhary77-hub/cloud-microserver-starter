# Agentic RAG DevOps Assistant

An AI-powered DevOps troubleshooting assistant that uses Retrieval-Augmented Generation (RAG) to answer operational questions using historical runbooks and incident tickets.

The system uses LangChain, FAISS, and OpenAI models to retrieve relevant DevOps knowledge and generate contextual responses for debugging and incident response.

---

## Tech Stack

Python
FastAPI
LangChain
FAISS
OpenAI API
Docker

---

## Features

* Retrieval-Augmented Generation (RAG) pipeline
* Vector search using FAISS
* DevOps troubleshooting assistant
* FastAPI REST interface
* Containerized deployment

---

## Architecture

User → FastAPI → RAG Pipeline → FAISS → OpenAI → Response

---

## Running the Project

### 1 Install dependencies

pip install -r requirements.txt

### 2 Build the vector index

python build_vectors.py

### 3 Start the API server

uvicorn main:app --reload

---

## API Endpoint

POST /ask

Request

{
"question": "Why is my Kubernetes pod crashing?"
}

Response

{
"answer": "Possible reasons include OOM errors, failing health checks..."
}
