"""Shared test fixtures."""

from __future__ import annotations

from collections.abc import Callable, Iterator

import pytest

from zazu_sdk import Zazu

from .cassette_replay import cassette_client
from .fixture_ids import STAGING_BASE_URL, TEST_API_KEY


@pytest.fixture
def make_client() -> Iterator[Callable[[list[str]], Zazu]]:
    """Return a factory: `make_client(["customers/list", ...])` builds a Zazu
    bound to a cassette-replay transport that walks those cassettes in order."""

    clients: list[Zazu] = []

    def _factory(cassettes: list[str]) -> Zazu:
        http = cassette_client(cassettes)
        client = Zazu(api_key=TEST_API_KEY, base_url=STAGING_BASE_URL, http_client=http)
        clients.append(client)
        return client

    yield _factory

    for c in clients:
        c.close()
