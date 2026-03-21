from __future__ import annotations

from urllib.parse import urlparse

from ..html_tools import parse_html_document
from ..models import NormalizedPage, PageSourceRecord
from ..paths import normalize_route
from ..utils import absolutize, clean_text, dedupe, is_public_page_url, text_hash
from .base import BaseAdapter


PUBLIC_SEEDS = [
    "/",
    "/news/",
    "/get-started/",
    "/learn/",
    "/platforms/",
    "/events/",
    "/support/",
    "/download/",
]

SECTION_PREFIXES = ("/documentation/", "/design/", "/videos/", "/library/archive/")


class PublicHtmlAdapter(BaseAdapter):
    name = "public"
    section = "public"
    incremental_discovery = True
    locale_probe_timeout = 5.0
    locale_probe_attempts = 1

    def can_handle(self, route: str) -> bool:
        return route == "/" or (route.startswith("/") and not route.startswith(SECTION_PREFIXES))

    def preferred_locale(self, route: str) -> str:
        if route == "/":
            return "en-US"
        kr_url = absolutize(f"/kr{route}")
        return (
            "ko-KR"
            if self.http.exists(
                kr_url,
                timeout=self.locale_probe_timeout,
                attempts=self.locale_probe_attempts,
            )
            else "en-US"
        )

    def seed_routes(self, *, limit: int | None = None) -> list[str]:
        routes = [normalize_route(seed) for seed in PUBLIC_SEEDS]
        if limit:
            return routes[:limit]
        return routes

    def expand_route(self, route: str) -> list[str]:
        try:
            html = self.http.get_text(absolutize(route))
        except Exception:
            return []
        _, _, links, _ = parse_html_document(html, url=absolutize(route))
        routes: list[str] = []
        for link in links:
            if not is_public_page_url(link):
                continue
            if link.startswith(SECTION_PREFIXES):
                continue
            if self.can_handle(link):
                routes.append(link)
        return dedupe(routes)

    def discover(self, *, limit: int | None = None) -> list[str]:
        queue = self.seed_routes()
        seen: set[str] = set()
        routes: list[str] = []
        while queue:
            route = normalize_route(queue.pop(0))
            if route in seen or not self.can_handle(route):
                continue
            seen.add(route)
            routes.append(route)
            if limit and len(routes) >= limit:
                break
            for link in self.expand_route(route):
                if link not in seen:
                    queue.append(link)
        return dedupe(routes)

    def fetch(self, route: str) -> NormalizedPage:
        canonical_locale = self.preferred_locale(route)
        canonical_url = absolutize(f"/kr{route}") if canonical_locale.startswith("ko") and route != "/" else absolutize(route)
        raw_html = self.http.get_text(canonical_url)
        title, blocks, links, assets = parse_html_document(raw_html, url=canonical_url)
        english_url = absolutize(route)
        source_variants = [PageSourceRecord(url=canonical_url, locale=canonical_locale, content_type="text/html", raw_text=raw_html)]
        if canonical_url != english_url:
            source_variants.append(
                PageSourceRecord(
                    url=english_url,
                    locale="en-US",
                    content_type="text/html",
                    raw_text=self.http.get_text(english_url),
                )
            )
        return NormalizedPage(
            route=route,
            source_url=english_url,
            source_locale=canonical_locale,
            section=self.section,
            content_type="public-html",
            title=title or clean_text(route.rsplit("/", 1)[-1] or "Apple Developer"),
            original_title=title or clean_text(route.rsplit("/", 1)[-1] or "Apple Developer"),
            source_hash=text_hash(raw_html),
            canonical_source="official-ko" if canonical_locale.startswith("ko") else "machine-translation",
            discovered_links=[link for link in links if self.can_handle(link)],
            asset_links=assets,
            content_blocks=blocks,
            source_variants=source_variants,
        )
