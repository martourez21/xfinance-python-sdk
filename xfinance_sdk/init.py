"""
XFinance Python SDK - A comprehensive financial calculations SDK
"""
from exceptions.authentication import AuthenticationError
from exceptions.base import XFinanceError, APIError, BadRequestError, UnauthorizedError, ForbiddenError, NotFoundError, \
    RateLimitError, ServerError, ValidationError
from exceptions.network import NetworkError, TimeoutError
from models.request.api_key import ApiKeyRequest
from models.request.auth import LoginRequest, UserRegistrationRequest
from models.request.compound_interest import CompoundInterestRequest
from models.request.investment_returns import InvestmentReturnsRequest
from models.request.loan_calculation import LoanCalculationRequest
from models.response.api_key import ApiKeyResponse
from models.response.auth import UserResponse, LoginResponse
from models.response.compound_interest import CompoundInterestResponse
from models.response.investment_returns import InvestmentReturnsResponse
from models.response.loan_calculation import LoanCalculationResponse
from models.response.plan import PlanResponse
from .client import XFinanceClient, AsyncXFinanceClient
from .config.settings import Settings


__version__ = "1.0.0"
__author__ = "XFinance Team"
__license__ = "MIT"

__all__ = [
    # Clients
    'XFinanceClient',
    'AsyncXFinanceClient',

    # Config
    'Settings',

    # Request Models
    'CompoundInterestRequest',
    'LoanCalculationRequest',
    'InvestmentReturnsRequest',
    'ApiKeyRequest',
    'UserRegistrationRequest',
    'LoginRequest',

    # Response Models
    'CompoundInterestResponse',
    'LoanCalculationResponse',
    'InvestmentReturnsResponse',
    'ApiKeyResponse',
    'UserResponse',
    'LoginResponse',
    'PlanResponse',

    # Exceptions
    'XFinanceError',
    'APIError',
    'BadRequestError',
    'UnauthorizedError',
    'ForbiddenError',
    'NotFoundError',
    'RateLimitError',
    'ServerError',
    'ValidationError',
    'AuthenticationError',
    'NetworkError',
    'TimeoutError',
]