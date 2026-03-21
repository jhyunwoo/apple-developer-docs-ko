from __future__ import annotations

from pathlib import Path
import json

from apple_developer_docs_ko.assets import public_asset_url
from apple_developer_docs_ko.models import AssetLink
from apple_developer_docs_ko.paths import mirrored_asset_relpath, normalize_route, route_to_content_path, route_to_dist_path
from apple_developer_docs_ko.utils import clean_text, is_public_page_url, strip_trailing_commas


def test_archive_like_json_with_trailing_commas_can_be_cleaned():
    archive_fixture = """
    {
      "documents": [
        ["Quick Start", "DTS1", "../qa/qa1/_index.html",],
        ["Map Guide", "DTS2", "../guide/index.html",]
      ],
    }
    """

    parsed = json.loads(strip_trailing_commas(archive_fixture))
    assert parsed["documents"][0][0] == "Quick Start"
    assert parsed["documents"][1][2] == "../guide/index.html"


def test_public_url_filtering_and_path_helpers():
    assert is_public_page_url("https://developer.apple.com/documentation/")
    assert not is_public_page_url("https://developer.apple.com/search/?q=swift")
    assert not is_public_page_url("https://developer.apple.com/account/")

    assert normalize_route("documentation/MapKit/") == "/documentation/MapKit"
    assert route_to_content_path(Path("/tmp/content"), "/documentation/MapKit") == Path(
        "/tmp/content/documentation/MapKit/index.md"
    )
    assert route_to_dist_path(Path("/tmp/dist"), "/documentation/MapKit") == Path(
        "/tmp/dist/documentation/MapKit/index.html"
    )
    assert mirrored_asset_relpath("https://events-delivery.apple.com/video/master.m3u8") == Path(
        "events-delivery.apple.com/video/master.m3u8"
    )


def test_clean_text_and_public_asset_url():
    assert clean_text("  A&nbsp; B \n C  ") == "A B C"

    mirrored = AssetLink(
        url="https://docs-assets.developer.apple.com/example.png",
        local_path=".cache/assets/docs-assets.developer.apple.com/example.png",
    )
    external = AssetLink(url="https://developer.apple.com/asset.pdf")

    assert public_asset_url(mirrored) == "/__mirror__/docs-assets.developer.apple.com/example.png"
    assert public_asset_url(external) == "https://developer.apple.com/asset.pdf"
