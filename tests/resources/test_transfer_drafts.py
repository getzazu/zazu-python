"""Mirror of spec/zazu/resources/transfer_drafts_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS


def test_create(make_client):
    zazu = make_client(["transfer_drafts/create"])
    response = zazu.transfer_drafts.create(
        account_id=FIXTURE_IDS["ZAZU_FIXTURE_ACCOUNT_ID"],
        beneficiary_id=FIXTURE_IDS["ZAZU_FIXTURE_BENEFICIARY_ID"],
        amount="150.00",
        payment_reference="SDK fixture",
    )
    assert response.status == 201
    assert response.body["status"] == "requested"
    assert response.body["transfer"] is None


def test_get(make_client):
    zazu = make_client(["transfer_drafts/get"])
    response = zazu.transfer_drafts.get(FIXTURE_IDS["ZAZU_FIXTURE_TRANSFER_DRAFT_ID"])
    assert isinstance(response.body["id"], str)
    assert isinstance(response.body["status"], str)
