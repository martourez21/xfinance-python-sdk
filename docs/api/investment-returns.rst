Investment Returns API
======================

The Investment Returns API allows you to calculate future value of investment with regular contributions.

Request Model
-------------

.. autoclass:: xfinance_sdk.models.request.investment_returns.InvestmentReturnsRequest
   :members:
   :inherited-members:

Response Model
--------------

.. autoclass:: xfinance_sdk.models.response.investment_returns.InvestmentReturnsResponse
   :members:
   :inherited-members:

Usage Example
-------------

.. code-block:: python

   from xfinance_sdk import XFinanceClient, InvestmentReturnsRequest
   from decimal import Decimal

   client = XFinanceClient(api_key="your-api-key")

   request = InvestmentReturnsRequest(
       initial_investment=Decimal("5000"),
       monthly_contribution=Decimal("500"),
       expected_annual_return=Decimal("0.07"),
       years=20
   )

   response = client.calculate_investment_returns(request)
   print(f"Final value: ${response.final_value:,.2f}")
   print(f"Total contributions: ${response.total_contributions:,.2f}")
   print(f"Total returns: ${response.total_returns:,.2f}")

Error Handling
--------------

The API may raise the following exceptions:

- :class:`xfinance_sdk.exceptions.BadRequestError`: Invalid input parameters
- :class:`xfinance_sdk.exceptions.UnauthorizedError`: Invalid API key
- :class:`xfinance_sdk.exceptions.ValidationError`: Validation failed