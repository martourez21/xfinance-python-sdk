from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class ErrorDetails(BaseModel):
    timestamp: datetime = Field(..., description="Error timestamp")
    status: int = Field(..., description="HTTP status code")
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    path: Optional[str] = Field(None, description="Request path")
    error_code: Optional[str] = Field(None, description="Error code")
    details: Optional[Dict[str, List[str]]] = Field(None, description="Validation errors")