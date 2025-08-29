from decimal import Decimal

from pydantic import BaseModel, Field, validator


class InvestmentReturnsRequest(BaseModel):
    initial_investment: Decimal = Field(..., gt=0, description="Initial investment amount")
    monthly_contribution: Decimal = Field(..., ge=0, description="Monthly contribution amount")
    expected_annual_return: Decimal = Field(..., ge=0, description="Expected annual return rate")
    years: int = Field(..., ge=1, description="Number of years")

    @validator('initial_investment', 'monthly_contribution', 'expected_annual_return')
    def validate_decimal_values(cls, v):
        return round(v, 6)