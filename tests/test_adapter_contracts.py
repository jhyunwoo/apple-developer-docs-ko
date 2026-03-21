from __future__ import annotations

import importlib

import pytest


def _optional_module(name: str):
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        pytest.skip(f"{name} is not implemented yet")


def test_docc_normalization_contract_when_adapter_exists():
    module = _optional_module("apple_developer_docs_ko.adapters.docc")
    normalize = getattr(module, "normalize_document", None)
    if normalize is None:
        pytest.skip("normalize_document() is not implemented yet")

    fixture = {
        "metadata": {"title": "MapKit"},
        "abstract": [{"type": "text", "text": "Work with maps."}],
        "references": {
            "doc://mapkit/article": {
                "title": "Map article",
                "url": "/documentation/MapKit/map-article",
            }
        },
        "primaryContentSections": [
            {
                "kind": "content",
                "content": [
                    {"type": "heading", "level": 2, "text": "Overview"},
                    {
                        "type": "paragraph",
                        "inlineContent": [
                            {"type": "text", "text": "Use "},
                            {"type": "codeVoice", "code": "MapKit"},
                            {"type": "text", "text": " in your app."},
                        ],
                    },
                ],
            }
        ],
    }

    page = normalize(route="/documentation/MapKit", document=fixture)
    assert page.title == "MapKit"
    assert any("Overview" in block.body for block in page.content_blocks)
    assert any("/documentation/MapKit/map-article" in link for link in page.discovered_links)


def test_archive_discovery_contract_when_adapter_exists():
    module = _optional_module("apple_developer_docs_ko.adapters.archive")
    parser = getattr(module, "parse_library_index", None)
    if parser is None:
        pytest.skip("parse_library_index() is not implemented yet")

    fixture = """
    {
      "documents": [
        ["Quick Start", "DTS1", 3, "2024-01-01", 0, 0, 0, 0, 0, "../qa/qa1/_index.html", 0, "2024-01-01", "iOS",],
        ["Map Guide", "DTS2", 3, "2024-01-02", 0, 0, 0, 0, 0, "../guide/index.html", 0, "2024-01-02", "macOS",]
      ],
    }
    """

    documents = parser(fixture)
    assert len(documents) == 2
    assert documents[0]["title"] == "Quick Start"
    assert documents[1]["url"].endswith("/guide/index.html")


def test_video_subtitle_contract_when_adapter_exists():
    module = _optional_module("apple_developer_docs_ko.adapters.videos")
    parse_tracks = getattr(module, "parse_subtitle_playlist", None)
    parse_vtt = getattr(module, "parse_webvtt", None)
    if parse_tracks is None or parse_vtt is None:
        pytest.skip("subtitle parsing helpers are not implemented yet")

    playlist = """#EXTM3U
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="English",LANGUAGE="en",URI="https://example.com/en.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",NAME="한국어",LANGUAGE="ko",URI="https://example.com/ko.m3u8"
"""
    vtt = """WEBVTT

00:00:01.000 --> 00:00:03.000
안녕하세요

00:00:04.000 --> 00:00:06.000
반갑습니다
"""

    tracks = parse_tracks(playlist)
    cues = parse_vtt(vtt)

    assert tracks["ko"]["name"] == "한국어"
    assert tracks["en"]["uri"] == "https://example.com/en.m3u8"
    assert cues[0]["text"] == "안녕하세요"
    assert cues[1]["start"] == "00:00:04.000"


def test_video_fetch_tolerates_unreachable_stream():
    module = _optional_module("apple_developer_docs_ko.adapters.videos")
    adapter_cls = getattr(module, "VideosAdapter", None)
    if adapter_cls is None:
        pytest.skip("VideosAdapter is not implemented yet")

    class FakeHttp:
        def exists(self, url: str, **kwargs) -> bool:
            return False

        def get_text(self, url: str, **kwargs) -> str:
            if url == "https://developer.apple.com/videos/play/wwdc2025/101":
                return """
                <html>
                  <head>
                    <title>Meet MapKit - WWDC25 - Videos - Apple Developer</title>
                    <meta property="og:video" content="https://stream.example/master.m3u8" />
                  </head>
                  <body>
                    <main>
                      <h1>Meet MapKit</h1>
                      <p>Build rich mapping experiences.</p>
                    </main>
                  </body>
                </html>
                """
            if url == "https://stream.example/master.m3u8":
                raise RuntimeError("stream host timed out")
            raise AssertionError(f"Unexpected URL: {url}")

    page = adapter_cls(FakeHttp()).fetch("/videos/play/wwdc2025/101")
    assert page.source_locale == "en-US"
    assert any(asset.url == "https://stream.example/master.m3u8" for asset in page.asset_links)
    assert all(block.kind != "video-transcript" for block in page.content_blocks)
