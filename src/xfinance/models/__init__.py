"""
Data models for the X-Finance-Util Python SDK.
"""

from .common import ApiResponse, ErrorDetails
from .request import (
    CompoundInterestRequest,
    LoanCalculationRequest,
    InvestmentReturnsRequest,
)
from .response import (
    CompoundInterestResponse,
    LoanCalculationResponse,
    InvestmentReturnsResponse,
)

__all__ = [
    'ApiResponse',
    'ErrorDetails',
    'CompoundInterestRequest',
    'LoanCalculationRequest',
    'InvestmentReturnsRequest',
    'CompoundInterestResponse',
    'LoanCalculationResponse',
    'InvestmentReturnsResponse',
]