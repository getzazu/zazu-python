# zazu-sdk

Python SDK for the [Zazu API](https://zazu.ma).

## Install

```bash
pip install zazu-sdk
```

Requires Python 3.11+.

## Quick start

```python
from zazu_sdk import Zazu

client = Zazu(api_key="sk_live_...")

client.entity.get()
client.accounts.list(currency_code="MAD")
client.customers.list(q="Acme")
client.customers.create(
    customer_type="business",
    company_name="Acme Corp",
    email="billing@acme.com",
)

client.invoices.list()
client.payment_links.cancel(payment_link_id)
client.webhook_endpoints.list()

client.checkout_sessions.create(
    account_id=account_id,
    amount="100.00",
    success_url="https://example.com/ok",
    cancel_url="https://example.com/cancel",
)
client.checkout_sessions.get(session_id)
```

The client picks up `ZAZU_API_KEY`, `ZAZU_BASE_URL`, `ZAZU_API_VERSION`, and
`ZAZU_TIMEOUT` from the environment if you don't pass them.

## Pagination

List endpoints return a `Page`. Iterate one page or chase cursors:

```python
page = client.invoices.list(limit=25)
for invoice in page:
    ...

# All items, automatic cursor chasing:
for invoice in client.invoices.list().auto_paging_iter():
    ...
```

## Errors

Nine concrete subclasses; discriminate with `isinstance`:

```python
from zazu_sdk import (
    ZazuValidationError,
    ZazuRateLimitError,
    ZazuNotFoundError,
)

try:
    client.invoices.get("nope")
except ZazuNotFoundError as err:
    print(err.status, err.request_id, err.body)
except ZazuRateLimitError as err:
    print("retry after", err.retry_after, "seconds")
```

## Cross-SDK contract

`zazu-sdk` is one of several Zazu SDKs that all replay cassettes recorded by
the canonical [`zazu-ruby`](https://github.com/getzazu/zazu-ruby) SDK against
staging. The wire format is snake_case JSON; request and response shapes match
across Ruby, TypeScript, Python, Go, and Rust.

## License

MIT.
