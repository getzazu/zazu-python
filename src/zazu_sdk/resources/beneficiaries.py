"""Mirrors lib/zazu/resources/beneficiaries.rb.

Read-only directory of saved transfer recipients. Each beneficiary
embeds its bank accounts; the one flagged ``default`` is used when a
transfer names only the beneficiary_id. Beneficiaries are created and
managed in the Zazu dashboard.
"""

from __future__ import annotations

from typing import Any

from ..page import MAX_PER_PAGE, Page
from ..response import ZazuResponse
from .base import ResourceBase


class Beneficiaries(ResourceBase):
    def list(self, *, limit: int = MAX_PER_PAGE, cursor: str | None = None) -> Page[Any]:
        return self.list_page("api/beneficiaries", {}, limit=limit, cursor=cursor)

    def get(self, id: str) -> ZazuResponse:
        return self.http_get(self.encode_path("api/beneficiaries", id))
