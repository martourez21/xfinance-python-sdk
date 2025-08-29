#!/usr/bin/env python3
"""
Basic usage example for xfinance Python SDK
"""

import os
from decimal import Decimal

from models.request.compound_interest import CompoundInterestRequest
from models.request.investment_returns import InvestmentReturnsRequest
from models.request.loan_calculation import LoanCalculationRequest
from xfinance_sdk import XFinanceClient, __all__


def main():
    # Initialize client with API key from environment variable
    api_key = os.getenv("XFINANCE_API_KEY")
    if not api_key:
        print("Please set XFINANCE_API_KEY environment variable")
        return

    client = XFinanceClient(api_key=api_key)

    print("=== Compound Interest Calculation ===")
    try:
        ci_request = CompoundInterestRequest(
            principal=Decimal("10000"),
            annual_rate=Decimal("0.05"),
            years=10,
            compounding_frequency=12
        )
        ci_response = client.calculate_compound_interest(ci_request)
        print(f"Principal: ${ci_response.principal:,.2f}")
        print(f"Annual Rate: {ci_response.annual_rate:.2%}")
        print(f"Years: {ci_response.years}")
        print(f"Final Amount: ${ci_response.final_amount:,.2f}")
        print(f"Total Interest: ${ci_response.total_interest:,.2f}")
        print()
    except Exception as e:
        print(f"Compound interest calculation failed: {e}")

    print("=== Loan Calculation ===")
    try:
        loan_request = LoanCalculationRequest(
            loan_amount=Decimal("200000"),
            annual_rate=Decimal("0.035"),
            term_years=30
        )
        loan_response = client.calculate_loan_payment(loan_request)
        print(f"Loan Amount: ${loan_response.loan_amount:,.2f}")
        print(f"Annual Rate: {loan_response.annual_rate:.2%}")
        print(f"Term: {loan_response.term_years} years")
        print(f"Monthly Payment: ${loan_response.monthly_payment:,.2f}")
        print(f"Total Interest: ${loan_response.total_interest:,.2f}")
        print(f"Total Amount: ${loan_response.total_amount:,.2f}")
        print()
    except Exception as e:
        print(f"Loan calculation failed: {e}")

    print("=== Investment Returns Calculation ===")
    try:
        investment_request = InvestmentReturnsRequest(
            initial_investment=Decimal("5000"),
            monthly_contribution=Decimal("500"),
            expected_annual_return=Decimal("0.07"),
            years=20
        )
        investment_response = client.calculate_investment_returns(investment_request)
        print(f"Initial Investment: ${investment_response.initial_investment:,.2f}")
        print(f"Monthly Contribution: ${investment_response.monthly_contribution:,.2f}")
        print(f"Expected Annual Return: {investment_response.expected_annual_return:.2%}")
        print(f"Years: {investment_response.years}")
        print(f"Final Value: ${investment_response.final_value:,.2f}")
        print(f"Total Contributions: ${investment_response.total_contributions:,.2f}")
        print(f"Total Returns: ${investment_response.total_returns:,.2f}")
        print()
    except Exception as e:
        print(f"Investment calculation failed: {e}")

    client.close()


if __name__ == "__main__":
    main()