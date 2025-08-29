# xfinance Python SDK

[![PyPI Version](https://img.shields.io/pypi/v/xfinance-python-sdk.svg)](https://pypi.org/project/xfinance-python-sdk/)
[![Python Versions](https://img.shields.io/pypi/pyversions/xfinance-python-sdk.svg)](https://pypi.org/project/xfinance-python-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://xfinance.github.io/xfinance-python-sdk/)
[![Build Status](https://img.shields.io/github/actions/workflow/status/martourez21/xfinance-python-sdk/ci.yml?branch=main)](https://github.com/martourez21/xfinance-python-sdk/actions)
[![codecov](https://codecov.io/gh/martourez21/xfinance-python-sdk/branch/main/graph/badge.svg)](https://codecov.io/gh/martourez21/xfinance-python-sdk)

A comprehensive Python SDK for interacting with the XFinance API, providing financial calculation services including compound interest, loan payments, and investment returns.

## 🌟 Features

- 🚀 **Easy to Use**: Simple and intuitive API design
- 💰 **Financial Calculations**: Compound interest, loan payments, investment returns
- 🔐 **Authentication**: API key and JWT token support
- ⚡ **Async Support**: Non-blocking async operations
- 🛡️ **Error Handling**: Comprehensive exception hierarchy
- 📊 **Validation**: Request validation with detailed error messages
- 🔄 **Retry Logic**: Automatic retry for transient failures
- 📚 **Full Documentation**: Comprehensive guides and API references

## 📦 Installation

```bash
pip install xfinance-python-sdk
```

## 🚀 Quick Start

```python
from xfinance_sdk import XFinanceClient
from xfinance_sdk.models.request import CompoundInterestRequest
from decimal import Decimal

# Initialize client
client = XFinanceClient(api_key="your-api-key")

# Calculate compound interest
request = CompoundInterestRequest(
    principal=Decimal("10000"),
    annual_rate=Decimal("0.05"),
    years=10,
    compounding_frequency=12
)

response = client.calculate_compound_interest(request)
print(f"Final amount: ${response.final_amount:,.2f}")
print(f"Total interest: ${response.total_interest:,.2f}")
```

## 📚 API Examples

### Compound Interest Calculation

```python
from xfinance_sdk import XFinanceClient
from xfinance_sdk.models.request import CompoundInterestRequest
from decimal import Decimal

client = XFinanceClient(api_key="your-api-key")

request = CompoundInterestRequest(
    principal=Decimal("10000"),
    annual_rate=Decimal("0.05"),
    years=10,
    compounding_frequency=12
)

response = client.calculate_compound_interest(request)
```

### Loan Payment Calculation

```python
from xfinance_sdk.models.request import LoanCalculationRequest

request = LoanCalculationRequest(
    loan_amount=Decimal("200000"),
    annual_rate=Decimal("0.035"),
    term_years=30
)

response = client.calculate_loan_payment(request)
```

### Investment Returns Calculation

```python
from xfinance_sdk.models.request import InvestmentReturnsRequest

request = InvestmentReturnsRequest(
    initial_investment=Decimal("5000"),
    monthly_contribution=Decimal("500"),
    expected_annual_return=Decimal("0.07"),
    years=20
)

response = client.calculate_investment_returns(request)
```

### Async Usage

```python
import asyncio
from xfinance_sdk import AsyncXFinanceClient

async def main():
    client = AsyncXFinanceClient(api_key="your-api-key")
    response = await client.calculate_compound_interest(request)
    await client.close()

asyncio.run(main())
```

## 🔐 Authentication

### API Key Authentication

```python
client = XFinanceClient(
    api_key="your-api-key",
    api_secret="your-api-secret"  # Optional
)
```

### User Authentication

```python
from xfinance_sdk.models.request import LoginRequest

# Login to get JWT token
login_request = LoginRequest(
    email="user@example.com",
    password="your-password"
)

login_response = client.login(login_request)

# Use token for authenticated requests
authenticated_client = XFinanceClient(api_key=login_response.token)
```

## ⚠️ Error Handling

```python
from xfinance_sdk.exceptions import (
    BadRequestError, UnauthorizedError, RateLimitError, ValidationError
)

try:
    response = client.calculate_compound_interest(request)
except UnauthorizedError as e:
    print(f"Authentication failed: {e.message}")
except BadRequestError as e:
    print(f"Invalid request: {e.message}")
except ValidationError as e:
    print(f"Validation errors: {e.errors}")
except RateLimitError as e:
    print(f"Rate limit exceeded: {e.message}")
```

## ⚙️ Configuration

### Environment Variables

```bash
export XFINANCE_API_KEY="your-api-key"
export XFINANCE_API_SECRET="your-api-secret"
export XFINANCE_API_URL="https://localhost:8087/api/v1"
export XFINANCE_TIMEOUT=30
export XFINANCE_MAX_RETRIES=3
```

### Programmatic Configuration

```python
from xfinance_sdk import XFinanceClient, Settings
from xfinance_sdk.config.retry_config import RetryConfig

# Using Settings class
settings = Settings(
    api_key="your-api-key",
    timeout=45,
    max_retries=4
)

client = XFinanceClient(settings=settings)

# Custom retry configuration
retry_config = RetryConfig(
    max_retries=5,
    backoff_factor=1.0,
    status_forcelist=(429, 500, 502, 503, 504)
)

client = XFinanceClient(api_key="your-api-key", retry_config=retry_config)
```

## 📖 Documentation

Full documentation is available at [https://xfinance.github.io/xfinance-python-sdk/](https://xfinance.github.io/xfinance-python-sdk/)

- [Getting Started Guide](https://xfinance.github.io/xfinance-python-sdk/getting-started/)
- [API Reference](https://xfinance.github.io/xfinance-python-sdk/api-reference/)
- [Examples & Tutorials](https://xfinance.github.io/xfinance-python-sdk/examples/)
- [Advanced Usage](https://xfinance.github.io/xfinance-python-sdk/advanced/)

## 🔧 Development

### Installation from Source

```bash
git clone https://github.com/martourez21/xfinance-python-sdk.git
cd xfinance-python-sdk
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=xfinance_sdk --cov-report=html

# Run specific test file
pytest tests/test_client.py
```

### Code Quality

```bash
# Format code
black xfinance_sdk tests

# Lint code
flake8 xfinance_sdk tests

# Type checking
mypy xfinance_sdk
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](https://github.com/martourez21/xfinance-python-sdk/blob/main/CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow [PEP 8](https://pep8.org/) style guidelines
- Write comprehensive tests for new features
- Update documentation for API changes
- Ensure all CI checks pass

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/martourez21/xfinance-python-sdk/blob/main/LICENSE) file for details.

## 🆘 Support

- 📧 **Email**: [nestorabiawuh@gmail.com](mailto:nestorabiawuh@gmail.com)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/martourez21/xfinance-python-sdk/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/martourez21/xfinance-python-sdk/discussions)
- 📚 **Documentation**: [Official Docs](https://xfinance.github.io/xfinance-python-sdk/)

## 📋 Requirements

- Python 3.8+
- requests >= 2.25.0
- pydantic >= 1.8.0
- typing-extensions >= 4.0.0 (for Python < 3.10)

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/martourez21/xfinance-python-sdk?style=social)
![GitHub forks](https://img.shields.io/github/forks/martourez21/xfinance-python-sdk?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/martourez21/xfinance-python-sdk?style=social)

## 📝 Changelog

See [CHANGELOG.md](https://github.com/martourez21/xfinance-python-sdk/blob/main/CHANGELOG.md) for a history of changes.

## 🙏 Acknowledgments

- Thanks to all our [contributors](https://github.com/martourez21/xfinance-python-sdk/contributors)
- Inspired by the Python financial computing community
- Built with ❤️ by the Nestor Martourez aka The CodedStreams

## 📞 Contact

For business inquiries or partnerships, please contact us at [Coded Streams](mailto:nestorabiawuh@gmail.com)

---

<div align="center">

**[Website](https://xfinance.github.io/)** • 
**[Documentation](https://xfinance.github.io/xfinance-python-sdk/)** • 
**[PyPI](https://pypi.org/project/xfinance-python-sdk/)** • 
**[GitHub](https://github.com/martourez21/xfinance-python-sdk)**

Made with ❤️ by developers, for developers.

</div>