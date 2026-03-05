# Agentic RAG DevOps Assistant


An AI-powered DevOps troubleshooting assistant that uses Retrieval-Augmented Generation (RAG) to answer operational questions using historical runbooks and incident tickets.

The system uses LangChain, FAISS, and OpenAI models to retrieve relevant DevOps knowledge and generate contextual responses for debugging and incident response.
=======
An AI-powered DevOps troubleshooting assistant that uses **Retrieval-Augmented Generation (RAG)** to answer operational questions using historical runbooks and incident tickets.

The system retrieves relevant DevOps knowledge using **LangChain + FAISS** and generates contextual responses using **OpenAI models**.
>>>>>>> 748d9d4 (Update README and architecture documentation)

---

## Tech Stack


Python
FastAPI
LangChain
FAISS
OpenAI API
Docker
=======
* Python
* FastAPI
* LangChain
* FAISS
* OpenAI API
* Docker
>>>>>>> 748d9d4 (Update README and architecture documentation)

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


=======
More details in:

`architecture/system-design.md`

---

## Project Structure

```
agentic-rag-devops-assistant
│
├── app/                # Application modules
├── data/               # Runbooks and DevOps knowledge base
├── faiss_index/        # Generated FAISS vector index
├── architecture/       # System architecture documentation
├── docker/             # Docker configuration
├── scripts/            # Utility scripts
├── tests/              # Test cases
│
├── build_vectors.py    # Builds FAISS vector database
├── main.py             # FastAPI entry point
├── requirements.txt
├── Dockerfile
└── README.md
```

748d9d4 (Update README and architecture documentation)
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
=======
### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Set environment variables

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key_here
```

### 3. Build the vector index

```
python build_vectors.py
```

### 4. Start the API server

```
uvicorn main:app --reload
```

---

## API Endpoints

### POST `/ask`

Ask a DevOps troubleshooting question.

Request

```
{
  "question": "Why is my Kubernetes pod crashing?"
}
```

Response

```
{
  "answer": "Possible reasons include OOM errors, failing health checks..."
}
```

---

## Future Improvements

* Kubernetes deployment
* Observability with Prometheus + Grafana
* Prompt evaluation tests
* Multi-agent troubleshooting workflow
748d9d4 (Update README and architecture documentation)
