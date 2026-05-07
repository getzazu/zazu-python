"""Mirrors lib/zazu/errors.rb. Nine-class hierarchy shared across SDKs."""

from __future__ import annotations

from typing import Any


class ZazuError(Exception):
    """Base class for every error raised by the SDK."""

    def __init__(
        self,
        message: str,
        *,
        status: int | None = None,
        request_id: str | None = None,
        type: str | None = None,
        param: str | None = None,
        body: Any = None,
        headers: Any = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status = status
        self.request_id = request_id
        self.type = type
        self.param = param
        self.body = body
        self.headers = headers


class ZazuArgumentError(ZazuError):
    """Caller passed bad arguments before any HTTP request was made."""


class ZazuConfigurationError(ZazuError):
    """Missing or invalid client configuration (e.g. no API key)."""


class ZazuConnectionError(ZazuError):
    """The HTTP request failed before getting a response (timeout, DNS, refused)."""


class ZazuAuthenticationError(ZazuError):
    """HTTP 401."""


class ZazuForbiddenError(ZazuError):
    """HTTP 403."""


class ZazuNotFoundError(ZazuError):
    """HTTP 404."""


class ZazuValidationError(ZazuError):
    """HTTP 422."""


class ZazuRateLimitError(ZazuError):
    """HTTP 429. `retry_after` is the value of the Retry-After header in seconds, if present."""

    def __init__(self, message: str, *, retry_after: int | None = None, **kwargs: Any) -> None:
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class ZazuServerError(ZazuError):
    """HTTP 5xx."""
