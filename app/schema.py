from pydantic import BaseModel
from enum import StrEnum


class Mode(StrEnum):
    AI_AGENT = "ai_agent"
    OFFLINE_MODE = "offline_mode"


class AskAgentResponse(BaseModel):
    response: str


class Status(BaseModel):
    mode: Mode
