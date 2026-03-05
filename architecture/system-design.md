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
