from decimal import Decimal

from pydantic import BaseModel, Field, validator


class CompoundInterestRequest(BaseModel):
    principal: Decimal = Field(..., gt=0, description="Principal amount")
    annual_rate: Decimal = Field(..., ge=0, description="Annual interest rate")
    years: int = Field(..., ge=1, description="Number of years")
    compounding_frequency: int = Field(..., ge=1, description="Compounding frequency per year")

    @validator('principal', 'annual_rate')
    def validate_decimal_values(cls, v):
        return round(v, 6)