from decimal import Decimal

from pydantic import BaseModel, Field, validator


class LoanCalculationRequest(BaseModel):
    loan_amount: Decimal = Field(..., gt=0, description="Loan amount")
    annual_rate: Decimal = Field(..., ge=0, description="Annual interest rate")
    term_years: int = Field(..., ge=1, description="Loan term in years")

    @validator('loan_amount', 'annual_rate')
    def validate_decimal_values(cls, v):
        return round(v, 6)