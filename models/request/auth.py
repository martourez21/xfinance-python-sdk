from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserRegistrationRequest(BaseModel):
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., min_length=8, description="User password")
    first_name: str = Field(..., min_length=1, description="User first name")
    last_name: str = Field(..., min_length=1, description="User last name")
    company_name: Optional[str] = Field(None, description="Company name")
    plan_name: str = Field(..., min_length=1, description="Subscription plan name")


class LoginRequest(BaseModel):
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., min_length=1, description="User password")