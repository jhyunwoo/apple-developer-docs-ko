from __future__ import annotations

from apple_developer_docs_ko.store import ManifestStore


def test_manifest_store_upserts_page_and_related_records(tmp_path, sample_page):
    store = ManifestStore(tmp_path / "state" / "manifest.sqlite")

    store.upsert_page(sample_page)
    page_row = store.conn.execute("SELECT * FROM pages WHERE route = ?", (sample_page.route,)).fetchone()
    source_rows = store.conn.execute(
        "SELECT * FROM page_sources WHERE route = ? ORDER BY locale",
        (sample_page.route,),
    ).fetchall()
    link_rows = store.conn.execute(
        "SELECT target_route FROM page_links WHERE route = ?",
        (sample_page.route,),
    ).fetchall()
    asset_row = store.conn.execute(
        "SELECT * FROM assets WHERE url = ?",
        (sample_page.asset_links[0].url,),
    ).fetchone()

    assert page_row is not None
    assert page_row["title"] == "MapKit"
    assert page_row["canonical_source"] == "official-ko"
    assert [row["locale"] for row in source_rows] == ["en-US", "ko-KR"]
    assert [row["target_route"] for row in link_rows] == ["/documentation/MapKit/Map"]
    assert asset_row["status"] == "mirrored"
    assert asset_row["local_path"].endswith("example.png")


def test_manifest_store_tracks_translation_and_tombstones(tmp_path, sample_page):
    store = ManifestStore(tmp_path / "state" / "manifest.sqlite")
    store.upsert_page(sample_page)

    assert not store.is_translation_current(sample_page.route, sample_page.source_hash)
    store.mark_translation(sample_page.route, "identity", sample_page.source_hash)
    assert store.is_translation_current(sample_page.route, sample_page.source_hash)

    store.tombstone_missing_pages([], sections=["docc"])
    row = store.conn.execute("SELECT removed_at FROM pages WHERE route = ?", (sample_page.route,)).fetchone()
    assert row["removed_at"] is not None


def test_manifest_store_records_sync_runs(tmp_path):
    store = ManifestStore(tmp_path / "state" / "manifest.sqlite")

    run_id = store.start_sync_run(["docc", "videos"])
    store.finish_sync_run(run_id, status="completed", notes="smoke")

    row = store.conn.execute("SELECT * FROM sync_runs WHERE id = ?", (run_id,)).fetchone()
    assert row["status"] == "completed"
    assert row["sections"] == "docc,videos"
    assert row["notes"] == "smoke"


def test_manifest_store_translation_queue_tracks_progress(tmp_path, sample_page):
    store = ManifestStore(tmp_path / "state" / "manifest.sqlite")

    inserted = store.upsert_translation_queue_entries(
        [
            {
                "route": sample_page.route,
                "section": "docc",
                "ordinal": 1,
                "status": "queued",
                "source_locale": sample_page.source_locale,
                "title": sample_page.title,
                "discovered_at": sample_page.last_crawled_at,
            },
            {
                "route": "/documentation/MapKit/Map",
                "section": "docc",
                "ordinal": 2,
                "status": "queued",
                "source_locale": "en-US",
                "title": "Map",
                "discovered_at": sample_page.last_crawled_at,
            },
        ]
    )

    assert inserted == 2
    counts = store.get_translation_queue_counts()
    assert counts["total"] == 2
    assert counts["queued"] == 2

    store.upsert_page(sample_page)
    updated = store.reconcile_translation_queue()

    assert updated == 1
    summary = {row["status"]: row["count"] for row in store.get_translation_queue_summary()}
    assert summary["translated"] == 1
    next_items = store.get_next_translation_queue_items(limit=5)
    assert [row["route"] for row in next_items] == ["/documentation/MapKit/Map"]


def test_manifest_store_tracks_discovery_frontier(tmp_path):
    store = ManifestStore(tmp_path / "state" / "manifest.sqlite")

    inserted = store.insert_discovery_frontier_routes(
        section="docc",
        routes=["/documentation/MapKit", "/documentation/MusicKit"],
    )

    assert inserted == 2
    pending = store.get_pending_discovery_frontier(section="docc", limit=10)
    assert [row["route"] for row in pending] == ["/documentation/MapKit", "/documentation/MusicKit"]

    store.mark_discovery_frontier_expanded(section="docc", route="/documentation/MapKit")
    counts = {row["section"]: (row["total"], row["expanded"], row["pending"]) for row in store.get_discovery_frontier_counts()}

    assert counts["docc"] == (2, 1, 1)
