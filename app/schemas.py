from pydantic import BaseModel, Field, AnyHttpUrl
from typing import List, Optional, Literal, Dict, Any


class Source(BaseModel):
    title: str
    url: AnyHttpUrl
    verdict: Literal["reliable", "tentative"] = "tentative"
    notes: Optional[str] = None


class ResearchPayload(BaseModel):
    query: str
    focus: Optional[str] = None
    max_sources: int = Field(default=5, ge=1, le=20)
    allow_domains: Optional[List[str]] = None


class ResearchResult(BaseModel):
    summary: str
    bullets: List[str]
    sources: List[Source]
    confidence: float = Field(ge=0.0, le=1.0)


class TaskRequest(BaseModel):
    task: str
    intent: Literal["research", "answer", "plan", "mixed"] = "research"
    params: Optional[Dict[str, Any]] = None


class StepResult(BaseModel):
    name: str
    ok: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class TaskResponse(BaseModel):
    task_id: str
    steps: List[StepResult]
    result_markdown: Optional[str] = None
