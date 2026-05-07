"""Mirror of spec/zazu/resources/webhook_endpoints_spec.rb."""

from __future__ import annotations

from tests.fixture_ids import FIXTURE_IDS
from zazu_sdk import Page


def test_list(make_client):
    zazu = make_client(["webhook_endpoints/list"])
    page = zazu.webhook_endpoints.list()
    assert isinstance(page, Page)


def test_get(make_client):
    zazu = make_client(["webhook_endpoints/get"])
    response = zazu.webhook_endpoints.get(FIXTURE_IDS["ZAZU_FIXTURE_WEBHOOK_ID"])
    assert isinstance(response.body["id"], str)


def test_create(make_client):
    zazu = make_client(["webhook_endpoints/create"])
    response = zazu.webhook_endpoints.create(
        url="https://example.com/zazu-webhooks",
        events=["payment_link.paid"],
        description="SDK fixture endpoint",
    )
    assert response.status == 201


def test_update(make_client):
    zazu = make_client(["webhook_endpoints/update"])
    response = zazu.webhook_endpoints.update(
        FIXTURE_IDS["ZAZU_FIXTURE_WEBHOOK_ID"],
        description="Updated description",
        events=["payment_link.paid"],
    )
    assert response.success


def test_delete(make_client):
    zazu = make_client(["webhook_endpoints/delete"])
    response = zazu.webhook_endpoints.delete(FIXTURE_IDS["ZAZU_FIXTURE_DELETABLE_WEBHOOK_ID"])
    assert response.status == 204


def test_test_endpoint(make_client):
    zazu = make_client(["webhook_endpoints/test"])
    response = zazu.webhook_endpoints.test_endpoint(FIXTURE_IDS["ZAZU_FIXTURE_WEBHOOK_ID"])
    assert response.success


def test_regenerate_secret(make_client):
    zazu = make_client(["webhook_endpoints/regenerate_secret"])
    response = zazu.webhook_endpoints.regenerate_secret(FIXTURE_IDS["ZAZU_FIXTURE_WEBHOOK_ID"])
    assert response.success


def test_enable(make_client):
    zazu = make_client(["webhook_endpoints/enable"])
    response = zazu.webhook_endpoints.enable(FIXTURE_IDS["ZAZU_FIXTURE_DISABLED_WEBHOOK_ID"])
    assert response.success


def test_disable(make_client):
    zazu = make_client(["webhook_endpoints/disable"])
    response = zazu.webhook_endpoints.disable(FIXTURE_IDS["ZAZU_FIXTURE_ENABLED_WEBHOOK_ID"])
    assert response.success
