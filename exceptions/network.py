from .base import XFinanceError


class NetworkError(XFinanceError):
    """Network connectivity errors"""
    pass


class TimeoutError(XFinanceError):
    """Request timeout error"""
    pass


class ConnectionError(XFinanceError):
    """Connection error"""
    pass