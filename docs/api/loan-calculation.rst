Loan Calculation API
====================

The Loan Calculation API allows you to calculate monthly loan payments for given amount, rate, and term.

Request Model
-------------

.. autoclass:: xfinance_sdk.models.request.loan_calculation.LoanCalculationRequest
   :members:
   :inherited-members:

Response Model
--------------

.. autoclass:: xfinance_sdk.models.response.loan_calculation.LoanCalculationResponse
   :members:
   :inherited-members:

Usage Example
-------------

.. code-block:: python

   from xfinance_sdk import XFinanceClient, LoanCalculationRequest
   from decimal import Decimal

   client = XFinanceClient(api_key="your-api-key")

   request = LoanCalculationRequest(
       loan_amount=Decimal("200000"),
       annual_rate=Decimal("0.035"),
       term_years=30
   )

   response = client.calculate_loan_payment(request)
   print(f"Monthly payment: ${response.monthly_payment:,.2f}")
   print(f"Total interest: ${response.total_interest:,.2f}")

Error Handling
--------------

The API may raise the following exceptions:

- :class:`xfinance_sdk.exceptions.BadRequestError`: Invalid input parameters
- :class:`xfinance_sdk.exceptions.UnauthorizedError`: Invalid API key
- :class:`xfinance_sdk.exceptions.ValidationError`: Validation failed