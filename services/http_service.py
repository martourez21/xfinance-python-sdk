import logging
from typing import Dict, Any, Optional, TypeVar

import aiohttp
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from exceptions.base import APIError, ServerError, BadRequestError, UnauthorizedError, ForbiddenError, NotFoundError, \
    RateLimitError
from exceptions.network import NetworkError
from xfinance_sdk.config.retry_config import RetryConfig

logger = logging.getLogger(__name__)
T = TypeVar('T')


class HttpService:
    def __init__(self, base_url: str, api_key: Optional[str] = None,
                 api_secret: Optional[str] = None, retry_config: Optional[RetryConfig] = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.api_secret = api_secret
        self.retry_config = retry_config or RetryConfig()

        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        session = requests.Session()

        # Configure retries
        retry_strategy = Retry(
            total=self.retry_config.max_retries,
            backoff_factor=self.retry_config.backoff_factor,
            status_forcelist=self.retry_config.status_forcelist,
            allowed_methods=self.retry_config.allowed_methods,
            respect_retry_after_header=self.retry_config.respect_retry_after_header
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def _get_headers(self) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "xfinance-python-sdk/1.0.0"
        }

        if self.api_key:
            headers["X-API-Key"] = self.api_key
        if self.api_secret:
            headers["X-API-Secret"] = self.api_secret

        return headers

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            self._handle_http_error(response, e)
        except requests.exceptions.JSONDecodeError:
            raise ServerError("Invalid JSON response from server", response.status_code)
        except Exception as e:
            raise NetworkError(f"Network error: {str(e)}")

    def _handle_http_error(self, response: requests.Response, original_error: Exception):
        status_code = response.status_code

        try:
            error_data = response.json()
            message = error_data.get('message', 'Unknown error')
        except:
            message = response.text or 'Unknown error'

        if status_code == 400:
            raise BadRequestError(message, status_code)
        elif status_code == 401:
            raise UnauthorizedError(message, status_code)
        elif status_code == 403:
            raise ForbiddenError(message, status_code)
        elif status_code == 404:
            raise NotFoundError(message, status_code)
        elif status_code == 429:
            raise RateLimitError(message, status_code)
        elif 500 <= status_code < 600:
            raise ServerError(message, status_code)
        else:
            raise APIError(message, status_code)

    def request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None,
                params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=self._get_headers(),
                timeout=self.retry_config.timeout if hasattr(self.retry_config, 'timeout') else 30
            )
            return self._handle_response(response)
        except requests.exceptions.Timeout:
            raise TimeoutError("Request timed out")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("Connection error")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {str(e)}")

    async def async_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None,
                            params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = self._get_headers()

        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(
                        method=method,
                        url=url,
                        json=data,
                        params=params,
                        headers=headers,
                        timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientError as e:
            raise NetworkError(f"Network error: {str(e)}")

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.request('GET', endpoint, params=params)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.request('POST', endpoint, data=data)

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return self.request('PUT', endpoint, data=data)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        return self.request('DELETE', endpoint)

    def close(self):
        self.session.close()