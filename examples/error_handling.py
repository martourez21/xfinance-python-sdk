#!/usr/bin/env python3
"""
Error handling example for X-Finance-Util Python SDK.
"""

from decimal import Decimal
from xfinance import (
    XFinanceClient,
    CompoundInterestRequest,
    AuthenticationException,
    ValidationException,
    NetworkException,
    RateLimitException,
    XFinanceException
)


def main():
    client = XFinanceClient("invalid-key", "invalid-secret")

    try:
        request = CompoundInterestRequest(
            principal=Decimal("10000.00"),
            annual_rate=Decimal("5.5"),
            years=10,
            compounding_frequency=12
        )

        response = client.calculate_compound_interest(request)
        print(f"Success: {response}")

    except AuthenticationException as e:
        print(f"Authentication error: {e}")
        # Handle authentication issues (renew API keys, etc.)

    except ValidationException as e:
        print(f"Validation error: {e}")
        # Show user-friendly error messages

    except RateLimitException as e:
        print(f"Rate limit exceeded: {e}")
        # Implement retry logic with backoff

    except NetworkException as e:
        print(f"Network error: {e}")
        # Check internet connection, retry later

    except XFinanceException as e:
        print(f"API error: {e}")
        # Handle other API errors

    finally:
        client.close()


if __name__ == "__main__":
    main()