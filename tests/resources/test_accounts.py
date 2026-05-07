"""Mirror of spec/zazu/resources/accounts_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS
from zazu_sdk import Page


def test_list(make_client):
    zazu = make_client(["accounts/list"])
    page = zazu.accounts.list()
    assert isinstance(page, Page)


def test_list_currency_filtered(make_client):
    zazu = make_client(["accounts/list_currency_filtered"])
    page = zazu.accounts.list(currency_code="MAD")
    assert isinstance(page, Page)


def test_get(make_client):
    zazu = make_client(["accounts/get"])
    response = zazu.accounts.get(FIXTURE_IDS["ZAZU_FIXTURE_ACCOUNT_ID"])
    assert isinstance(response.body["id"], str)


def test_list_transactions(make_client):
    zazu = make_client(["accounts/list_transactions"])
    page = zazu.accounts.list_transactions(FIXTURE_IDS["ZAZU_FIXTURE_ACCOUNT_ID"])
    assert isinstance(page, Page)


def test_get_transaction(make_client):
    zazu = make_client(["accounts/get_transaction"])
    response = zazu.accounts.get_transaction(
        FIXTURE_IDS["ZAZU_FIXTURE_ACCOUNT_ID"],
        FIXTURE_IDS["ZAZU_FIXTURE_TRANSACTION_ID"],
    )
    assert isinstance(response.body["id"], str)
