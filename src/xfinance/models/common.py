from datetime import datetime
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel, Field

T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    """
    Generic API response wrapper for all API responses.

    Attributes:
        success: Whether the request was successful
        message: Response message
        data: Response data
        timestamp: Response timestamp
        request_id: Request identifier (if available)
    """
    success: bool
    message: str
    data: Optional[T] = None
    timestamp: datetime = Field(default_factory=datetime.now)
    request_id: Optional[str] = None


class ErrorDetails(BaseModel):
    """
    Detailed error information for API error responses.

    Attributes:
        code: Error code
        message: Error message
        field: Field that caused the error (if applicable)
        details: Additional error details
    """
    code: str
    message: str
    field: Optional[str] = None
    details: Optional[str] = None