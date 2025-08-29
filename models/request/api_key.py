from typing import Optional

from pydantic import BaseModel, Field


class ApiKeyRequest(BaseModel):
    key_name: str = Field(..., min_length=1, description="Name for the API key")
    description: Optional[str] = Field(None, description="Description of the API key usage")