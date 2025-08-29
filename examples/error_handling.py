#!/usr/bin/env python3
"""
Error handling example for xfinance Python SDK
"""

import os
from decimal import Decimal

from exceptions.base import ValidationError, RateLimitError, BadRequestError, UnauthorizedError
from exceptions.validation import RequestValidationError
from models.request.compound_interest import CompoundInterestRequest
from xfinance_sdk import XFinanceClient



def main():
    # Test with invalid API key
    print("=== Testing Invalid API Key ===")
    try:
        client = XFinanceClient(api_key="invalid-key")
        request = CompoundInterestRequest(
            principal=Decimal("10000"),
            annual_rate=Decimal("0.05"),
            years=10,
            compounding_frequency=12
        )
        response = client.calculate_compound_interest(request)
        print("Unexpected success!")
    except UnauthorizedError as e:
        print(f"Authentication failed as expected: {e.message}")
    except Exception as e:
        print(f"Unexpected error type: {e}")
    print()

    # Test validation errors
    print("=== Testing Validation Errors ===")
    try:
        # This should fail validation
        request = CompoundInterestRequest(
            principal=Decimal("-100"),  # Negative principal
            annual_rate=Decimal("0.05"),
            years=10,
            compounding_frequency=12
        )
        response = client.calculate_compound_interest(request)
        print("Unexpected success!")
    except RequestValidationError as e:
        print(f"Validation failed as expected: {e.message}")
        if hasattr(e, 'errors') and e.errors:
            print("Field errors:")
            for field, errors in e.errors.items():
                print(f"  {field}: {', '.join(errors)}")
    except Exception as e:
        print(f"Unexpected error type: {e}")
    print()

    # Test with valid credentials but invalid request
    api_key = os.getenv("XFINANCE_API_KEY")
    if api_key:
        print("=== Testing with Valid API Key but Bad Request ===")
        try:
            client = XFinanceClient(api_key=api_key)
            # Extremely high rate that might be rejected
            request = CompoundInterestRequest(
                principal=Decimal("10000"),
                annual_rate=Decimal("5.0"),  # 500% rate
                years=10,
                compounding_frequency=12
            )
            response = client.calculate_compound_interest(request)
            print("Request succeeded!")
        except BadRequestError as e:
            print(f"Bad request as expected: {e.message}")
        except Exception as e:
            print(f"Other error: {e}")
    else:
        print("Set XFINANCE_API_KEY to test with valid credentials")

    print()
    print("=== Testing Error Handling Best Practices ===")

    def safe_calculation(client, request):
        try:
            response = client.calculate_compound_interest(request)
            return response
        except UnauthorizedError:
            print("Please check your API credentials")
            raise
        except BadRequestError as e:
            print(f"Please check your input parameters: {e.message}")
            raise
        except RateLimitError:
            print("Rate limit exceeded. Please try again later.")
            raise
        except ValidationError as e:
            print(f"Input validation failed: {e.message}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    try:
        client = XFinanceClient(api_key=api_key or "test-key")
        request = CompoundInterestRequest(
            principal=Decimal("10000"),
            annual_rate=Decimal("0.05"),
            years=10,
            compounding_frequency=12
        )
        response = safe_calculation(client, request)
        print("Calculation successful!")
    except Exception:
        print("Error handled gracefully")


if __name__ == "__main__":
    main()