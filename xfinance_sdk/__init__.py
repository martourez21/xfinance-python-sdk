"""X-Finance SDK package initialization."""

from .client import XFinanceClient

__version__ = "1.0.0"
__author__ = "X-Finance Team"
__email__ = "support@xfinance.com"

__all__ = [
    "XFinanceClient",
    "XFinanceException",
    "AuthenticationException",
    "ValidationException",
    "NetworkException",
    "CompoundInterestRequest",
    "LoanCalculationRequest",
    "InvestmentReturnsRequest",
    "CompoundInterestResponse",
    "LoanCalculationResponse",
    "InvestmentReturnsResponse",
]
