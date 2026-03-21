from __future__ import annotations

from apple_developer_docs_ko.models import AssetLink, ContentBlock, NormalizedPage, PageSourceRecord
from apple_developer_docs_ko.utils import text_hash
import pytest


@pytest.fixture
def sample_page() -> NormalizedPage:
    source_body = "# MapKit\n\nApple map content."
    return NormalizedPage(
        route="/documentation/MapKit",
        source_url="https://developer.apple.com/documentation/MapKit",
        source_locale="ko-KR",
        section="docc",
        content_type="symbol",
        title="MapKit",
        original_title="MapKit",
        source_hash=text_hash(source_body),
        canonical_source="official-ko",
        discovered_links=["/documentation/MapKit/Map"],
        asset_links=[
            AssetLink(
                url="https://docs-assets.developer.apple.com/example.png",
                local_path=".cache/assets/docs-assets.developer.apple.com/example.png",
                content_type="image/png",
                status="mirrored",
                sha256="abc123",
            )
        ],
        content_blocks=[
            ContentBlock(kind="markdown", body="# MapKit\n\nApple map content."),
            ContentBlock(
                kind="aside",
                body="Use the latest APIs.",
                metadata={"style": "note", "name": "Note"},
            ),
            ContentBlock(
                kind="declaration",
                body="struct MapKitView {}",
                metadata={"syntax": "swift"},
                translatable=False,
            ),
        ],
        source_variants=[
            PageSourceRecord(
                url="https://developer.apple.com/documentation/MapKit",
                locale="en-US",
                content_type="application/json",
                raw_text='{"metadata":{"title":"MapKit"}}',
            ),
            PageSourceRecord(
                url="https://developer.apple.com/kr/design/human-interface-guidelines",
                locale="ko-KR",
                content_type="text/html",
                raw_text="<html><body><main><h1>지도</h1></main></body></html>",
            ),
        ],
    )
