from fastapi import APIRouter
from app.config import API_KEY
from app.service import PolicyRetrieval

router = APIRouter()
policy_retrieval = PolicyRetrieval()


@router.post("/ask-agent")
async def ask_agent(question: str):
    """Answers a question, using the real agent or CSV retrieval depending on setup."""
    return policy_retrieval.answer(question)


@router.get("/status")
async def status():
    """Reports which mode the assistant is running in."""
    return {"mode": "Real Agent" if API_KEY else "Offline CSV Retrieval"}