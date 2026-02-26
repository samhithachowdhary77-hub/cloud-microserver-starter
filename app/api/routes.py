from fastapi import APIRouter
from app.agent.assistant import ask_agent

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.get("/ask")
def ask(question: str):
    answer = ask_agent(question)
    return {"answer": answer}