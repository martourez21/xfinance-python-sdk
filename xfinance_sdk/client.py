from typing import Optional, List, Dict, Any

from exceptions.base import ValidationError
from models.request.api_key import ApiKeyRequest
from models.request.auth import LoginRequest, UserRegistrationRequest
from models.request.compound_interest import CompoundInterestRequest
from models.request.investment_returns import InvestmentReturnsRequest
from models.request.loan_calculation import LoanCalculationRequest
from models.response.api_key import ApiKeyResponse
from models.response.auth import LoginResponse, UserResponse
from models.response.compound_interest import CompoundInterestResponse
from models.response.investment_returns import InvestmentReturnsResponse
from models.response.loan_calculation import LoanCalculationResponse
from models.response.plan import PlanResponse
from services.auth_service import AuthService
from services.http_service import HttpService
from services.validation_service import ValidationService
from utils.decorators import log_execution_time, retry, validate_api_key
from .config.settings import Settings



class XFinanceClient:
    def __init__(self, api_key: Optional[str] = None, 
                 api_secret: Optional[str] = None,
                 base_url: Optional[str] = None,
                 settings: Optional[Settings] = None):
        self.settings = settings or Settings()
        self.api_key = api_key or self.settings.api_key
        self.api_secret = api_secret or self.settings.api_secret
        self.base_url = base_url or self.settings.api_base_url
        
        self.http_service = HttpService(
            base_url=self.base_url,
            api_key=self.api_key,
            api_secret=self.api_secret
        )
        self.auth_service = AuthService(self.http_service)
        self.validation_service = ValidationService()
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    @validate_api_key
    def calculate_compound_interest(self, request: CompoundInterestRequest) -> CompoundInterestResponse:
        """Calculate compound interest"""
        response = self.http_service.post('/api/v1/finance/compound-interest', request.dict())
        return CompoundInterestResponse(**response['data'])
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    @validate_api_key
    def calculate_loan_payment(self, request: LoanCalculationRequest) -> LoanCalculationResponse:
        """Calculate loan payment"""
        response = self.http_service.post('/api/v1/finance/loan-calculation', request.dict())
        return LoanCalculationResponse(**response['data'])
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    @validate_api_key
    def calculate_investment_returns(self, request: InvestmentReturnsRequest) -> InvestmentReturnsResponse:
        """Calculate investment returns"""
        response = self.http_service.post('/api/v1/finance/investment-returns', request.dict())
        return InvestmentReturnsResponse(**response['data'])
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    @validate_api_key
    def generate_api_key(self, request: ApiKeyRequest) -> ApiKeyResponse:
        """Generate a new API key"""
        response = self.http_service.post('/api/v1/keys/generate', request.dict())
        return ApiKeyResponse(**response['data'])
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    @validate_api_key
    def list_api_keys(self) -> List[ApiKeyResponse]:
        """List all API keys for the authenticated user"""
        response = self.http_service.get('/api/v1/keys/list')
        return [ApiKeyResponse(**key_data) for key_data in response['data']]
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    def register_user(self, request: UserRegistrationRequest) -> UserResponse:
        """Register a new user"""
        return self.auth_service.register(request)
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    def login(self, request: LoginRequest) -> LoginResponse:
        """Login user and get JWT token"""
        return self.auth_service.login(request)
    
    @retry(max_retries=3, delay=1.0)
    @log_execution_time
    def get_plans(self) -> List[PlanResponse]:
        """Get all available subscription plans"""
        response = self.http_service.get('/api/v1/plans')
        return [PlanResponse(**plan_data) for plan_data in response['data']]
    
    def validate_request(self, request_data: Dict[str, Any], request_type: str) -> Any:
        """Validate request data against specific request type"""
        if request_type == 'compound_interest':
            return self.validation_service.validate_compound_interest(request_data)
        elif request_type == 'loan_calculation':
            return self.validation_service.validate_loan_calculation(request_data)
        elif request_type == 'investment_returns':
            return self.validation_service.validate_investment_returns(request_data)
        elif request_type == 'api_key':
            return self.validation_service.validate_api_key_request(request_data)
        else:
            raise ValidationError(f"Unknown request type: {request_type}")
    
    def close(self):
        """Close the HTTP session"""
        self.http_service.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class AsyncXFinanceClient:
    """Async version of the XFinance client"""
    
    def __init__(self, api_key: Optional[str] = None, 
                 api_secret: Optional[str] = None,
                 base_url: Optional[str] = None):
        self.settings = Settings()
        self.api_key = api_key or self.settings.api_key
        self.api_secret = api_secret or self.settings.api_secret
        self.base_url = base_url or self.settings.api_base_url
        self.http_service = HttpService(
            base_url=self.base_url,
            api_key=self.api_key,
            api_secret=self.api_secret
        )
    
    async def calculate_compound_interest(self, request: CompoundInterestRequest) -> CompoundInterestResponse:
        """Async calculate compound interest"""
        response = await self.http_service.async_request('POST', '/api/v1/finance/compound-interest', request.dict())
        return CompoundInterestResponse(**response['data'])
    
    async def calculate_loan_payment(self, request: LoanCalculationRequest) -> LoanCalculationResponse:
        """Async calculate loan payment"""
        response = await self.http_service.async_request('POST', '/api/v1/finance/loan-calculation', request.dict())
        return LoanCalculationResponse(**response['data'])
    
    async def calculate_investment_returns(self, request: InvestmentReturnsRequest) -> InvestmentReturnsResponse:
        """Async calculate investment returns"""
        response = await self.http_service.async_request('POST', '/api/v1/finance/investment-returns', request.dict())
        return InvestmentReturnsResponse(**response['data'])
    
    async def close(self):
        """Close async resources"""
        pass