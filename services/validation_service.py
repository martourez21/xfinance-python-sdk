from decimal import Decimal
from typing import Dict, Any

from pydantic import ValidationError as PydanticValidationError

from models.request.api_key import ApiKeyRequest
from models.request.compound_interest import CompoundInterestRequest
from models.request.investment_returns import InvestmentReturnsRequest
from models.request.loan_calculation import LoanCalculationRequest
from ..exceptions.validation import RequestValidationError, ParameterValidationError



class ValidationService:
    @staticmethod
    def validate_compound_interest(data: Dict[str, Any]) -> CompoundInterestRequest:
        try:
            return CompoundInterestRequest(**data)
        except PydanticValidationError as e:
            errors = {}
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                if field not in errors:
                    errors[field] = []
                errors[field].append(msg)
            raise RequestValidationError("Compound interest validation failed", errors)

    @staticmethod
    def validate_loan_calculation(data: Dict[str, Any]) -> LoanCalculationRequest:
        try:
            return LoanCalculationRequest(**data)
        except PydanticValidationError as e:
            errors = {}
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                if field not in errors:
                    errors[field] = []
                errors[field].append(msg)
            raise RequestValidationError("Loan calculation validation failed", errors)

    @staticmethod
    def validate_investment_returns(data: Dict[str, Any]) -> InvestmentReturnsRequest:
        try:
            return InvestmentReturnsRequest(**data)
        except PydanticValidationError as e:
            errors = {}
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                if field not in errors:
                    errors[field] = []
                errors[field].append(msg)
            raise RequestValidationError("Investment returns validation failed", errors)

    @staticmethod
    def validate_api_key_request(data: Dict[str, Any]) -> ApiKeyRequest:
        try:
            return ApiKeyRequest(**data)
        except PydanticValidationError as e:
            errors = {}
            for error in e.errors():
                field = error['loc'][0]
                msg = error['msg']
                if field not in errors:
                    errors[field] = []
                errors[field].append(msg)
            raise RequestValidationError("API key request validation failed", errors)

    @staticmethod
    def validate_positive_number(value: Any, field_name: str) -> Decimal:
        """Validate that a value is a positive number"""
        try:
            num = Decimal(str(value))
            if num <= 0:
                raise ParameterValidationError(f"{field_name} must be positive")
            return num
        except (ValueError, TypeError):
            raise ParameterValidationError(f"{field_name} must be a valid number")