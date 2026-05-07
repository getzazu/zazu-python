"""Mirrors lib/zazu/resources/entity.rb."""

from __future__ import annotations

from ..response import ZazuResponse
from .base import ResourceBase


class Entity(ResourceBase):
    def get(self) -> ZazuResponse:
        return self.http_get("api/entity")
