"""Mirror of spec/zazu/resources/invoices_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS
from zazu_sdk import Page


def test_list(make_client):
    zazu = make_client(["invoices/list"])
    page = zazu.invoices.list()
    assert isinstance(page, Page)


def test_get(make_client):
    zazu = make_client(["invoices/get"])
    response = zazu.invoices.get(FIXTURE_IDS["ZAZU_FIXTURE_INVOICE_ID"])
    assert isinstance(response.body["id"], str)


def test_create(make_client):
    zazu = make_client(["invoices/create"])
    response = zazu.invoices.create(
        customer_id=FIXTURE_IDS["ZAZU_FIXTURE_CUSTOMER_ID"],
        currency_code="MAD",
        issue_date="2026-05-03",
        due_date="2026-06-03",
        items=[{"description": "SDK fixture line", "quantity": 1, "unit_price": "100.00"}],
    )
    assert response.status == 201


def test_update(make_client):
    zazu = make_client(["invoices/update"])
    response = zazu.invoices.update(
        FIXTURE_IDS["ZAZU_FIXTURE_INVOICE_ID"],
        notes="updated by SDK fixture spec",
    )
    assert response.status == 200


def test_delete(make_client):
    zazu = make_client(["invoices/delete"])
    response = zazu.invoices.delete(FIXTURE_IDS["ZAZU_FIXTURE_DELETABLE_INVOICE_ID"])
    assert response.status == 204
