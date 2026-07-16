# Changelog

All notable changes to `zazu-sdk` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0]

Initial release.

### Added

- Sync `Zazu` client built on `httpx`
- Resource modules: `accounts`, `beneficiaries`, `checkout_sessions`, `customers`, `entity`, `invoices`, `payment_links`, `transfer_drafts`, `webhook_endpoints`
- Cursor-based `Page` with `auto_paging_iter()`
- Nine-class error hierarchy mirroring `zazu-ruby`
- Cassette-replay test harness driven by the Ruby SDK's release tarball
