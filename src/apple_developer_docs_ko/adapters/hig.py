from __future__ import annotations

import json

from ..models import PageSourceRecord
from ..utils import clean_text, dedupe
from .base import BaseAdapter
from .docc import DOCC_DATA_BASE, normalize_docc_page


def _collect_hig_paths(nodes: list[dict], out: list[str]) -> None:
    for node in nodes:
        path = node.get("path")
        if path:
            normalized = path.removeprefix("/kr")
            if normalized.startswith("/design/"):
                out.append(normalized.rstrip("/"))
        children = node.get("children") or []
        if children:
            _collect_hig_paths(children, out)


class HIGAdapter(BaseAdapter):
    name = "hig"
    section = "hig"
    locale_probe_timeout = 5.0
    locale_probe_attempts = 1

    def can_handle(self, route: str) -> bool:
        return route.startswith("/design/")

    def preferred_locale(self, route: str) -> str:
        kr_json = f"{DOCC_DATA_BASE}/kr{route}.json"
        return (
            "ko-KR"
            if self.http.exists(
                kr_json,
                timeout=self.locale_probe_timeout,
                attempts=self.locale_probe_attempts,
            )
            else "en-US"
        )

    def discover(self, *, limit: int | None = None) -> list[str]:
        locale_prefix = "kr/" if self.preferred_locale("/design/human-interface-guidelines").startswith("ko") else ""
        index = self.http.get_json(f"https://developer.apple.com/tutorials/data/index/{locale_prefix}design--human-interface-guidelines")
        paths: list[str] = []
        swift_tree = index.get("interfaceLanguages", {}).get("swift", [])
        _collect_hig_paths(swift_tree, paths)
        paths = dedupe(paths)
        if limit:
            return paths[:limit]
        return paths

    def fetch(self, route: str) -> NormalizedPage:
        english_raw = self.http.get_text(f"{DOCC_DATA_BASE}{route}.json")
        english_doc = json.loads(english_raw)
        original_title = english_doc.get("metadata", {}).get("title") or clean_text(route.rsplit("/", 1)[-1])
        kr_json_url = f"{DOCC_DATA_BASE}/kr{route}.json"
        if self.http.exists(
            kr_json_url,
            timeout=self.locale_probe_timeout,
            attempts=self.locale_probe_attempts,
        ):
            kr_raw = self.http.get_text(kr_json_url)
            kr_doc = json.loads(kr_raw)
            page = normalize_docc_page(
                route=route,
                raw_text=kr_raw,
                doc=kr_doc,
                section=self.section,
                source_locale="ko-KR",
                canonical_source="official-ko",
            )
            page.original_title = original_title
            page.source_variants = [
                PageSourceRecord(url=f"{DOCC_DATA_BASE}{route}.json", locale="en-US", content_type="application/json", raw_text=english_raw),
                PageSourceRecord(url=kr_json_url, locale="ko-KR", content_type="application/json", raw_text=kr_raw),
            ]
            return page
        page = normalize_docc_page(route=route, raw_text=english_raw, doc=english_doc, section=self.section)
        return page
