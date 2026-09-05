from fastapi import APIRouter
from app.config import API_KEY
from app.service import PolicyRetrieval
from app.schema import Mode, Status, AskAgentResponse

router = APIRouter()


@router.post("/ask-agent")
async def ask_agent(question: str):
    """Answers a question, using the real agent or CSV retrieval depending on setup."""
    policy_retrieval = PolicyRetrieval()
    return AskAgentResponse(response=policy_retrieval.answer(question))


@router.get("/status")
async def status():
    """Reports which mode the assistant is running in."""
    return Status(mode=Mode.AI_AGENT if API_KEY else Mode.OFFLINE_MODE).model_dump()
