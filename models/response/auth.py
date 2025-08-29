from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserResponse(BaseModel):
    id: int = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User email")
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    company_name: Optional[str] = Field(None, description="Company name")
    plan_name: str = Field(..., description="Subscription plan name")
    status: str = Field(..., description="User status")
    created_at: datetime = Field(..., description="Account creation date")


class LoginResponse(BaseModel):
    token: str = Field(..., description="JWT token")
    token_type: str = Field("Bearer", description="Token type")
    user: UserResponse = Field(..., description="User information")