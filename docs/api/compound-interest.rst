Compound Interest API
=====================

The Compound Interest API allows you to calculate compound interest for given principal, rate, and time period.

Request Model
-------------

.. autoclass:: xfinance_sdk.models.request.compound_interest.CompoundInterestRequest
   :members:
   :inherited-members:

Response Model
--------------

.. autoclass:: xfinance_sdk.models.response.compound_interest.CompoundInterestResponse
   :members:
   :inherited-members:

Usage Example
-------------

.. code-block:: python

   from xfinance_sdk import XFinanceClient, CompoundInterestRequest
   from decimal import Decimal

   client = XFinanceClient(api_key="your-api-key")

   request = CompoundInterestRequest(
       principal=Decimal("10000"),
       annual_rate=Decimal("0.05"),
       years=10,
       compounding_frequency=12
   )

   response = client.calculate_compound_interest(request)
   print(f"Final amount: ${response.final_amount:,.2f}")
   print(f"Total interest: ${response.total_interest:,.2f}")

Error Handling
--------------

The API may raise the following exceptions:

- :class:`xfinance_sdk.exceptions.BadRequestError`: Invalid input parameters
- :class:`xfinance_sdk.exceptions.UnauthorizedError`: Invalid API key
- :class:`xfinance_sdk.exceptions.ValidationError`: Validation failed