from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field, validator


class CompoundInterestRequest(BaseModel):
    """
    Request model for compound interest calculation.

    Attributes:
        principal: Principal amount (must be greater than 0)
        annual_rate: Annual interest rate (cannot be negative)
        years: Number of years (must be at least 1)
        compounding_frequency: Compounding frequency per year (must be at least 1)
    """
    principal: Decimal = Field(..., gt=0, description="Principal amount must be greater than 0")
    annual_rate: Decimal = Field(..., ge=0, description="Annual interest rate cannot be negative")
    years: int = Field(..., ge=1, description="Years must be at least 1")
    compounding_frequency: int = Field(..., ge=1, description="Compounding frequency must be at least 1")

    class Config:
        json_encoders = {
            Decimal: str
        }


class LoanCalculationRequest(BaseModel):
    """
    Request model for loan calculation.

    Attributes:
        loan_amount: Loan amount (must be greater than 0)
        annual_rate: Annual interest rate (cannot be negative)
        term_years: Loan term in years (must be at least 1)
    """
    loan_amount: Decimal = Field(..., gt=0, description="Loan amount must be greater than 0")
    annual_rate: Decimal = Field(..., ge=0, description="Annual interest rate cannot be negative")
    term_years: int = Field(..., ge=1, description="Loan term must be at least 1 year")

    class Config:
        json_encoders = {
            Decimal: str
        }


class InvestmentReturnsRequest(BaseModel):
    """
    Request model for investment returns calculation.

    Attributes:
        initial_investment: Initial investment amount (cannot be negative)
        monthly_contribution: Monthly contribution amount (cannot be negative)
        expected_annual_return: Expected annual return rate (cannot be negative)
        years: Number of years (must be at least 1)
    """
    initial_investment: Decimal = Field(..., ge=0, description="Initial investment cannot be negative")
    monthly_contribution: Decimal = Field(..., ge=0, description="Monthly contribution cannot be negative")
    expected_annual_return: Decimal = Field(..., ge=0, description="Expected annual return cannot be negative")
    years: int = Field(..., ge=1, description="Years must be at least 1")

    class Config:
        json_encoders = {
            Decimal: str
        }