from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable

from .models import AssetLink, NormalizedPage, PageSourceRecord, utc_now


SCHEMA = """
CREATE TABLE IF NOT EXISTS pages (
    route TEXT PRIMARY KEY,
    source_url TEXT NOT NULL,
    source_locale TEXT NOT NULL,
    section TEXT NOT NULL,
    content_type TEXT NOT NULL,
    title TEXT NOT NULL,
    original_title TEXT NOT NULL,
    source_hash TEXT NOT NULL,
    canonical_source TEXT NOT NULL,
    last_crawled_at TEXT NOT NULL,
    last_translated_at TEXT,
    removed_at TEXT
);

CREATE TABLE IF NOT EXISTS page_sources (
    route TEXT NOT NULL,
    url TEXT NOT NULL,
    locale TEXT NOT NULL,
    content_type TEXT NOT NULL,
    source_hash TEXT NOT NULL,
    raw_cache_path TEXT,
    PRIMARY KEY(route, url)
);

CREATE TABLE IF NOT EXISTS page_links (
    route TEXT NOT NULL,
    target_route TEXT NOT NULL,
    PRIMARY KEY(route, target_route)
);

CREATE TABLE IF NOT EXISTS assets (
    url TEXT PRIMARY KEY,
    local_path TEXT,
    content_type TEXT,
    status TEXT NOT NULL,
    last_seen_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS asset_revisions (
    url TEXT NOT NULL,
    sha256 TEXT,
    local_path TEXT,
    content_type TEXT,
    created_at TEXT NOT NULL,
    PRIMARY KEY(url, created_at)
);

CREATE TABLE IF NOT EXISTS translations (
    route TEXT PRIMARY KEY,
    translator TEXT NOT NULL,
    source_hash TEXT NOT NULL,
    translated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sync_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL,
    sections TEXT NOT NULL,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS translation_queue (
    route TEXT PRIMARY KEY,
    section TEXT NOT NULL,
    ordinal INTEGER NOT NULL,
    status TEXT NOT NULL,
    source_locale TEXT,
    title TEXT,
    discovered_at TEXT NOT NULL,
    last_attempted_at TEXT,
    translated_at TEXT,
    notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_translation_queue_status_ordinal
ON translation_queue(status, ordinal);

CREATE TABLE IF NOT EXISTS discovery_frontier (
    section TEXT NOT NULL,
    route TEXT NOT NULL,
    ordinal INTEGER NOT NULL,
    discovered_from TEXT,
    attempts INTEGER NOT NULL DEFAULT 0,
    last_error TEXT,
    expanded_at TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    PRIMARY KEY(section, route)
);

CREATE INDEX IF NOT EXISTS idx_discovery_frontier_section_expanded
ON discovery_frontier(section, expanded_at, ordinal);
"""


class ManifestStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    @contextmanager
    def transaction(self):
        try:
            yield
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    def start_sync_run(self, sections: list[str]) -> int:
        cursor = self.conn.execute(
            "INSERT INTO sync_runs(started_at, status, sections) VALUES (?, ?, ?)",
            (utc_now(), "running", ",".join(sections)),
        )
        self.conn.commit()
        return int(cursor.lastrowid)

    def finish_sync_run(self, run_id: int, *, status: str, notes: str | None = None) -> None:
        self.conn.execute(
            "UPDATE sync_runs SET completed_at = ?, status = ?, notes = ? WHERE id = ?",
            (utc_now(), status, notes, run_id),
        )
        self.conn.commit()

    def upsert_page(self, page: NormalizedPage) -> None:
        with self.transaction():
            self.conn.execute(
                """
                INSERT INTO pages(
                    route, source_url, source_locale, section, content_type, title,
                    original_title, source_hash, canonical_source, last_crawled_at,
                    last_translated_at, removed_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
                ON CONFLICT(route) DO UPDATE SET
                    source_url=excluded.source_url,
                    source_locale=excluded.source_locale,
                    section=excluded.section,
                    content_type=excluded.content_type,
                    title=excluded.title,
                    original_title=excluded.original_title,
                    source_hash=excluded.source_hash,
                    canonical_source=excluded.canonical_source,
                    last_crawled_at=excluded.last_crawled_at,
                    last_translated_at=excluded.last_translated_at,
                    removed_at=NULL
                """,
                (
                    page.route,
                    page.source_url,
                    page.source_locale,
                    page.section,
                    page.content_type,
                    page.title,
                    page.original_title,
                    page.source_hash,
                    page.canonical_source,
                    page.last_crawled_at,
                    page.last_translated_at,
                ),
            )
            self.conn.execute("DELETE FROM page_links WHERE route = ?", (page.route,))
            for target in page.discovered_links:
                self.conn.execute(
                    "INSERT OR IGNORE INTO page_links(route, target_route) VALUES (?, ?)",
                    (page.route, target),
                )
            for source in page.source_variants:
                self.upsert_page_source(page.route, source)
            for asset in page.asset_links:
                self.upsert_asset(asset)

    def upsert_page_source(self, route: str, source: PageSourceRecord) -> None:
        self.conn.execute(
            """
            INSERT INTO page_sources(route, url, locale, content_type, source_hash, raw_cache_path)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(route, url) DO UPDATE SET
                locale=excluded.locale,
                content_type=excluded.content_type,
                source_hash=excluded.source_hash
            """,
            (route, source.url, source.locale, source.content_type, source.source_hash, None),
        )

    def upsert_asset(self, asset: AssetLink) -> None:
        now = utc_now()
        self.conn.execute(
            """
            INSERT INTO assets(url, local_path, content_type, status, last_seen_at)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                local_path=excluded.local_path,
                content_type=excluded.content_type,
                status=excluded.status,
                last_seen_at=excluded.last_seen_at
            """,
            (asset.url, asset.local_path, asset.content_type, asset.status, now),
        )
        if asset.sha256 or asset.local_path:
            self.conn.execute(
                """
                INSERT OR IGNORE INTO asset_revisions(url, sha256, local_path, content_type, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                (asset.url, asset.sha256, asset.local_path, asset.content_type, now),
            )

    def mark_translation(self, route: str, translator: str, source_hash: str) -> None:
        self.conn.execute(
            """
            INSERT INTO translations(route, translator, source_hash, translated_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(route) DO UPDATE SET
                translator=excluded.translator,
                source_hash=excluded.source_hash,
                translated_at=excluded.translated_at
            """,
            (route, translator, source_hash, utc_now()),
        )
        self.conn.commit()

    def is_translation_current(self, route: str, source_hash: str) -> bool:
        row = self.conn.execute(
            "SELECT 1 FROM translations WHERE route = ? AND source_hash = ?",
            (route, source_hash),
        ).fetchone()
        return row is not None

    def tombstone_missing_pages(self, seen_routes: Iterable[str], *, sections: list[str]) -> None:
        seen = set(seen_routes)
        section_qmarks = ",".join("?" for _ in sections)
        rows = self.conn.execute(
            f"SELECT route FROM pages WHERE section IN ({section_qmarks}) AND removed_at IS NULL",
            tuple(sections),
        ).fetchall()
        now = utc_now()
        with self.transaction():
            for row in rows:
                route = row["route"]
                if route in seen:
                    continue
                self.conn.execute(
                    "UPDATE pages SET removed_at = ? WHERE route = ?",
                    (now, route),
                )

    def iter_pages(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            "SELECT * FROM pages WHERE removed_at IS NULL ORDER BY route"
        ).fetchall()

    def upsert_translation_queue_entries(self, entries: list[dict[str, object]]) -> int:
        inserted = 0
        with self.transaction():
            for entry in entries:
                existing = self.conn.execute(
                    "SELECT status, translated_at, notes FROM translation_queue WHERE route = ?",
                    (entry["route"],),
                ).fetchone()
                if existing is None:
                    inserted += 1
                status = entry["status"]
                translated_at = entry.get("translated_at")
                notes = entry.get("notes")
                if existing is not None and existing["status"] in {"translated", "blocked", "skipped"}:
                    status = existing["status"]
                    translated_at = existing["translated_at"]
                    notes = existing["notes"]
                self.conn.execute(
                    """
                    INSERT INTO translation_queue(
                        route, section, ordinal, status, source_locale, title,
                        discovered_at, last_attempted_at, translated_at, notes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(route) DO UPDATE SET
                        section=excluded.section,
                        ordinal=excluded.ordinal,
                        status=excluded.status,
                        source_locale=excluded.source_locale,
                        title=excluded.title,
                        last_attempted_at=excluded.last_attempted_at,
                        translated_at=excluded.translated_at,
                        notes=excluded.notes
                    """,
                    (
                        entry["route"],
                        entry["section"],
                        entry["ordinal"],
                        status,
                        entry.get("source_locale"),
                        entry.get("title"),
                        entry["discovered_at"],
                        entry.get("last_attempted_at"),
                        translated_at,
                        notes,
                    ),
                )
        return inserted

    def clear_translation_queue(self) -> None:
        self.conn.execute("DELETE FROM translation_queue")
        self.conn.commit()

    def clear_discovery_frontier(self, *, sections: list[str] | None = None) -> None:
        if sections:
            qmarks = ",".join("?" for _ in sections)
            self.conn.execute(
                f"DELETE FROM discovery_frontier WHERE section IN ({qmarks})",
                tuple(sections),
            )
        else:
            self.conn.execute("DELETE FROM discovery_frontier")
        self.conn.commit()

    def get_discovery_frontier_counts(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT
                section,
                COUNT(*) AS total,
                SUM(CASE WHEN expanded_at IS NOT NULL THEN 1 ELSE 0 END) AS expanded,
                SUM(CASE WHEN expanded_at IS NULL THEN 1 ELSE 0 END) AS pending
            FROM discovery_frontier
            GROUP BY section
            ORDER BY section
            """
        ).fetchall()

    def discovery_frontier_exists(self, section: str, route: str) -> bool:
        row = self.conn.execute(
            "SELECT 1 FROM discovery_frontier WHERE section = ? AND route = ?",
            (section, route),
        ).fetchone()
        return row is not None

    def insert_discovery_frontier_routes(
        self,
        *,
        section: str,
        routes: list[str],
        discovered_from: str | None = None,
    ) -> int:
        if not routes:
            return 0
        inserted = 0
        max_row = self.conn.execute(
            "SELECT COALESCE(MAX(ordinal), 0) AS max_ordinal FROM discovery_frontier WHERE section = ?",
            (section,),
        ).fetchone()
        ordinal = (max_row["max_ordinal"] or 0) + 1
        now = utc_now()
        with self.transaction():
            for route in routes:
                existing = self.conn.execute(
                    "SELECT 1 FROM discovery_frontier WHERE section = ? AND route = ?",
                    (section, route),
                ).fetchone()
                if existing is not None:
                    continue
                self.conn.execute(
                    """
                    INSERT INTO discovery_frontier(
                        section, route, ordinal, discovered_from, attempts,
                        last_error, expanded_at, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, 0, NULL, NULL, ?, ?)
                    """,
                    (section, route, ordinal, discovered_from, now, now),
                )
                inserted += 1
                ordinal += 1
        return inserted

    def get_pending_discovery_frontier(self, *, section: str, limit: int) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT section, route, ordinal, discovered_from, attempts, last_error
            FROM discovery_frontier
            WHERE section = ? AND expanded_at IS NULL
            ORDER BY ordinal
            LIMIT ?
            """,
            (section, limit),
        ).fetchall()

    def mark_discovery_frontier_expanded(
        self,
        *,
        section: str,
        route: str,
        last_error: str | None = None,
    ) -> None:
        now = utc_now()
        self.conn.execute(
            """
            UPDATE discovery_frontier
            SET expanded_at = ?,
                updated_at = ?,
                attempts = attempts + 1,
                last_error = ?
            WHERE section = ? AND route = ?
            """,
            (now, now, last_error, section, route),
        )
        self.conn.commit()

    def set_translation_queue_status(
        self,
        route: str,
        *,
        status: str,
        notes: str | None = None,
        translated_at: str | None = None,
    ) -> None:
        self.conn.execute(
            """
            UPDATE translation_queue
            SET status = ?,
                notes = ?,
                last_attempted_at = ?,
                translated_at = ?
            WHERE route = ?
            """,
            (status, notes, utc_now(), translated_at, route),
        )
        self.conn.commit()

    def get_translation_queue_summary(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT status, COUNT(*) AS count
            FROM translation_queue
            GROUP BY status
            ORDER BY CASE status
                WHEN 'translated' THEN 0
                WHEN 'queued' THEN 1
                WHEN 'in_progress' THEN 2
                WHEN 'blocked' THEN 3
                WHEN 'skipped' THEN 4
                ELSE 9
            END
            """
        ).fetchall()

    def get_next_translation_queue_items(self, limit: int = 10) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT route, section, ordinal, status, source_locale, title
            FROM translation_queue
            WHERE status = 'queued'
            ORDER BY ordinal
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

    def get_translation_queue_counts(self) -> sqlite3.Row:
        return self.conn.execute(
            """
            SELECT
                COUNT(*) AS total,
                SUM(CASE WHEN status = 'translated' THEN 1 ELSE 0 END) AS translated,
                SUM(CASE WHEN status = 'queued' THEN 1 ELSE 0 END) AS queued,
                SUM(CASE WHEN status = 'in_progress' THEN 1 ELSE 0 END) AS in_progress,
                SUM(CASE WHEN status = 'blocked' THEN 1 ELSE 0 END) AS blocked,
                SUM(CASE WHEN status = 'skipped' THEN 1 ELSE 0 END) AS skipped
            FROM translation_queue
            """
        ).fetchone()

    def reconcile_translation_queue(self) -> int:
        rows = self.conn.execute("SELECT route FROM translation_queue ORDER BY ordinal").fetchall()
        updated = 0
        with self.transaction():
            for row in rows:
                route = row["route"]
                page = self.conn.execute(
                    "SELECT source_locale, last_crawled_at, last_translated_at, removed_at FROM pages WHERE route = ?",
                    (route,),
                ).fetchone()
                translation = self.conn.execute(
                    "SELECT translator, translated_at FROM translations WHERE route = ?",
                    (route,),
                ).fetchone()
                if page is None or page["removed_at"] is not None:
                    continue
                status = None
                translated_at = None
                if page["source_locale"].startswith("ko"):
                    status = "translated"
                    translated_at = page["last_translated_at"] or page["last_crawled_at"]
                elif translation is not None and translation["translator"] != "identity":
                    status = "translated"
                    translated_at = translation["translated_at"]
                if status is None:
                    continue
                self.conn.execute(
                    """
                    UPDATE translation_queue
                    SET status = ?, translated_at = ?, last_attempted_at = ?
                    WHERE route = ?
                    """,
                    (status, translated_at, utc_now(), route),
                )
                updated += 1
        return updated
