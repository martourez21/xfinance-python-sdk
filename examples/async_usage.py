#!/usr/bin/env python3
"""
Async usage example for xfinance Python SDK
"""

import asyncio
import os
from decimal import Decimal

from models.request.compound_interest import CompoundInterestRequest
from models.request.investment_returns import InvestmentReturnsRequest
from models.request.loan_calculation import LoanCalculationRequest
from xfinance_sdk.client import AsyncXFinanceClient


async def main():
    # Initialize async client
    api_key = os.getenv("XFINANCE_API_KEY")
    if not api_key:
        print("Please set XFINANCE_API_KEY environment variable")
        return

    client = AsyncXFinanceClient(api_key=api_key)

    print("=== Async Compound Interest Calculation ===")
    try:
        ci_request = CompoundInterestRequest(
            principal=Decimal("10000"),
            annual_rate=Decimal("0.05"),
            years=10,
            compounding_frequency=12
        )
        ci_response = await client.calculate_compound_interest(ci_request)
        print(f"Final Amount: ${ci_response.final_amount:,.2f}")
        print()
    except Exception as e:
        print(f"Compound interest calculation failed: {e}")

    print("=== Async Loan Calculation ===")
    try:
        loan_request = LoanCalculationRequest(
            loan_amount=Decimal("200000"),
            annual_rate=Decimal("0.035"),
            term_years=30
        )
        loan_response = await client.calculate_loan_payment(loan_request)
        print(f"Monthly Payment: ${loan_response.monthly_payment:,.2f}")
        print()
    except Exception as e:
        print(f"Loan calculation failed: {e}")

    print("=== Async Investment Returns Calculation ===")
    try:
        investment_request = InvestmentReturnsRequest(
            initial_investment=Decimal("5000"),
            monthly_contribution=Decimal("500"),
            expected_annual_return=Decimal("0.07"),
            years=20
        )
        investment_response = await client.calculate_investment_returns(investment_request)
        print(f"Final Value: ${investment_response.final_value:,.2f}")
        print()
    except Exception as e:
        print(f"Investment calculation failed: {e}")

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())