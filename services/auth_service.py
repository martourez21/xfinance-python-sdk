from ..models.request.auth import UserRegistrationRequest, LoginRequest
from ..models.response.auth import LoginResponse, UserResponse
from ..services.http_service import HttpService


class AuthService:
    def __init__(self, http_service: HttpService):
        self.http_service = http_service

    def register(self, request: UserRegistrationRequest) -> UserResponse:
        """Register a new user"""
        response = self.http_service.post('/api/v1/auth/register', request.dict())
        return UserResponse(**response['data'])

    def login(self, request: LoginRequest) -> LoginResponse:
        """Login user and get JWT token"""
        response = self.http_service.post('/api/v1/auth/login', request.dict())
        return LoginResponse(**response['data'])

    def validate_token(self, token: str) -> bool:
        """Validate JWT token"""
        try:
            # This would typically call a token validation endpoint
            # For now, we'll assume basic validation
            headers = {'Authorization': f'Bearer {token}'}
            # Store original headers and restore after
            original_headers = self.http_service._get_headers()
            self.http_service.session.headers.update(headers)

            # Make a simple request to validate token
            response = self.http_service.get('/api/v1/auth/validate')

            # Restore original headers
            self.http_service.session.headers.update(original_headers)

            return response.get('valid', False)
        except Exception:
            return False