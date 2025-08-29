from decimal import Decimal

from pydantic import BaseModel, Field


class CompoundInterestResponse(BaseModel):
    final_amount: Decimal = Field(..., description="Final amount after compounding")
    total_interest: Decimal = Field(..., description="Total interest earned")
    principal: Decimal = Field(..., description="Original principal amount")
    annual_rate: Decimal = Field(..., description="Annual interest rate used")
    years: int = Field(..., description="Number of years")
    compounding_frequency: int = Field(..., description="Compounding frequency used")