from decimal import Decimal
from pydantic import BaseModel, Field


class CompoundInterestResponse(BaseModel):
    """
    Response model for compound interest calculation.

    Attributes:
        final_amount: Final amount after interest
        total_interest: Total interest earned
        principal: Original principal amount
        annual_rate: Annual interest rate used
        years: Number of years
        compounding_frequency: Compounding frequency used
    """
    final_amount: Decimal
    total_interest: Decimal
    principal: Decimal
    annual_rate: Decimal
    years: int
    compounding_frequency: int


class LoanCalculationResponse(BaseModel):
    """
    Response model for loan calculation.

    Attributes:
        monthly_payment: Monthly payment amount
        total_interest: Total interest paid
        total_amount: Total amount paid
        loan_amount: Original loan amount
        annual_rate: Annual interest rate used
        term_years: Loan term in years
    """
    monthly_payment: Decimal
    total_interest: Decimal
    total_amount: Decimal
    loan_amount: Decimal
    annual_rate: Decimal
    term_years: int


class InvestmentReturnsResponse(BaseModel):
    """
    Response model for investment returns calculation.

    Attributes:
        final_value: Final investment value
        total_contributions: Total contributions made
        total_returns: Total returns earned
        initial_investment: Initial investment amount
        monthly_contribution: Monthly contribution amount
        expected_annual_return: Expected annual return rate used
        years: Number of years
    """
    final_value: Decimal
    total_contributions: Decimal
    total_returns: Decimal
    initial_investment: Decimal
    monthly_contribution: Decimal
    expected_annual_return: Decimal
    years: int