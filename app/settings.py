import os
from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Allgemein
    app_name: str = "manager-bot"
    debug: bool = False

    # Inbound-Auth für /task (optional)
    inbound_token: Optional[str] = os.getenv("MANAGER_INBOUND_TOKEN")

    # Outbound zum Researcher-Agent
    researcher_url: Optional[str] = os.getenv("RESEARCHER_URL")  # z.B. http://localhost:9000
    researcher_token: Optional[str] = os.getenv("RESEARCHER_OUTBOUND_TOKEN")

    class Config:
        env_file = ".env"


settings = Settings()
