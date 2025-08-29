from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, Field


class PlanResponse(BaseModel):
    id: int = Field(..., description="Plan ID")
    name: str = Field(..., description="Plan name")
    description: Optional[str] = Field(None, description="Plan description")
    price: Decimal = Field(..., description="Plan price")
    features: List[str] = Field(..., description="Plan features")
    api_calls_per_month: int = Field(..., description="Monthly API call limit")
    is_active: bool = Field(..., description="Whether plan is active")
    created_at: datetime = Field(..., description="Plan creation date")