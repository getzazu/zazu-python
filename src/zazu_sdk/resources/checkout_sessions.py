"""Mirrors lib/zazu/resources/checkout_sessions.rb."""

from __future__ import annotations

from typing import Any

from ..response import ZazuResponse
from .base import ResourceBase


class CheckoutSessions(ResourceBase):
    def get(self, id: str) -> ZazuResponse:
        return self.http_get(self.encode_path("api/checkout_sessions", id))

    def create(self, **attributes: Any) -> ZazuResponse:
        return self.http_post("api/checkout_sessions", body=attributes)
