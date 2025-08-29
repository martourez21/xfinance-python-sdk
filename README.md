# X-Finance Python SDK

[![PyPI Version](https://img.shields.io/pypi/v/xfinance-sdk.svg)](https://pypi.org/project/xfinance-sdk/)
[![Python Versions](https://img.shields.io/pypi/pyversions/xfinance-sdk.svg)](https://pypi.org/project/xfinance-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/martourez21/xfinance-python-sdk/workflows/CI/badge.svg)](https://github.com/martourez21/xfinance-python-sdk/actions)
[![Code Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/martourez21/xfinance-python-sdk)
[![Downloads](https://img.shields.io/pypi/dm/xfinance-sdk.svg)](https://pypi.org/project/xfinance-sdk/)

A modern, type-safe Python SDK for interacting with the X-Finance-Util API. This SDK provides seamless access to financial calculation services including compound interest, loan payments, and investment return calculations.

## ✨ Features

- **🔧 Fully Typed**: Complete type annotations with Pydantic models
- **🚀 Async Ready**: Supports both synchronous and asynchronous operations
- **🛡️ Error Handling**: Comprehensive exception hierarchy with detailed error messages
- **📦 Easy Installation**: Simple pip installation with no heavy dependencies
- **⚡ Performance**: Efficient HTTP connection pooling and request retry logic
- **📚 Documentation**: Comprehensive docstrings and usage examples

## 📦 Installation

```bash
pip install xfinance-sdk
```

## ⚡ Quick Start

```python
from xfinance import XFinanceClient
from xfinance.models.request import CompoundInterestRequest
from decimal import Decimal

# Initialize the client
client = XFinanceClient(
    api_key="your-api-key",
    api_secret="your-api-secret",
    base_url="https://api.xfinanceutil.com"  # Optional: defaults to production
)

try:
    # Create a compound interest calculation request
    request = CompoundInterestRequest(
        principal=Decimal("10000.00"),
        annual_rate=Decimal("5.5"),
        years=10,
        compounding_frequency=12
    )
    
    # Get the calculation result
    response = client.calculate_compound_interest(request)
    
    print(f"Final Amount: ${response.final_amount:,.2f}")
    print(f"Total Interest: ${response.total_interest:,.2f}")
    
except Exception as e:
    print(f"Calculation failed: {e}")

finally:
    # Always close the client
    client.close()
```

## 📋 API Reference

### Available Calculations

#### Compound Interest
```python
response = client.calculate_compound_interest(
    CompoundInterestRequest(
        principal=Decimal("10000.00"),
        annual_rate=Decimal("5.5"),
        years=10,
        compounding_frequency=12
    )
)
```

#### Loan Payment Calculation
```python
response = client.calculate_loan_payment(
    LoanCalculationRequest(
        loan_amount=Decimal("300000.00"),
        annual_rate=Decimal("3.5"),
        term_years=30
    )
)
```

#### Investment Returns
```python
response = client.calculate_investment_returns(
    InvestmentReturnsRequest(
        initial_investment=Decimal("5000.00"),
        monthly_contribution=Decimal("500.00"),
        expected_annual_return=Decimal("7.0"),
        years=20
    )
)
```

## 🔧 Configuration

### Client Options

```python
client = XFinanceClient(
    api_key="your-api-key",
    api_secret="your-api-secret",
    base_url="https://api.xfinanceutil.com",  # Optional
    timeout=30,                               # Request timeout in seconds
    max_retries=3                             # Maximum retry attempts
)
```

### Environment Variables

You can also configure the client using environment variables:

```bash
export XFINANCE_API_KEY="your-api-key"
export XFINANCE_API_SECRET="your-api-secret"
export XFINANCE_BASE_URL="https://api.xfinanceutil.com"
```

```python
# Client will automatically use environment variables
client = XFinanceClient()
```

## 🛡️ Error Handling

The SDK provides detailed exception handling:

```python
from xfinance.exceptions import (
    AuthenticationException,
    ValidationException,
    NetworkException,
    RateLimitException,
    XFinanceException
)

try:
    response = client.calculate_compound_interest(request)
    
except AuthenticationException as e:
    print(f"Authentication failed: {e}")
    # Handle invalid API credentials
    
except ValidationException as e:
    print(f"Invalid request: {e}")
    # Handle invalid input parameters
    
except RateLimitException as e:
    print(f"Rate limit exceeded: {e}")
    # Implement retry logic with backoff
    
except NetworkException as e:
    print(f"Network error: {e}")
    # Handle connection issues
    
except XFinanceException as e:
    print(f"API error: {e}")
    # Handle other API errors
```

## 🔄 Async Support

For asynchronous applications:

```python
import asyncio
from xfinance import AsyncXFinanceClient

async def main():
    async with AsyncXFinanceClient("your-api-key", "your-api-secret") as client:
        response = await client.calculate_compound_interest_async(request)
        print(f"Async result: {response.final_amount}")

asyncio.run(main())
```

## 📊 Response Models

All responses are strongly typed Pydantic models:

```python
# CompoundInterestResponse
response.final_amount          # Decimal: Final amount after interest
response.total_interest        # Decimal: Total interest earned
response.principal             # Decimal: Original principal
response.annual_rate           # Decimal: Annual interest rate used
response.years                 # int: Number of years
response.compounding_frequency # int: Compounding frequency

# LoanCalculationResponse  
response.monthly_payment       # Decimal: Monthly payment amount
response.total_interest        # Decimal: Total interest paid
response.total_amount          # Decimal: Total amount paid
response.loan_amount           # Decimal: Original loan amount
response.annual_rate           # Decimal: Annual interest rate used
response.term_years            # int: Loan term in years

# InvestmentReturnsResponse
response.final_value           # Decimal: Final investment value
response.total_contributions   # Decimal: Total contributions made
response.total_returns         # Decimal: Total returns earned
response.initial_investment    # Decimal: Initial investment amount
response.monthly_contribution  # Decimal: Monthly contribution amount
response.expected_annual_return # Decimal: Expected annual return rate
response.years                 # int: Number of years
```

## 🚀 Advanced Usage

### Custom HTTP Client

```python
import requests
from xfinance import XFinanceClient

# Use a custom session
session = requests.Session()
session.headers.update({"Custom-Header": "value"})

client = XFinanceClient(
    api_key="your-key",
    api_secret="your-secret",
    session=session  # Use custom session
)
```

### Request Validation

```python
from xfinance.utils.validation import validate_request

# Manual validation
try:
    validate_request(your_request)
    response = client.calculate_compound_interest(your_request)
except ValidationException as e:
    print(f"Validation failed: {e}")
```

## 📚 Examples

Check out the [examples directory](https://github.com/martourez21/xfinance-python-sdk/tree/main/examples) for complete usage examples:

- [Basic Usage](examples/basic_usage.py)
- [Error Handling](examples/error_handling.py) 
- [Async Operations](examples/async_usage.py)
- [Batch Processing](examples/batch_processing.py)

## 🔧 Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/martourez21/xfinance-python-sdk.git
cd xfinance-python-sdk

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Run linting
black src/ tests/ examples/
isort src/ tests/ examples/
flake8 src/ tests/
mypy src/
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=xfinance --cov-report=html

# Run specific test file
pytest tests/test_client.py -v
```

## 📊 Performance

The SDK includes built-in performance optimizations:

- **Connection Pooling**: Reuses HTTP connections for better performance
- **Request Retry**: Automatic retry for failed requests with exponential backoff
- **Efficient Serialization**: Optimized JSON serialization/deserialization
- **Memory Efficiency**: Minimal memory footprint with lazy loading

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [GitHub Repository](https://github.com/martourez21/xfinance-python-sdk/)
- **Issues**: [GitHub Issues](https://github.com/martourez21/xfinance-python-sdk/issues)
- **Email**: nestorabiawuh@gmail.com
- **Developer**: Nestor Martourez

## 🔗 Links

- **[PyPI Package](https://pypi.org/project/xfinance-sdk/)**
- **[GitHub Repository](https://github.com/martourez21/xfinance-python-sdk)**
- **[Release Notes](https://github.com/martourez21/xfinance-python-sdk/releases)**
- **[Issue Tracker](https://github.com/martourez21/xfinance-python-sdk/issues)**

---

**Note**: This SDK requires valid API credentials from [X-Finance-Util](https://xfinanceutil.com). Sign up for an account to get your API keys.

---

<div align="center">
  
Made with ❤️ by [Nestor Martourez](mailto:nestorabiawuh@gmail.com)

[![GitHub](https://img.shields.io/badge/GitHub-martourez21-blue?style=flat&logo=github)](https://github.com/martourez21)

</div>

## 📈 Versioning

This project uses [Semantic Versioning](https://semver.org/). Given a version number MAJOR.MINOR.PATCH:

- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible functionality additions  
- **PATCH**: Backward-compatible bug fixes

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes and releases.

---

*This SDK is independently developed by Nestor Martourez and is officially affiliated with X-Finance-Util.*