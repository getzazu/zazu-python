"""Mirror of spec/zazu/resources/customers_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS
from zazu_sdk import Page


def test_list(make_client):
    zazu = make_client(["customers/list"])
    page = zazu.customers.list()
    assert isinstance(page, Page)


def test_list_q_filtered(make_client):
    zazu = make_client(["customers/list_q_filtered"])
    page = zazu.customers.list(q="Acme")
    assert isinstance(page, Page)


def test_get(make_client):
    zazu = make_client(["customers/get"])
    response = zazu.customers.get(FIXTURE_IDS["ZAZU_FIXTURE_CUSTOMER_ID"])
    assert isinstance(response.body["id"], str)


def test_create(make_client):
    zazu = make_client(["customers/create"])
    response = zazu.customers.create(
        customer_type="business",
        company_name="Zazu SDK Fixture Co (zazu-ruby-fixture-v1-spec)",
        email="create-spec@zazu-ruby-fixture.example.com",
        ice_number="000000000000000",
    )
    assert response.status == 201
    assert isinstance(response.body["id"], str)


def test_update(make_client):
    zazu = make_client(["customers/update"])
    response = zazu.customers.update(
        FIXTURE_IDS["ZAZU_FIXTURE_CUSTOMER_ID"],
        email="updated@example.com",
    )
    assert response.status == 200


def test_delete(make_client):
    zazu = make_client(["customers/delete"])
    response = zazu.customers.delete(FIXTURE_IDS["ZAZU_FIXTURE_DELETABLE_CUSTOMER_ID"])
    assert response.status == 204
