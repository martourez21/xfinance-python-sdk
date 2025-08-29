from .base import APIError


class AuthenticationError(APIError):
    """Authentication related errors"""
    pass


class InvalidApiKeyError(AuthenticationError):
    """Invalid API key error"""
    pass


class ExpiredApiKeyError(AuthenticationError):
    """Expired API key error"""
    pass