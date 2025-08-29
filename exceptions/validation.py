from typing import Dict, List, Optional

from .base import ValidationError


class RequestValidationError(ValidationError):
    """Validation error for API requests"""

    def __init__(self, message: str, errors: Optional[Dict[str, List[str]]] = None):
        self.errors = errors or {}
        super().__init__(message)


class ParameterValidationError(ValidationError):
    """Specific parameter validation error"""
    pass