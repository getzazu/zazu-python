"""Mirror of spec/zazu/resources/payment_links_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS
from zazu_sdk import Page


def test_list(make_client):
    zazu = make_client(["payment_links/list"])
    page = zazu.payment_links.list()
    assert isinstance(page, Page)


def test_get(make_client):
    zazu = make_client(["payment_links/get"])
    response = zazu.payment_links.get(FIXTURE_IDS["ZAZU_FIXTURE_PAYMENT_LINK_ID"])
    assert isinstance(response.body["id"], str)


def test_create(make_client):
    zazu = make_client(["payment_links/create"])
    response = zazu.payment_links.create(
        account_id=FIXTURE_IDS["ZAZU_FIXTURE_ACCOUNT_ID"],
        amount="100.00",
        title="SDK fixture",
        description="Created by zazu-ruby fixture spec",
        link_type="single",
    )
    assert response.status == 201


def test_cancel(make_client):
    zazu = make_client(["payment_links/cancel"])
    response = zazu.payment_links.cancel(FIXTURE_IDS["ZAZU_FIXTURE_CANCELLABLE_PAYMENT_LINK_ID"])
    assert response.success
