import json
import logging
from typing import Type, TypeVar, Optional, Dict, Any
from dataclasses import asdict

import requests
from pydantic import BaseModel, ValidationError

from .exceptions import (
    XFinanceException,
    AuthenticationException,
    ValidationException,
    NetworkException,
    RateLimitException,
)
from .models.common import ApiResponse
from .utils.validation import validate_request
from .utils.constants import DEFAULT_BASE_URL, DEFAULT_TIMEOUT, USER_AGENT

T = TypeVar('T')
logger = logging.getLogger(__name__)


class XFinanceClient:
    """
    Main client class for interacting with the X-Finance-Util API.

    Provides methods for financial calculations and API operations.

    Args:
        api_key: The API key for authentication
        api_secret: The API secret for authentication
        base_url: The base URL of the API (defaults to production)
        timeout: Request timeout in seconds
        max_retries: Maximum number of retries for failed requests
    """

    def __init__(
            self,
            api_key: str,
            api_secret: str,
            base_url: str = DEFAULT_BASE_URL,
            timeout: int = DEFAULT_TIMEOUT,
            max_retries: int = 3,
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.max_retries = max_retries

        self.session = requests.Session()
        self.session.headers.update({
            'X-API-Key': api_key,
            'X-API-Secret': api_secret,
            'User-Agent': USER_AGENT,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        })

        logger.info("XFinanceClient initialized with base URL: %s", base_url)

    def calculate_compound_interest(
            self,
            request: 'CompoundInterestRequest'
    ) -> 'CompoundInterestResponse':
        """
        Calculate compound interest based on the provided parameters.

        Args:
            request: The compound interest calculation request

        Returns:
            CompoundInterestResponse: The calculation results

        Raises:
            ValidationException: If input validation fails
            AuthenticationException: If authentication fails
            NetworkException: If network issues occur
            RateLimitException: If rate limits are exceeded
            XFinanceException: For other API errors
        """
        validate_request(request)
        return self._post(
            '/finance/compound-interest',
            request,
            CompoundInterestResponse
        )

    def calculate_loan_payment(
            self,
            request: 'LoanCalculationRequest'
    ) -> 'LoanCalculationResponse':
        """
        Calculate loan payment details based on the provided parameters.

        Args:
            request: The loan calculation request

        Returns:
            LoanCalculationResponse: The calculation results

        Raises:
            ValidationException: If input validation fails
            AuthenticationException: If authentication fails
            NetworkException: If network issues occur
            RateLimitException: If rate limits are exceeded
            XFinanceException: For other API errors
        """
        validate_request(request)
        return self._post(
            '/finance/loan-calculation',
            request,
            LoanCalculationResponse
        )

    def calculate_investment_returns(
            self,
            request: 'InvestmentReturnsRequest'
    ) -> 'InvestmentReturnsResponse':
        """
        Calculate investment returns based on the provided parameters.

        Args:
            request: The investment returns calculation request

        Returns:
            InvestmentReturnsResponse: The calculation results

        Raises:
            ValidationException: If input validation fails
            AuthenticationException: If authentication fails
            NetworkException: If network issues occur
            RateLimitException: If rate limits are exceeded
            XFinanceException: For other API errors
        """
        validate_request(request)
        return self._post(
            '/finance/investment-returns',
            request,
            InvestmentReturnsResponse
        )

    def _post(
            self,
            endpoint: str,
            request: BaseModel,
            response_model: Type[T]
    ) -> T:
        """
        Internal method to make POST requests to the API.

        Args:
            endpoint: API endpoint path
            request: Request data as Pydantic model
            response_model: Expected response model type

        Returns:
            The parsed response

        Raises:
            Various XFinanceException subclasses for different error types
        """
        url = f"{self.base_url}/api/v1{endpoint}"

        # Convert Pydantic model to dict, excluding None values
        request_data = request.dict(exclude_none=True)

        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.post(
                    url,
                    json=request_data,
                    timeout=self.timeout
                )
                return self._handle_response(response, response_model)

            except requests.exceptions.Timeout:
                if attempt == self.max_retries:
                    raise NetworkException("Request timed out after multiple retries")
                logger.warning("Request timeout, retrying... (attempt %d/%d)",
                               attempt + 1, self.max_retries)

            except requests.exceptions.ConnectionError:
                if attempt == self.max_retries:
                    raise NetworkException("Connection error after multiple retries")
                logger.warning("Connection error, retrying... (attempt %d/%d)",
                               attempt + 1, self.max_retries)

            except requests.exceptions.RequestException as e:
                raise NetworkException(f"Network error: {str(e)}")

    def _handle_response(self, response: requests.Response, response_model: Type[T]) -> T:
        """
        Handle API response and convert to appropriate model.

        Args:
            response: The HTTP response
            response_model: Expected response model type

        Returns:
            The parsed response data

        Raises:
            Various XFinanceException subclasses based on HTTP status
        """
        try:
            response.raise_for_status()
            response_data = response.json()

            # Handle wrapped API response
            if 'data' in response_data:
                api_response = ApiResponse(**response_data)
                if not api_response.success:
                    raise XFinanceException(api_response.message)
                return response_model(**api_response.data)
            else:
                # Direct response (without success/message wrapper)
                return response_model(**response_data)

        except requests.exceptions.HTTPError as e:
            self._handle_http_error(response, e)
        except (json.JSONDecodeError, ValidationError) as e:
            raise XFinanceException(f"Failed to parse response: {str(e)}")

    def _handle_http_error(self, response: requests.Response, error: requests.HTTPError):
        """
        Handle HTTP errors and convert to appropriate exception types.
        """
        status_code = response.status_code

        try:
            error_data = response.json()
            error_msg = error_data.get('message', response.text)
        except json.JSONDecodeError:
            error_msg = response.text or str(error)

        if status_code == 401:
            raise AuthenticationException(error_msg)
        elif status_code == 403:
            raise AuthenticationException(error_msg)
        elif status_code == 400:
            raise ValidationException(error_msg)
        elif status_code == 429:
            raise RateLimitException(error_msg)
        elif status_code >= 500:
            raise NetworkException(f"Server error: {error_msg}")
        else:
            raise XFinanceException(f"HTTP error {status_code}: {error_msg}")

    def close(self):
        """Close the HTTP session."""
        self.session.close()
        logger.info("XFinanceClient session closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()