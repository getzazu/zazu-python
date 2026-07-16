#!/usr/bin/env python3
"""Download the cassette tarball published by zazu-ruby's release workflow.

CI calls this before running tests so we don't have to commit cassettes into
both repos.

  python scripts/fetch_cassettes.py            # latest release
  python scripts/fetch_cassettes.py v0.2.0     # specific tag

Cassettes land under tests/fixtures/cassettes/.
"""

from __future__ import annotations

import json
import os
import sys
import tarfile
import tempfile
import time
import urllib.request
from pathlib import Path

REPO = "getzazu/zazu-ruby"
ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "tests" / "fixtures" / "cassettes"


def urlopen_with_retry(req: urllib.request.Request, attempts: int = 8):
    """GitHub's API weathers occasional 503 storms - retry rather than fail CI."""
    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            return urllib.request.urlopen(req)
        except Exception as error:
            last_error = error
            time.sleep(10)
    raise SystemExit(f"fetch failed after {attempts} attempts: {req.full_url}: {last_error}")


def latest_tag() -> str:
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.getenv("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/releases?per_page=1",
        headers=headers,
    )

    with urlopen_with_retry(req) as resp:
        data = json.loads(resp.read())
    for rel in data:
        if not rel.get("draft"):
            return str(rel["tag_name"])
    raise SystemExit(f"No published releases found for {REPO}")


def main() -> int:
    tag = sys.argv[1] if len(sys.argv) > 1 else latest_tag()
    url = f"https://github.com/{REPO}/releases/download/{tag}/cassettes-{tag}.tar.gz"
    print(f"Fetching cassettes from {url}")

    headers = {"Accept": "application/octet-stream"}
    if token := os.getenv("GH_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)

    with (
        urlopen_with_retry(req) as resp,
        tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False) as tmp,
    ):
        tmp.write(resp.read())
        tar_path = tmp.name

    DEST.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tar_path, "r:gz") as tar:
        # Tarball root is `cassettes/`; extract relative to tests/fixtures/
        tar.extractall(DEST.parent, filter="data")

    print(f"Cassettes extracted to {DEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
