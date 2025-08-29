from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    api_base_url: str = Field("https://api.xfinance.com", env="XFINANCE_API_URL")
    api_key: Optional[str] = Field(None, env="XFINANCE_API_KEY")
    api_secret: Optional[str] = Field(None, env="XFINANCE_API_SECRET")
    timeout: int = Field(30, env="XFINANCE_TIMEOUT")
    max_retries: int = Field(3, env="XFINANCE_MAX_RETRIES")

    class Config:
        env_file = ".env"
        case_sensitive = False