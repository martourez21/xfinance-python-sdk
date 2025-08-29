#!/usr/bin/env python3
"""
Configuration example for xfinance Python SDK
"""

import os
from decimal import Decimal

from models.request.compound_interest import CompoundInterestRequest
from xfinance_sdk import XFinanceClient, __all__
from xfinance_sdk.config.retry_config import RetryConfig
from xfinance_sdk.config.settings import Settings


def main():
    print("=== Configuration Examples ===")

    # Method 1: Environment variables
    print("1. Using environment variables:")
    os.environ["XFINANCE_API_KEY"] = "your-api-key-here"
    os.environ["XFINANCE_TIMEOUT"] = "60"
    os.environ["XFINANCE_MAX_RETRIES"] = "5"

    client1 = XFinanceClient()
    print(f"Client configured with timeout: {client1.settings.timeout}")
    print(f"Client configured with max retries: {client1.settings.max_retries}")
    print()

    # Method 2: Programmatic settings
    print("2. Using Settings class:")
    settings = Settings(
        api_key="your-api-key",
        api_secret="your-api-secret",
        timeout=45,
        max_retries=4
    )

    client2 = XFinanceClient(settings=settings)
    print(f"Client configured with timeout: {client2.settings.timeout}")
    print(f"Client configured with max retries: {client2.settings.max_retries}")
    print()

    # Method 3: Direct parameters
    print("3. Using direct parameters:")
    client3 = XFinanceClient(
        api_key="your-api-key",
        api_secret="your-api-secret",
        base_url="https://api.xfinance.com"
    )
    print(f"Client base URL: {client3.base_url}")
    print()

    # Method 4: Custom retry configuration
    print("4. Using custom retry configuration:")
    retry_config = RetryConfig(
        max_retries=5,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        timeout=60
    )

    client4 = XFinanceClient(
        api_key="your-api-key",
        retry_config=retry_config
    )
    print(f"Custom retry config - max retries: {retry_config.max_retries}")
    print(f"Custom retry config - backoff factor: {retry_config.backoff_factor}")
    print()

    # Method 5: Context manager for resource cleanup
    print("5. Using context manager:")
    with XFinanceClient(api_key="your-api-key") as client:
        request = CompoundInterestRequest(
            principal=Decimal("10000"),
            annual_rate=Decimal("0.05"),
            years=5,
            compounding_frequency=12
        )
        # response = client.calculate_compound_interest(request)
        print("Client used within context manager - resources will be auto-closed")
    print()

    # Method 6: Multiple clients with different configurations
    print("6. Multiple clients with different configs:")

    # Client for high-priority requests
    high_priority_client = XFinanceClient(
        api_key="high-priority-key",
        timeout=10,
        retry_config=RetryConfig(max_retries=2)
    )

    # Client for batch processing
    batch_client = XFinanceClient(
        api_key="batch-key",
        timeout=120,
        retry_config=RetryConfig(max_retries=5, backoff_factor=2.0)
    )

    print("Multiple clients created with different configurations")
    print()

    # Clean up
    client1.close()
    client2.close()
    client3.close()
    client4.close()
    high_priority_client.close()
    batch_client.close()


if __name__ == "__main__":
    main()