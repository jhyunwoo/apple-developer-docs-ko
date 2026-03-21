from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import hashlib


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass(slots=True)
class AssetLink:
    url: str
    local_path: str | None = None
    content_type: str | None = None
    status: str = "pending"
    sha256: str | None = None


@dataclass(slots=True)
class ContentBlock:
    kind: str
    body: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    translatable: bool = True


@dataclass(slots=True)
class PageSourceRecord:
    url: str
    locale: str
    content_type: str
    raw_text: str
    source_hash: str | None = None

    def __post_init__(self) -> None:
        if self.source_hash is None:
            self.source_hash = hashlib.sha256(self.raw_text.encode("utf-8")).hexdigest()


@dataclass(slots=True)
class NormalizedPage:
    route: str
    source_url: str
    source_locale: str
    section: str
    content_type: str
    title: str
    original_title: str
    source_hash: str
    canonical_source: str
    discovered_links: list[str] = field(default_factory=list)
    asset_links: list[AssetLink] = field(default_factory=list)
    content_blocks: list[ContentBlock] = field(default_factory=list)
    last_crawled_at: str = field(default_factory=utc_now)
    last_translated_at: str | None = None
    source_variants: list[PageSourceRecord] = field(default_factory=list)

    def frontmatter(self) -> dict[str, Any]:
        return {
            "route": self.route,
            "source_url": self.source_url,
            "source_locale": self.source_locale,
            "section": self.section,
            "content_type": self.content_type,
            "title": self.title,
            "original_title": self.original_title,
            "source_hash": self.source_hash,
            "canonical_source": self.canonical_source,
            "last_crawled_at": self.last_crawled_at,
            "last_translated_at": self.last_translated_at,
        }
