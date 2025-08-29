# X-Finance Python SDK

[![PyPI version](https://badge.fury.io/py/xfinance-sdk.svg)](https://badge.fury.io/py/xfinance-sdk)
[![Python Version](https://img.shields.io/pypi/pyversions/xfinance-sdk.svg)](https://pypi.org/project/xfinance-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/xfinance-python-sdk/badge/?version=latest)](https://xfinance-python-sdk.readthedocs.io/en/latest/?badge=latest)

Official Python SDK for the X-Finance API, providing easy integration for financial calculations including compound interest, loan payments, and investment returns.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Async Support](#async-support)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Compound Interest Calculations** - Calculate compound interest with customizable compounding frequencies
- **Loan Payment Calculations** - Determine monthly payments, total interest, and payment schedules
- **Investment Returns** - Project investment growth with regular contributions
- **Type Safety** - Full type hints and Pydantic model validation
- **Error Handling** - Comprehensive exception handling with detailed error information
- **Async Support** - Optional asyncio support for high-performance applications
- **Logging** - Built-in logging with configurable levels
- **Configuration** - Flexible settings for different environments
- **Data Validation** - Automatic request/response validation with clear error messages

## Requirements

- Python 3.8 or higher
- `requests` >= 2.28.0
- `pydantic` >= 2.0.0
- `typing-extensions` >= 4.0.0

## Installation

### Using pip

```bash
pip install xfinance-sdk
```

### Using pip with optional dependencies

```bash
# For development
pip install xfinance-sdk[dev]

# For async support
pip install xfinance-sdk[async]

# For documentation building
pip install xfinance-sdk[docs]

# Install everything
pip install xfinance-sdk[dev,async,docs]
```

### Using poetry

```bash
poetry add xfinance-sdk
```

### From source

```bash
git clone https://github.com/xfinance/xfinance-python-sdk.git
cd xfinance-python-sdk
pip install -e .
```

## Quick Start

```python
from xfinance_sdk import XFinanceClient, CompoundInterestRequest

# Initialize the client
client = XFinanceClient("your-api-key", "your-api-secret")

# Create a compound interest request
request = CompoundInterestRequest(
    principal=10000.0,
    annual_rate=5.5,
    years=10,
    compounding_frequency=12
)

# Calculate compound interest
try:
    response = client.calculate_compound_interest(request)
    print(f"Final Amount: ${response.final_amount:,.2f}")
    print(f"Total Interest: ${response.total_interest:,.2f}")
except Exception as e:
    print(f"Error: {e}")
```

## Usage Examples

### Compound Interest Calculation

```python
from xfinance_sdk import XFinanceClient, CompoundInterestRequest

client = XFinanceClient("your-api-key", "your-api-secret")

# Calculate compound interest for a $10,000 investment
request = CompoundInterestRequest(
    principal=10000.0,          # $10,000 initial investment
    annual_rate=5.5,            # 5.5% annual interest rate
    years=10,                   # 10 years
    compounding_frequency=12    # Monthly compounding
)

response = client.calculate_compound_interest(request)

print("Investment Summary:")
print(f"Initial Investment: ${response.principal:,.2f}")
print(f"Final Amount: ${response.final_amount:,.2f}")
print(f"Total Interest Earned: ${response.total_interest:,.2f}")
print(f"Effective Annual Rate: {response.effective_annual_rate:.2f}%")
print(f"ROI: {response.roi_percentage:.2f}%")
```

### Loan Payment Calculation

```python
from xfinance_sdk import XFinanceClient, LoanCalculationRequest

client = XFinanceClient("your-api-key", "your-api-secret")

# Calculate payments for a $300,000 mortgage
request = LoanCalculationRequest(
    loan_amount=300000.0,    # $300,000 mortgage
    annual_rate=3.5,         # 3.5% annual interest rate
    term_years=30            # 30-year term
)

response = client.calculate_loan_payment(request)

print("Loan Summary:")
print(f"Loan Amount: ${response.loan_amount:,.2f}")
print(f"Monthly Payment: ${response.monthly_payment:,.2f}")
print(f"Total Interest: ${response.total_interest:,.2f}")
print(f"Total Amount: ${response.total_amount:,.2f}")
print(f"Total Payments: {response.total_payments}")
```

### Investment Returns Calculation

```python
from xfinance_sdk import XFinanceClient, InvestmentReturnsRequest

client = XFinanceClient("your-api-key", "your-api-secret")

# Project investment growth over 20 years
request = InvestmentReturnsRequest(
    initial_investment=5000.0,      # $5,000 initial investment
    monthly_contribution=500.0,     # $500 monthly contribution
    expected_annual_return=7.0,     # 7% expected annual return
    years=20                        # 20-year investment period
)

response = client.calculate_investment_returns(request)

print("Investment Projection:")
print(f"Initial Investment: ${response.initial_investment:,.2f}")
print(f"Monthly Contributions: ${response.monthly_contribution:,.2f}")
print(f"Final Value: ${response.final_value:,.2f}")
print(f"Total Contributions: ${response.total_contributions:,.2f}")
print(f"Total Returns: ${response.total_returns:,.2f}")
print(f"ROI: {response.roi_percentage:.2f}%")
```

## Configuration

### Basic Configuration

```python
from xfinance_sdk import XFinanceClient

# Default configuration (production)
client = XFinanceClient("your-api-key", "your-api-secret")

# Custom base URL
client = XFinanceClient(
    "your-api-key", 
    "your-api-secret", 
    base_url="https://api-staging.xfinance.com/v1"
)
```

### Advanced Configuration

```python
from xfinance_sdk import XFinanceClient
from xfinance_sdk.config import ClientSettings

# Create custom settings
settings = ClientSettings(
    base_url="https://api.xfinance.com/v1",
    timeout=30.0,
    max_retries=3,
    retry_delay=1.0,
    debug_logging=True,
    user_agent="MyApp/1.0.0",
    verify_ssl=True
)

client = XFinanceClient("your-api-key", "your-api-secret", settings=settings)
```

### Environment-Specific Configurations

```python
from xfinance_sdk.config import ClientSettings

# Local development
local_settings = ClientSettings.local_development()
local_client = XFinanceClient("api-key", "api-secret", settings=local_settings)

# Production
prod_settings = ClientSettings.production()
prod_client = XFinanceClient("api-key", "api-secret", settings=prod_settings)
```

### Environment Variables

You can also configure the client using environment variables:

```bash
export XFINANCE_API_KEY="your-api-key"
export XFINANCE_API_SECRET="your-api-secret"
export XFINANCE_BASE_URL="https://api.xfinance.com/v1"
export XFINANCE_DEBUG="true"
```

```python
import os
from xfinance_sdk import XFinanceClient

client = XFinanceClient(
    os.getenv("XFINANCE_API_KEY"),
    os.getenv("XFINANCE_API_SECRET"),
    base_url=os.getenv("XFINANCE_BASE_URL")
)
```

## Error Handling

The SDK provides comprehensive error handling with specific exception types:

```python
from xfinance_sdk import (
    XFinanceClient, 
    XFinanceException, 
    AuthenticationException, 
    ValidationException, 
    NetworkException
)

client = XFinanceClient("your-api-key", "your-api-secret")

try:
    response = client.calculate_compound_interest(request)
    # Process successful response
    
except AuthenticationException as e:
    # Handle authentication errors (401)
    print(f"Authentication failed: {e}")
    
except ValidationException as e:
    # Handle validation errors (400)
    print(f"Invalid request: {e}")
    print(f"Field: {e.details.get('field')}")
    
except NetworkException as e:
    # Handle network/connectivity errors
    print(f"Network error: {e}")
    print(f"Original exception: {e.original_exception}")
    
except XFinanceException as e:
    # Handle other API errors
    print(f"API error: {e}")
    print(f"Error code: {e.error_code}")
    print(f"HTTP status: {e.http_status_code}")
    print(f"Details: {e.details}")
```

### Exception Hierarchy

```
XFinanceException (base)
├── AuthenticationException (401 errors)
├── ValidationException (400 errors)
└── NetworkException (network/timeout errors)
```

### Custom Error Handling

```python
def handle_xfinance_error(func, *args, **kwargs):
    """Decorator for handling X-Finance API errors."""
    try:
        return func(*args, **kwargs)
    except AuthenticationException:
        print("Please check your API credentials")
        raise
    except ValidationException as e:
        print(f"Request validation failed: {e}")
        raise
    except NetworkException:
        print("Network connectivity issue - please try again")
        raise
    except XFinanceException as e:
        print(f"API error occurred: {e}")
        raise

# Usage
@handle_xfinance_error
def calculate_interest():
    return client.calculate_compound_interest(request)
```

## Async Support

The SDK provides optional async support for high-performance applications:

```python
import asyncio
from xfinance_sdk.async_client import AsyncXFinanceClient
from xfinance_sdk import CompoundInterestRequest

async def main():
    async with AsyncXFinanceClient("api-key", "api-secret") as client:
        request = CompoundInterestRequest(
            principal=10000.0,
            annual_rate=5.5,
            years=10,
            compounding_frequency=12
        )
        
        response = await client.calculate_compound_interest(request)
        print(f"Final Amount: ${response.final_amount:,.2f}")

# Run the async function
asyncio.run(main())
```

### Concurrent Calculations

```python
import asyncio
from xfinance_sdk.async_client import AsyncXFinanceClient

async def calculate_multiple_scenarios():
    async with AsyncXFinanceClient("api-key", "api-secret") as client:
        # Create multiple scenarios
        scenarios = [
            CompoundInterestRequest(principal=10000.0, annual_rate=rate, years=10, compounding_frequency=12)
            for rate in [3.0, 4.0, 5.0, 6.0, 7.0]
        ]
        
        # Calculate all scenarios concurrently
        tasks = [client.calculate_compound_interest(scenario) for scenario in scenarios]
        results = await asyncio.gather(*tasks)
        
        # Process results
        for i, result in enumerate(results):
            rate = scenarios[i].annual_rate
            print(f"Rate {rate}%: Final Amount ${result.final_amount:,.2f}")

asyncio.run(calculate_multiple_scenarios())
```

## API Reference

### XFinanceClient

The main client class for interacting with the X-Finance API.

#### Constructor

```python
XFinanceClient(
    api_key: str,
    api_secret: str,
    base_url: Optional[str] = None,
    settings: Optional[ClientSettings] = None
)
```

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `calculate_compound_interest()` | Calculate compound interest | `CompoundInterestRequest` | `CompoundInterestResponse` |
| `calculate_loan_payment()` | Calculate loan payments | `LoanCalculationRequest` | `LoanCalculationResponse` |
| `calculate_investment_returns()` | Calculate investment returns | `InvestmentReturnsRequest` | `InvestmentReturnsResponse` |

### Request Models

All request models are Pydantic models with automatic validation.

#### CompoundInterestRequest

```python
class CompoundInterestRequest(BaseModel):
    principal: float          # > 0
    annual_rate: float       # 0 < x <= 100
    years: int              # >= 1
    compounding_frequency: int  # >= 1
```

**Common compounding frequencies:**
- `1` - Annual
- `2` - Semi-annual  
- `4` - Quarterly
- `12` - Monthly
- `52` - Weekly
- `365` - Daily

#### LoanCalculationRequest

```python
class LoanCalculationRequest(BaseModel):
    loan_amount: float    # > 0
    annual_rate: float   # > 0
    term_years: int     # >= 1
```

#### InvestmentReturnsRequest

```python
class InvestmentReturnsRequest(BaseModel):
    initial_investment: float      # >= 0
    monthly_contribution: float    # >= 0
    expected_annual_return: float  # > 0
    years: int                    # >= 1
```

### Response Models

All response models include computed properties for additional insights.

#### CompoundInterestResponse

```python
class CompoundInterestResponse(BaseModel):
    final_amount: float
    total_interest: float
    principal: float
    annual_rate: float
    years: int
    compounding_frequency: int
    
    # Computed properties
    effective_annual_rate: float  # Effective APR
    roi_percentage: float         # Return on Investment %
```

#### LoanCalculationResponse

```python
class LoanCalculationResponse(BaseModel):
    monthly_payment: float
    total_interest: float
    total_amount: float
    loan_amount: float
    annual_rate: float
    term_years: int
    
    # Computed properties
    total_payments: int          # Total number of payments
    monthly_interest_rate: float # Monthly interest rate
```

#### InvestmentReturnsResponse

```python
class InvestmentReturnsResponse(BaseModel):
    final_value: float
    total_contributions: float
    total_returns: float
    initial_investment: float
    monthly_contribution: float
    expected_annual_return: float
    years: int
    
    # Computed properties
    roi_percentage: float        # Return on Investment %
    annualized_return: float     # Actual annualized return
```

## Logging

The SDK uses Python's built-in logging module. Configure logging to control output:

```python
import logging

# Enable debug logging for the SDK
logging.getLogger('xfinance_sdk').setLevel(logging.DEBUG)

# Configure a handler
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger('xfinance_sdk').addHandler(handler)
```

### Logging Configuration

```python
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'xfinance_sdk': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
```

## Data Validation

The SDK uses Pydantic for automatic data validation:

```python
from xfinance_sdk import CompoundInterestRequest
from pydantic import ValidationError

try:
    # This will raise a ValidationError
    request = CompoundInterestRequest(
        principal=-1000.0,  # Invalid: must be > 0
        annual_rate=150.0,  # Invalid: must be <= 100
        years=0,           # Invalid: must be >= 1
        compounding_frequency=0  # Invalid: must be >= 1
    )
except ValidationError as e:
    print("Validation errors:")
    for error in e.errors():
        field = error['loc'][0]
        message = error['msg']
        value = error['input']
        print(f"  {field}: {message} (got: {value})")
```

## Testing

### Running Tests

```bash
# Install development dependencies
pip install -e .[dev]

# Run all tests
pytest

# Run with coverage
pytest --cov=xfinance_sdk

# Run only unit tests
pytest tests/unit/

# Run only integration tests
pytest tests/integration/
```

### Test Configuration

Set environment variables for integration tests:

```bash
export XFINANCE_API_KEY=your-test-api-key
export XFINANCE_API_SECRET=your-test-api-secret
export XFINANCE_BASE_URL=https://api-staging.xfinance.com/v1
```

### Writing Tests

```python
import pytest
from xfinance_sdk import XFinanceClient, CompoundInterestRequest

@pytest.fixture
def client():
    return XFinanceClient("test-key", "test-secret")

@pytest.fixture
def compound_request():
    return CompoundInterestRequest(
        principal=10000.0,
        annual_rate=5.5,
        years=10,
        compounding_frequency=12
    )

def test_compound_interest_calculation(client, compound_request):
    response = client.calculate_compound_interest(compound_request)
    assert response.final_amount > response.principal
    assert response.total_interest > 0
```

## Performance Tips

1. **Reuse Client Instances**: Create one client instance and reuse it
2. **Use Async for Concurrent Requests**: Use `AsyncXFinanceClient` for multiple concurrent calculations
3. **Enable Connection Pooling**: The underlying `requests` library handles this automatically
4. **Configure Timeouts**: Set appropriate timeout values for your use case
5. **Use Appropriate Retry Settings**: Configure retries based on your reliability requirements

```python
# Good: Reuse client
client = XFinanceClient("api-key", "api-secret")
for scenario in scenarios:
    result = client.calculate_compound_interest(scenario)

# Better: Use async for concurrent requests
async with AsyncXFinanceClient("api-key", "api-secret") as client:
    tasks = [client.calculate_compound_interest(s) for s in scenarios]
    results = await asyncio.gather(*tasks)
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/xfinance/xfinance-python-sdk.git
cd xfinance-python-sdk

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install

# Run tests
pytest
```

### Code Quality

The project uses several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pytest**: Testing

Run all quality checks:

```bash
make lint
make test
make type-check
```

## Support

- **Documentation**: [https://xfinance-python-sdk.readthedocs.io/](https://xfinance-python-sdk.readthedocs.io/)
- **API Documentation**: [https://docs.xfinance.com/](https://docs.xfinance.com/)
- **Issues**: [GitHub Issues](https://github.com/xfinance/xfinance-python-sdk/issues)
- **Email**: support@xfinance.com
- **Discord**: [Join our community](https://discord.gg/xfinance)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes.

## Roadmap

- [ ] WebSocket support for real-time calculations
- [ ] Additional financial calculators (NPV, IRR, etc.)
- [ ] Caching layer for improved performance
- [ ] Advanced retry strategies
- [ ] Metrics and monitoring integration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by the X-Finance Team