"""Mirror of spec/zazu/resources/beneficiaries_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS
from zazu_sdk import Page


def test_list(make_client):
    zazu = make_client(["beneficiaries/list"])
    page = zazu.beneficiaries.list()
    assert isinstance(page, Page)
    assert isinstance(page.data[0]["external_accounts"], list)


def test_get(make_client):
    zazu = make_client(["beneficiaries/get"])
    response = zazu.beneficiaries.get(FIXTURE_IDS["ZAZU_FIXTURE_BENEFICIARY_ID"])
    assert isinstance(response.body["id"], str)
    assert isinstance(response.body["external_accounts"], list)
