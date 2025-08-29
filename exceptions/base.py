class XFinanceError(Exception):
    """Base exception for all XFinance SDK errors"""

    def __init__(self, message: str, code: str = None):
        self.message = message
        self.code = code
        super().__init__(message)


class APIError(XFinanceError):
    """Base exception for API-related errors"""

    def __init__(self, message: str, status_code: int = None, code: str = None):
        self.status_code = status_code
        super().__init__(message, code)


class BadRequestError(APIError):
    """400 Bad Request error"""
    pass


class UnauthorizedError(APIError):
    """401 Unauthorized error"""
    pass


class ForbiddenError(APIError):
    """403 Forbidden error"""
    pass


class NotFoundError(APIError):
    """404 Not Found error"""
    pass


class RateLimitError(APIError):
    """429 Rate Limit error"""
    pass


class ServerError(APIError):
    """5xx Server errors"""
    pass


class ValidationError(XFinanceError):
    """Validation error for request parameters"""
    pass