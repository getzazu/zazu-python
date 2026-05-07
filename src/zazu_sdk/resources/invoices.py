"""Mirrors lib/zazu/resources/invoices.rb."""

from __future__ import annotations

from typing import Any

from ..page import MAX_PER_PAGE, Page
from ..response import ZazuResponse
from .base import ResourceBase


class Invoices(ResourceBase):
    def list(
        self,
        *,
        status: str | None = None,
        customer_id: str | None = None,
        limit: int = MAX_PER_PAGE,
        cursor: str | None = None,
    ) -> Page[Any]:
        return self.list_page(
            "api/invoices",
            {"status": status, "customer_id": customer_id},
            limit=limit,
            cursor=cursor,
        )

    def get(self, id: str) -> ZazuResponse:
        return self.http_get(self.encode_path("api/invoices", id))

    def create(self, **attributes: Any) -> ZazuResponse:
        return self.http_post("api/invoices", body=attributes)

    def update(self, id: str, **attributes: Any) -> ZazuResponse:
        return self.http_patch(self.encode_path("api/invoices", id), body=attributes)

    def send_invoice(self, id: str) -> ZazuResponse:
        return self.http_post(self.encode_path("api/invoices", id, "send"))

    def mark_as_paid(self, id: str) -> ZazuResponse:
        return self.http_post(self.encode_path("api/invoices", id, "mark_as_paid"))

    def cancel(self, id: str) -> ZazuResponse:
        return self.http_post(self.encode_path("api/invoices", id, "cancel"))

    def credit_note(self, id: str) -> ZazuResponse:
        return self.http_post(self.encode_path("api/invoices", id, "credit_note"))

    def delete(self, id: str) -> ZazuResponse:
        return self.http_delete(self.encode_path("api/invoices", id))

    def create_payment_link(self, invoice_id: str, *, account_id: str) -> ZazuResponse:
        return self.http_post(
            self.encode_path("api/invoices", invoice_id, "payment_link"),
            body={"account_id": account_id},
        )
