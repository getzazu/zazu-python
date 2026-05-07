"""Mirror of spec/zazu/resources/entity_spec.rb."""

from __future__ import annotations


def test_entity_get(make_client):
    zazu = make_client(["entity/get"])
    response = zazu.entity.get()
    assert response.status == 200
    assert isinstance(response.body["id"], str)
