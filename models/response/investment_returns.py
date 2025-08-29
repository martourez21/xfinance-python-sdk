from decimal import Decimal

from pydantic import BaseModel, Field


class InvestmentReturnsResponse(BaseModel):
    final_value: Decimal = Field(..., description="Final investment value")
    total_contributions: Decimal = Field(..., description="Total contributions made")
    total_returns: Decimal = Field(..., description="Total returns earned")
    initial_investment: Decimal = Field(..., description="Initial investment amount")
    monthly_contribution: Decimal = Field(..., description="Monthly contribution amount")
    expected_annual_return: Decimal = Field(..., description="Expected annual return rate used")
    years: int = Field(..., description="Number of years")