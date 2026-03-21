from __future__ import annotations

import json
import re
from urllib.parse import urljoin

from ..html_tools import parse_html_document
from ..models import NormalizedPage, PageSourceRecord
from ..utils import clean_text, dedupe, strip_trailing_commas, text_hash
from .base import BaseAdapter


ARCHIVE_BASE = "https://developer.apple.com/library/archive/navigation/"


def parse_library_index(raw: str) -> list[dict[str, str]]:
    parsed = json.loads(strip_trailing_commas(raw))
    documents: list[dict[str, str]] = []
    for entry in parsed.get("documents", []):
        if len(entry) < 10:
            continue
        title = clean_text(entry[0].replace("&quot;", '"'))
        url = urljoin(ARCHIVE_BASE, entry[9])
        documents.append({"title": title, "url": re.sub(r"#.*$", "", url)})
    return documents


class ArchiveAdapter(BaseAdapter):
    name = "archive"
    section = "archive"

    def can_handle(self, route: str) -> bool:
        return route.startswith("/library/archive/")

    def discover(self, *, limit: int | None = None) -> list[str]:
        raw = self.http.get_text(urljoin(ARCHIVE_BASE, "library.json"))
        routes: list[str] = ["/library/archive/navigation"]
        for document in parse_library_index(raw):
            route = document["url"].replace("https://developer.apple.com", "").rstrip("/")
            if route:
                routes.append(route)
        routes = dedupe(routes)
        if limit:
            return routes[:limit]
        return routes

    def fetch(self, route: str) -> NormalizedPage:
        url = f"https://developer.apple.com{route}"
        raw_html = self.http.get_text(url)
        title, blocks, links, assets = parse_html_document(raw_html, url=url)
        return NormalizedPage(
            route=route,
            source_url=url,
            source_locale="en-US",
            section=self.section,
            content_type="archive-html",
            title=title or clean_text(route.rsplit("/", 1)[-1]),
            original_title=title or clean_text(route.rsplit("/", 1)[-1]),
            source_hash=text_hash(raw_html),
            canonical_source="machine-translation",
            discovered_links=[link for link in links if link.startswith("/library/archive/")],
            asset_links=assets,
            content_blocks=blocks,
            source_variants=[PageSourceRecord(url=url, locale="en-US", content_type="text/html", raw_text=raw_html)],
        )
