from decimal import Decimal

from pydantic import BaseModel, Field


class LoanCalculationResponse(BaseModel):
    monthly_payment: Decimal = Field(..., description="Monthly payment amount")
    total_interest: Decimal = Field(..., description="Total interest paid over loan term")
    total_amount: Decimal = Field(..., description="Total amount paid (principal + interest)")
    loan_amount: Decimal = Field(..., description="Original loan amount")
    annual_rate: Decimal = Field(..., description="Annual interest rate used")
    term_years: int = Field(..., description="Loan term in years")