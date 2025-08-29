import functools
import logging
import time
from typing import Callable, Any, TypeVar, cast

from exceptions.base import XFinanceError

logger = logging.getLogger(__name__)
T = TypeVar('T')
Func = TypeVar('Func', bound=Callable[..., Any])


def retry(max_retries: int = 3, delay: float = 1.0,
          exceptions: tuple = (XFinanceError,)):
    """Retry decorator for API calls"""

    def decorator(func: Func) -> Func:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            raise last_exception

        return cast(Func, wrapper)

    return decorator


def timeout(timeout_seconds: float):
    """Timeout decorator for function execution"""

    def decorator(func: Func) -> Func:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import signal

            def timeout_handler(signum, frame):
                raise TimeoutError(f"Function {func.__name__} timed out after {timeout_seconds} seconds")

            # Set the timeout signal
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(int(timeout_seconds))

            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)  # Cancel the alarm

            return result

        return cast(Func, wrapper)

    return decorator


def log_execution_time(func: Func) -> Func:
    """Decorator to log function execution time"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            logger.debug(f"{func.__name__} executed in {execution_time:.3f}s")
            return result
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"{func.__name__} failed after {execution_time:.3f}s: {e}")
            raise

    return cast(Func, wrapper)


def validate_api_key(func: Func) -> Func:
    """Decorator to validate API key before making requests"""

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.api_key:
            raise ValueError("API key is required for this operation")
        return func(self, *args, **kwargs)

    return cast(Func, wrapper)