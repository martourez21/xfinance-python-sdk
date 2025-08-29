#!/usr/bin/env python3
"""
Basic usage example for X-Finance-Util Python SDK.
"""

from decimal import Decimal
from xfinance import XFinanceClient, CompoundInterestRequest


def main():
    # Initialize the client
    client = XFinanceClient(
        api_key="your-api-key",
        api_secret="your-api-secret",
        base_url="https://api.xfinanceutil.com"  # or use default
    )

    try:
        # Calculate compound interest
        request = CompoundInterestRequest(
            principal=Decimal("10000.00"),
            annual_rate=Decimal("5.5"),
            years=10,
            compounding_frequency=12
        )

        response = client.calculate_compound_interest(request)

        print(f"Principal: ${response.principal}")
        print(f"Annual Rate: {response.annual_rate}%")
        print(f"Years: {response.years}")
        print(f"Compounding Frequency: {response.compounding_frequency}")
        print(f"Final Amount: ${response.final_amount}")
        print(f"Total Interest: ${response.total_interest}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()