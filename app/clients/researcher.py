import httpx
from typing import Optional
from ..schemas import ResearchPayload, ResearchResult
from ..settings import settings


class ResearcherClient:
    def __init__(self, base_url: Optional[str]):
        self.base_url = base_url

    async def research(self, payload: ResearchPayload) -> Optional[ResearchResult]:
        if not self.base_url:
            return None

        headers = {}
        if settings.researcher_token:
            headers["X-API-Key"] = settings.researcher_token

        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                f"{self.base_url.rstrip('/')}/research",
                json=payload.dict(),
                headers=headers,
            )
            r.raise_for_status()
            return ResearchResult(**r.json())
