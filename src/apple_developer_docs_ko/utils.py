from __future__ import annotations

from html import unescape
from urllib.parse import urljoin, urlparse
import hashlib
import json
import re


APPLE_BASE_URL = "https://developer.apple.com"

SKIP_PREFIXES = (
    "/account",
    "/search",
    "/forums/create",
    "/forums/login",
    "/forums/preferences",
    "/forums/profile",
)


def strip_trailing_commas(value: str) -> str:
    return re.sub(r",\s*([}\]])", r"\1", value)


def json_hash(value: object) -> str:
    blob = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def text_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(value or "")).strip()


def absolutize(url: str, base_url: str = APPLE_BASE_URL) -> str:
    return urljoin(base_url, url)


def is_public_page_url(url: str) -> bool:
    parsed = urlparse(absolutize(url))
    if parsed.netloc != "developer.apple.com":
        return False
    if parsed.query:
        return False
    if any(parsed.path.startswith(prefix) for prefix in SKIP_PREFIXES):
        return False
    return True


def is_same_site_url(url: str) -> bool:
    return urlparse(absolutize(url)).netloc == "developer.apple.com"


def dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out
