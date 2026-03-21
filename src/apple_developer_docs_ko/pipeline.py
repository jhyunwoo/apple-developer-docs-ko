from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from .adapters import ArchiveAdapter, DoccAdapter, HIGAdapter, PublicHtmlAdapter, VideosAdapter
from .assets import mirror_asset
from .config import Settings
from .http import HttpClient
from .markdown_renderer import write_page_markdown
from .models import NormalizedPage, utc_now
from .paths import normalize_route
from .site_builder import build_site
from .store import ManifestStore
from .translate import Translator


SMOKE_ROUTES = {
    "docc": ["/documentation/MapKit"],
    "hig": ["/design/human-interface-guidelines"],
    "videos": ["/videos/play/wwdc2025/101"],
    "archive": ["/library/archive/navigation"],
    "public": ["/news"],
}


@dataclass(slots=True)
class SyncResult:
    processed_routes: list[str]
    run_id: int | None


@dataclass(slots=True)
class QueueSeedResult:
    inserted: int
    total: int
    translated: int
    queued: int


@dataclass(slots=True)
class QueueExtendResult:
    expanded: int
    discovered: int
    total: int
    translated: int
    queued: int


class MirrorPipeline:
    def __init__(self, settings: Settings, translator: Translator) -> None:
        self.settings = settings
        self.settings.ensure_directories()
        self.http = HttpClient(settings)
        self.store = ManifestStore(settings.manifest_path)
        self.translator = translator
        self.adapters = {
            "docc": DoccAdapter(self.http),
            "hig": HIGAdapter(self.http),
            "videos": VideosAdapter(self.http),
            "archive": ArchiveAdapter(self.http),
            "public": PublicHtmlAdapter(self.http),
        }

    def close(self) -> None:
        self.store.close()

    def _queue_entry_for_route(
        self,
        *,
        route: str,
        section: str,
        ordinal: int,
    ) -> dict[str, object]:
        queue_row = self.store.conn.execute(
            "SELECT ordinal FROM translation_queue WHERE route = ?",
            (route,),
        ).fetchone()
        page_row = self.store.conn.execute(
            "SELECT title, source_locale, last_crawled_at, last_translated_at, removed_at FROM pages WHERE route = ?",
            (route,),
        ).fetchone()
        translation_row = self.store.conn.execute(
            "SELECT translator, translated_at FROM translations WHERE route = ?",
            (route,),
        ).fetchone()
        status = "queued"
        translated_at = None
        source_locale = None
        title = None
        if page_row is not None and page_row["removed_at"] is None:
            source_locale = page_row["source_locale"]
            title = page_row["title"]
            if source_locale.startswith("ko"):
                status = "translated"
                translated_at = page_row["last_translated_at"] or page_row["last_crawled_at"]
        if translation_row is not None and translation_row["translator"] != "identity":
            status = "translated"
            translated_at = translation_row["translated_at"]
        return {
            "route": route,
            "section": section,
            "ordinal": queue_row["ordinal"] if queue_row is not None else ordinal,
            "status": status,
            "source_locale": source_locale,
            "title": title,
            "discovered_at": utc_now(),
            "translated_at": translated_at,
        }

    def _enqueue_routes(self, *, section: str, routes: list[str]) -> int:
        if not routes:
            return 0
        max_ordinal_row = self.store.conn.execute(
            "SELECT COALESCE(MAX(ordinal), 0) AS max_ordinal FROM translation_queue"
        ).fetchone()
        ordinal = (max_ordinal_row["max_ordinal"] or 0) + 1
        entries: list[dict[str, object]] = []
        for route in routes:
            entry = self._queue_entry_for_route(route=route, section=section, ordinal=ordinal)
            entries.append(entry)
            if entry["ordinal"] == ordinal:
                ordinal += 1
        return self.store.upsert_translation_queue_entries(entries)

    def _bootstrap_discovery_frontier(self, *, section: str, routes: list[str]) -> int:
        inserted = self.store.insert_discovery_frontier_routes(section=section, routes=routes)
        self._enqueue_routes(section=section, routes=routes)
        return inserted

    def _process_page(self, page, *, dry_run: bool) -> None:
        if page.source_locale.startswith("en"):
            if not self.store.is_translation_current(page.route, page.source_hash):
                page = self.translator.translate_page(page)
            else:
                page.last_translated_at = page.last_crawled_at
        else:
            page.last_translated_at = page.last_crawled_at

        if dry_run:
            return

        page.asset_links = [mirror_asset(self.http, asset) for asset in page.asset_links]
        write_page_markdown(self.settings.content_dir, page)
        self.store.upsert_page(page)
        if page.last_translated_at and page.source_locale.startswith("en"):
            self.store.mark_translation(page.route, self.translator.name, page.source_hash)
        if page.source_locale.startswith("ko"):
            self.store.set_translation_queue_status(
                page.route,
                status="translated",
                translated_at=page.last_translated_at or page.last_crawled_at,
            )
        elif page.last_translated_at and self.translator.name != "identity":
            self.store.set_translation_queue_status(
                page.route,
                status="translated",
                translated_at=page.last_translated_at,
            )

    def sync(self, *, sections: list[str], limit: int | None = None, dry_run: bool = False) -> SyncResult:
        run_id = None if dry_run else self.store.start_sync_run(sections)
        processed_routes: list[str] = []
        try:
            for section in sections:
                adapter = self.adapters[section]
                routes = adapter.discover(limit=limit)
                for route in routes:
                    if limit and len(processed_routes) >= limit:
                        break
                    page = adapter.fetch(route)
                    self._process_page(page, dry_run=dry_run)
                    processed_routes.append(route)
                if limit and len(processed_routes) >= limit:
                    break
            if not dry_run:
                self.store.tombstone_missing_pages(processed_routes, sections=sections)
                self.store.finish_sync_run(run_id, status="completed", notes=f"processed={len(processed_routes)}")
            return SyncResult(processed_routes=processed_routes, run_id=run_id)
        except Exception as exc:
            if run_id is not None:
                self.store.finish_sync_run(run_id, status="failed", notes=str(exc))
            raise

    def smoke_test(self, *, dry_run: bool = False) -> SyncResult:
        processed_routes: list[str] = []
        videos_adapter = self.adapters["videos"]
        previous_segment_cap = getattr(videos_adapter, "max_transcript_segments", None)
        videos_adapter.max_transcript_segments = 40
        try:
            for section, routes in SMOKE_ROUTES.items():
                adapter = self.adapters[section]
                for route in routes:
                    page = adapter.fetch(route)
                    self._process_page(page, dry_run=dry_run)
                    processed_routes.append(route)
        finally:
            videos_adapter.max_transcript_segments = previous_segment_cap
        return SyncResult(processed_routes=processed_routes, run_id=None)

    def build_site(self) -> None:
        build_site(self.settings.content_dir, self.settings.dist_dir)

    def _load_content_frontmatter(self, markdown_path: Path) -> tuple[dict, str]:
        raw = markdown_path.read_text(encoding="utf-8")
        if not raw.startswith("---\n"):
            return {}, raw
        try:
            _, rest = raw.split("---\n", 1)
            frontmatter_text, body = rest.split("\n---\n", 1)
        except ValueError:
            return {}, raw
        return yaml.safe_load(frontmatter_text) or {}, body

    def _sync_manifest_from_content(self) -> int:
        synced = 0
        for markdown_path in sorted(self.settings.content_dir.rglob("index.md")):
            frontmatter, _ = self._load_content_frontmatter(markdown_path)
            route = normalize_route(
                str(frontmatter.get("route") or "/" + markdown_path.relative_to(self.settings.content_dir).parent.as_posix())
            )
            source_locale = str(frontmatter.get("source_locale") or "en-US")
            page = NormalizedPage(
                route=route,
                source_url=str(frontmatter.get("source_url") or route),
                source_locale=source_locale,
                section=str(frontmatter.get("section") or "public"),
                content_type=str(frontmatter.get("content_type") or "article"),
                title=str(frontmatter.get("title") or frontmatter.get("original_title") or markdown_path.parent.name),
                original_title=str(frontmatter.get("original_title") or frontmatter.get("title") or markdown_path.parent.name),
                source_hash=str(frontmatter.get("source_hash") or ""),
                canonical_source=str(frontmatter.get("canonical_source") or "manual-translation"),
                last_crawled_at=str(frontmatter.get("last_crawled_at") or utc_now()),
                last_translated_at=(
                    str(frontmatter.get("last_translated_at"))
                    if frontmatter.get("last_translated_at")
                    else None
                ),
            )
            self.store.upsert_page(page)
            if page.source_locale.startswith("en") and page.last_translated_at:
                translator_name = "manual" if page.canonical_source == "manual-translation" else page.canonical_source
                self.store.mark_translation(page.route, translator_name, page.source_hash)
            synced += 1
        return synced

    def seed_translation_queue(
        self,
        *,
        sections: list[str],
        limit: int | None = None,
        per_section_limit: int | None = None,
        reset: bool = False,
    ) -> QueueSeedResult:
        before_counts = self.store.get_translation_queue_counts()
        if reset:
            self.store.clear_translation_queue()
            self.store.clear_discovery_frontier(sections=sections)
        for section in sections:
            adapter = self.adapters[section]
            route_limit = per_section_limit or limit
            if adapter.incremental_discovery:
                routes = adapter.seed_routes(limit=route_limit)
                self._bootstrap_discovery_frontier(section=section, routes=routes)
            else:
                routes = adapter.discover(limit=route_limit)
                self._enqueue_routes(section=section, routes=routes)
            if limit is not None:
                remaining = limit - len(routes)
                if remaining <= 0:
                    break
                limit = remaining
        counts = self.store.get_translation_queue_counts()
        inserted = (counts["total"] or 0) - (0 if reset else (before_counts["total"] or 0))
        return QueueSeedResult(
            inserted=inserted,
            total=counts["total"] or 0,
            translated=counts["translated"] or 0,
            queued=counts["queued"] or 0,
        )

    def extend_translation_queue(
        self,
        *,
        sections: list[str],
        expand_routes: int = 100,
    ) -> QueueExtendResult:
        expanded = 0
        discovered = 0
        for section in sections:
            adapter = self.adapters[section]
            if not adapter.incremental_discovery:
                continue
            if not self.store.get_pending_discovery_frontier(section=section, limit=1):
                self._bootstrap_discovery_frontier(section=section, routes=adapter.seed_routes())
            frontier_rows = self.store.get_pending_discovery_frontier(section=section, limit=expand_routes)
            for row in frontier_rows:
                route = row["route"]
                try:
                    next_routes = adapter.expand_route(route)
                    self.store.insert_discovery_frontier_routes(
                        section=section,
                        routes=next_routes,
                        discovered_from=route,
                    )
                    discovered += self._enqueue_routes(section=section, routes=next_routes)
                    self.store.mark_discovery_frontier_expanded(section=section, route=route)
                except Exception as exc:
                    self.store.mark_discovery_frontier_expanded(
                        section=section,
                        route=route,
                        last_error=str(exc),
                    )
                expanded += 1
        counts = self.store.get_translation_queue_counts()
        return QueueExtendResult(
            expanded=expanded,
            discovered=discovered,
            total=counts["total"] or 0,
            translated=counts["translated"] or 0,
            queued=counts["queued"] or 0,
        )

    def get_translation_queue_status(self, *, next_limit: int = 10) -> tuple[dict[str, int], list[object]]:
        counts = self.store.get_translation_queue_counts()
        next_items = self.store.get_next_translation_queue_items(limit=next_limit)
        return (
            {
                "total": counts["total"] or 0,
                "translated": counts["translated"] or 0,
                "queued": counts["queued"] or 0,
                "in_progress": counts["in_progress"] or 0,
                "blocked": counts["blocked"] or 0,
                "skipped": counts["skipped"] or 0,
            },
            next_items,
        )

    def reconcile_translation_queue(self) -> int:
        self._sync_manifest_from_content()
        return self.store.reconcile_translation_queue()
