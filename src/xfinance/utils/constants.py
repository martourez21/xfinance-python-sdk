"""
Constants used throughout the X-Finance-Util Python SDK.
"""

# API Configuration
DEFAULT_BASE_URL = "http://localhost:8087/api/v1"
DEFAULT_TIMEOUT = 30  # seconds
MAX_RETRIES = 3

# HTTP Headers
USER_AGENT = "X-Finance-Python-SDK/1.0.0"
CONTENT_TYPE_JSON = "application/json"

# API Endpoints
ENDPOINT_COMPOUND_INTEREST = "/finance/compound-interest"
ENDPOINT_LOAN_CALCULATION = "/finance/loan-calculation"
ENDPOINT_INVESTMENT_RETURNS = "/finance/investment-returns"

# Error Messages
ERROR_AUTHENTICATION = "Authentication failed. Please check your API credentials."
ERROR_VALIDATION = "Request validation failed. Please check your input parameters."
ERROR_NETWORK = "Network error occurred. Please check your connection and try again."
ERROR_RATE_LIMIT = "Rate limit exceeded. Please try again later."
ERROR_SERVER = "Server error occurred. Please try again later."

# Validation Limits
MAX_YEARS = 100
MAX_COMPOUNDING_FREQUENCY = 365
MAX_LOAN_TERM = 50
MAX_INTEREST_RATE = 1000  # 1000%