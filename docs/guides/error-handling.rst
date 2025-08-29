Error Handling
==============

The xfinance SDK provides comprehensive error handling.

Exception Hierarchy
-------------------

.. code-block:: text

   XFinanceError
   ├── APIError
   │   ├── BadRequestError (400)
   │   ├── UnauthorizedError (401)
   │   ├── ForbiddenError (403)
   │   ├── NotFoundError (404)
   │   ├── RateLimitError (429)
   │   └── ServerError (5xx)
   ├── ValidationError
   │   └── RequestValidationError
   ├── AuthenticationError
   │   ├── InvalidApiKeyError
   │   └── ExpiredApiKeyError
   └── NetworkError
       ├── TimeoutError
       └── ConnectionError

Handling Exceptions
-------------------

.. code-block:: python

   from xfinance_sdk import XFinanceClient
   from xfinance_sdk.exceptions import (
       BadRequestError, UnauthorizedError, RateLimitError, ValidationError
   )

   try:
       response = client.calculate_compound_interest(request)
   except BadRequestError as e:
       print(f"Invalid request: {e.message}")
   except UnauthorizedError as e:
       print(f"Authentication failed: {e.message}")
   except RateLimitError as e:
       print(f"Rate limit exceeded: {e.message}")
   except ValidationError as e:
       print(f"Validation failed: {e.message}")
       if hasattr(e, 'errors'):
           for field, errors in e.errors.items():
               print(f"{field}: {', '.join(errors)}")
   except Exception as e:
       print(f"Unexpected error: {e}")

Validation Errors
-----------------

Validation errors provide detailed field-level information:

.. code-block:: python

   from xfinance_sdk.exceptions import RequestValidationError

   try:
       request = CompoundInterestRequest(
           principal=Decimal("-100"),  # Invalid negative value
           annual_rate=Decimal("0.05"),
           years=10,
           compounding_frequency=12
       )
   except RequestValidationError as e:
       print(f"Validation failed: {e.message}")
       for field, errors in e.errors.items():
           print(f"{field}: {errors}")

Retry Mechanism
---------------

The SDK includes automatic retry for transient errors:

.. code-block:: python

   from xfinance_sdk import XFinanceClient
   from xfinance_sdk.utils.decorators import retry

   @retry(max_retries=3, delay=2.0)
   def make_api_call():
       return client.calculate_compound_interest(request)

   try:
       response = make_api_call()
   except Exception as e:
       print(f"All retry attempts failed: {e}")

Custom Error Handling
---------------------

You can create custom error handlers:

.. code-block:: python

   def handle_api_error(func):
       def wrapper(*args, **kwargs):
           try:
               return func(*args, **kwargs)
           except Exception as e:
               # Log error, send to monitoring, etc.
               logger.error(f"API call failed: {e}")
               raise
       return wrapper

   @handle_api_error
   def safe_api_call():
       return client.calculate_compound_interest(request)