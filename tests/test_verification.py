from __future__ import annotations

from apple_developer_docs_ko.config import Settings
from apple_developer_docs_ko.markdown_renderer import write_page_markdown
from apple_developer_docs_ko.site_builder import build_site
from apple_developer_docs_ko.store import ManifestStore
from apple_developer_docs_ko.verification import format_report, verify_outputs


def test_verify_outputs_passes_for_consistent_korean_page(tmp_path, sample_page):
    settings = Settings.from_env(tmp_path)
    settings.ensure_directories()
    sample_page.content_blocks[0].body = "# MapKit\n\n지도 콘텐츠입니다."
    sample_page.content_blocks[1].body = "최신 API를 사용하십시오."

    store = ManifestStore(settings.manifest_path)
    try:
        store.upsert_page(sample_page)
    finally:
        store.close()

    write_page_markdown(settings.content_dir, sample_page)
    build_site(settings.content_dir, settings.dist_dir)

    report = verify_outputs(settings)

    assert report.ok
    assert "Verification passed with no findings." in format_report(report)


def test_verify_outputs_flags_missing_and_untranslated_outputs(tmp_path, sample_page):
    settings = Settings.from_env(tmp_path)
    settings.ensure_directories()

    sample_page.source_locale = "en-US"
    sample_page.canonical_source = "machine-translation"

    store = ManifestStore(settings.manifest_path)
    try:
        store.upsert_page(sample_page)
        store.mark_translation(sample_page.route, "identity", sample_page.source_hash)
    finally:
        store.close()

    report = verify_outputs(settings)
    codes = {finding.code for finding in report.findings}

    assert not report.ok
    assert "missing-markdown" in codes

    write_page_markdown(settings.content_dir, sample_page)
    build_site(settings.content_dir, settings.dist_dir)

    report = verify_outputs(settings)
    codes = {finding.code for finding in report.findings}

    assert "identity-translation" in codes
