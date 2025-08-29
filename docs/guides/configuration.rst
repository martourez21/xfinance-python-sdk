Configuration
=============

The xfinance SDK provides flexible configuration options.

Environment Variables
---------------------

You can configure the SDK using environment variables:

.. list-table:: Environment Variables
   :header-rows: 1

   * - Variable
     - Description
     - Default
   * - ``XFINANCE_API_KEY``
     - Your API key
     - ``None``
   * - ``XFINANCE_API_SECRET``
     - Your API secret
     - ``None``
   * - ``XFINANCE_API_URL``
     - API base URL
     - ``https://api.xfinance.com``
   * - ``XFINANCE_TIMEOUT``
     - Request timeout in seconds
     - ``30``
   * - ``XFINANCE_MAX_RETRIES``
     - Maximum retry attempts
     - ``3``

Programmatic Configuration
--------------------------

You can configure the client programmatically:

.. code-block:: python

   from xfinance_sdk import XFinanceClient, Settings

   settings = Settings(
       api_key="your-api-key",
       api_secret="your-api-secret",
       api_base_url="https://api.xfinance.com",
       timeout=30,
       max_retries=3
   )

   client = XFinanceClient(settings=settings)

Or directly:

.. code-block:: python

   client = XFinanceClient(
       api_key="your-api-key",
       api_secret="your-api-secret",
       base_url="https://api.xfinance.com"
   )

Retry Configuration
-------------------

You can customize retry behavior:

.. code-block:: python

   from xfinance_sdk.config.retry_config import RetryConfig
   from xfinance_sdk import XFinanceClient

   retry_config = RetryConfig(
       max_retries=5,
       backoff_factor=1.0,
       status_forcelist=(429, 500, 502, 503, 504)
   )

   client = XFinanceClient(
       api_key="your-api-key",
       retry_config=retry_config
   )

Timeout Configuration
---------------------

.. code-block:: python

   from xfinance_sdk import XFinanceClient

   # Global timeout
   client = XFinanceClient(api_key="your-api-key", timeout=60)

   # Per-request timeout (using context manager)
   with XFinanceClient(api_key="your-api-key") as client:
       response = client.calculate_compound_interest(request)