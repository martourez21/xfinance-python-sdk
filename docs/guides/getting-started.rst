Getting Started
===============

This guide will help you get started with the xfinance Python SDK.

Installation
------------

You can install the SDK using pip:

.. code-block:: bash

   pip install xfinance-python-sdk

Or from source:

.. code-block:: bash

   git clone https://github.com/xfinance/xfinance-python-sdk.git
   cd xfinance-python-sdk
   pip install -e .

Basic Usage
-----------

First, import the SDK and create a client:

.. code-block:: python

   from xfinance_sdk import XFinanceClient

   # Initialize with API key
   client = XFinanceClient(api_key="your-api-key")

Make your first API call:

.. code-block:: python

   from decimal import Decimal
   from xfinance_sdk.models.request import CompoundInterestRequest

   request = CompoundInterestRequest(
       principal=Decimal("10000"),
       annual_rate=Decimal("0.05"),
       years=10,
       compounding_frequency=12
   )

   response = client.calculate_compound_interest(request)
   print(f"Final amount: ${response.final_amount:,.2f}")

Configuration
-------------

You can configure the client using environment variables:

.. code-block:: bash

   export XFINANCE_API_KEY="your-api-key"
   export XFINANCE_API_SECRET="your-api-secret"
   export XFINANCE_API_URL="https://api.xfinance.com"
   export XFINANCE_TIMEOUT=30
   export XFINANCE_MAX_RETRIES=3

Or programmatically:

.. code-block:: python

   from xfinance_sdk import XFinanceClient, Settings

   settings = Settings(
       api_key="your-api-key",
       api_secret="your-api-secret",
       timeout=30,
       max_retries=3
   )

   client = XFinanceClient(settings=settings)

Next Steps
----------

- Learn about :doc:`authentication`
- Explore :doc:`configuration` options
- Understand :doc:`error-handling`