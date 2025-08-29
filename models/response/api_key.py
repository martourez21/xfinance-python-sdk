from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ApiKeyResponse(BaseModel):
    key_id: str = Field(..., description="API key ID")
    key_secret: Optional[str] = Field(None, description="API key secret (only shown once)")
    key_name: str = Field(..., description="API key name")
    status: str = Field(..., description="API key status")
    created_at: datetime = Field(..., description="Creation timestamp")
    expires_at: Optional[datetime] = Field(None, description="Expiration timestamp")