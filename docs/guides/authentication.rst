Authentication
==============

The xfinance SDK supports multiple authentication methods.

API Key Authentication
----------------------

The primary authentication method is using API keys:

.. code-block:: python

   from xfinance_sdk import XFinanceClient

   client = XFinanceClient(
       api_key="your-api-key",
       api_secret="your-api-secret"  # Optional for some endpoints
   )

Generating API Keys
-------------------

You can generate API keys through the API:

.. code-block:: python

   from xfinance_sdk.models.request import ApiKeyRequest

   # First, authenticate with user credentials
   from xfinance_sdk.models.request import LoginRequest

   login_request = LoginRequest(
       email="user@example.com",
       password="your-password"
   )

   login_response = client.login(login_request)

   # Use the token for authenticated requests
   client_with_token = XFinanceClient(api_key=login_response.token)

   # Generate a new API key
   api_key_request = ApiKeyRequest(
       key_name="my-production-key",
       description="Key for production environment"
   )

   api_key_response = client_with_token.generate_api_key(api_key_request)
   print(f"API Key ID: {api_key_response.key_id}")
   print(f"API Key Secret: {api_key_response.key_secret}")  # Save this securely!

Listing API Keys
----------------

.. code-block:: python

   api_keys = client_with_token.list_api_keys()
   for key in api_keys:
       print(f"Key: {key.key_name}, Status: {key.status}")

JWT Token Authentication
------------------------

For user-level operations, you can use JWT tokens:

.. code-block:: python

   from xfinance_sdk import XFinanceClient
   from xfinance_sdk.models.request import LoginRequest

   client = XFinanceClient()

   login_request = LoginRequest(
       email="user@example.com",
       password="your-password"
   )

   login_response = client.login(login_request)

   # Use the token for subsequent requests
   authenticated_client = XFinanceClient(api_key=login_response.token)

Error Handling
--------------

Authentication errors may include:

- :class:`xfinance_sdk.exceptions.UnauthorizedError`: Invalid credentials
- :class:`xfinance_sdk.exceptions.ForbiddenError`: Insufficient permissions
- :class:`xfinance_sdk.exceptions.ExpiredApiKeyError`: Expired API key