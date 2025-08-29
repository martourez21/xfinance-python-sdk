from dataclasses import dataclass


@dataclass
class RetryConfig:
    max_retries: int = 3
    backoff_factor: float = 0.5
    status_forcelist: tuple = (429, 500, 502, 503, 504)
    allowed_methods: tuple = ("GET", "POST", "PUT", "DELETE")
    respect_retry_after_header: bool = True