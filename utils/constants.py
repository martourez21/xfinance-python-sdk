from enum import Enum


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class ApiEndpoints:
    BASE = "/api/v1"

    # Authentication endpoints
    REGISTER = f"{BASE}/auth/register"
    LOGIN = f"{BASE}/auth/login"
    VALIDATE_TOKEN = f"{BASE}/auth/validate"

    # API Key endpoints
    GENERATE_API_KEY = f"{BASE}/keys/generate"
    LIST_API_KEYS = f"{BASE}/keys/list"

    # Finance endpoints
    COMPOUND_INTEREST = f"{BASE}/finance/compound-interest"
    LOAN_CALCULATION = f"{BASE}/finance/loan-calculation"
    INVESTMENT_RETURNS = f"{BASE}/finance/investment-returns"

    # Plan endpoints
    LIST_PLANS = f"{BASE}/plans"


class ErrorCodes(str, Enum):
    VALIDATION_ERROR = "VALIDATION_ERROR"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    AUTHORIZATION_ERROR = "AUTHORIZATION_ERROR"
    RATE_LIMIT_ERROR = "RATE_LIMIT_ERROR"
    SERVER_ERROR = "SERVER_ERROR"
    NETWORK_ERROR = "NETWORK_ERROR"
    NOT_FOUND_ERROR = "NOT_FOUND_ERROR"


class PlanNames(str, Enum):
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"