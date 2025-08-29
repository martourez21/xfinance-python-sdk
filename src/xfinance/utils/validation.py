from decimal import Decimal
from typing import Any

from ..exceptions import ValidationException
from ..models.request import (
    CompoundInterestRequest,
    LoanCalculationRequest,
    InvestmentReturnsRequest,
)


def validate_request(request: Any) -> None:
    """
    Validate request parameters before sending to API.

    Args:
        request: The request object to validate

    Raises:
        ValidationException: If validation fails
    """
    if isinstance(request, CompoundInterestRequest):
        _validate_compound_interest_request(request)
    elif isinstance(request, LoanCalculationRequest):
        _validate_loan_calculation_request(request)
    elif isinstance(request, InvestmentReturnsRequest):
        _validate_investment_returns_request(request)
    else:
        raise ValidationException(f"Unknown request type: {type(request)}")


def _validate_compound_interest_request(request: CompoundInterestRequest) -> None:
    """Validate compound interest request parameters."""
    if request.years > 100:
        raise ValidationException("Years cannot exceed 100")
    if request.compounding_frequency > 365:
        raise ValidationException("Compounding frequency cannot exceed 365")
    if request.annual_rate > Decimal('1000'):
        raise ValidationException("Annual rate cannot exceed 1000%")


def _validate_loan_calculation_request(request: LoanCalculationRequest) -> None:
    """Validate loan calculation request parameters."""
    if request.term_years > 50:
        raise ValidationException("Loan term cannot exceed 50 years")
    if request.annual_rate > Decimal('1000'):
        raise ValidationException("Annual rate cannot exceed 1000%")


def _validate_investment_returns_request(request: InvestmentReturnsRequest) -> None:
    """Validate investment returns request parameters."""
    if request.years > 100:
        raise ValidationException("Years cannot exceed 100")
    if request.expected_annual_return > Decimal('1000'):
        raise ValidationException("Expected annual return cannot exceed 1000%")