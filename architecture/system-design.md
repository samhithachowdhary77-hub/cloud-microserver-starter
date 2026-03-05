
# System Architecture

The Agentic RAG DevOps Assistant follows a Retrieval-Augmented Generation (RAG) architecture to answer operational troubleshooting questions.

## Workflow

User Query
↓
FastAPI Service
↓
LangChain RAG Pipeline
↓
FAISS Vector Store
↓
DevOps Runbooks / Incident Tickets
↓
OpenAI LLM
↓
Generated Response

## Components

**FastAPI API**

Handles incoming user requests and exposes the `/ask` endpoint.

**LangChain Retrieval Pipeline**

Processes the query and retrieves relevant context from the vector database.

**FAISS Vector Store**

Stores embeddings created from DevOps runbooks and incident documentation.

**Knowledge Base**

Contains DevOps troubleshooting documents such as:

* Kubernetes restart troubleshooting
* Redis latency debugging
* Infrastructure incident runbooks

**OpenAI LLM**

Generates the final answer using retrieved context.
=======
# Agentic RAG DevOps Assistant Architecture

User Query
   ↓
FastAPI Service (main.py)
   ↓
RAG Pipeline
   ↓
LangChain Retrieval
   ↓
FAISS Vector Index
   ↓
DevOps Runbooks / Tickets Dataset
   ↓
OpenAI LLM
   ↓
Response returned to user

Components

FastAPI
Provides REST endpoints for interacting with the assistant.

LangChain
Handles the retrieval augmented generation pipeline.

FAISS
Stores vector embeddings of DevOps runbooks and tickets.

Embedding Pipeline
build_vectors.py processes runbooks and creates embeddings stored in FAISS.

OpenAI LLM
Generates final answers using retrieved context.
748d9d4 (Update README and architecture documentation)
