"""Mirrors lib/zazu/resources/transfer_drafts.rb.

API-initiated transfers. Creating a draft routes it into the workspace's
in-app approval flow — the API never executes a transfer itself. Poll
``get`` (status: requested → processing → completed / failed) or
subscribe to the ``transfer.executed`` webhook.
"""

from __future__ import annotations

from typing import Any

from ..response import ZazuResponse
from .base import ResourceBase


class TransferDrafts(ResourceBase):
    def create(self, **attributes: Any) -> ZazuResponse:
        return self.http_post("api/transfer_drafts", body=attributes)

    def get(self, id: str) -> ZazuResponse:
        return self.http_get(self.encode_path("api/transfer_drafts", id))
