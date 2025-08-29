"""
X-Finance-Util Python SDK
A comprehensive Python SDK for interacting with the X-Finance-Util API.
"""

from .client import XFinanceClient
from .exceptions import (
    XFinanceException,
    AuthenticationException,
    ValidationException,
    NetworkException,
    RateLimitException,
)
from .models.request import (
    CompoundInterestRequest,
    LoanCalculationRequest,
    InvestmentReturnsRequest,
)
from .models.response import (
    CompoundInterestResponse,
    LoanCalculationResponse,
    InvestmentReturnsResponse,
    ApiResponse,
)

__version__ = "1.0.0"
__author__ = "X-Finance Team"
__email__ = "dev@xfinance.com"

__all__ = [
    "XFinanceClient",
    "XFinanceException",
    "AuthenticationException",
    "ValidationException",
    "NetworkException",
    "RateLimitException",
    "CompoundInterestRequest",
    "LoanCalculationRequest",
    "InvestmentReturnsRequest",
    "CompoundInterestResponse",
    "LoanCalculationResponse",
    "InvestmentReturnsResponse",
    "ApiResponse",
]