from __future__ import annotations

import json

from apple_developer_docs_ko.markdown_renderer import page_to_markdown, write_page_markdown
from apple_developer_docs_ko.site_builder import build_site


def test_page_to_markdown_renders_frontmatter_blocks_and_assets(sample_page):
    rendered = page_to_markdown(sample_page)

    assert rendered.startswith("---\nroute: /documentation/MapKit")
    assert "# MapKit" in rendered
    assert ":::note Note" in rendered
    assert ":::declaration swift" in rendered
    assert "https://docs-assets.developer.apple.com/example.png" in rendered
    assert "/__mirror__/docs-assets.developer.apple.com/example.png" in rendered


def test_write_page_markdown_and_build_site(tmp_path, sample_page):
    content_dir = tmp_path / "content"
    dist_dir = tmp_path / "dist"

    markdown_path = write_page_markdown(content_dir, sample_page)
    assert markdown_path == content_dir / "documentation" / "MapKit" / "index.md"
    assert markdown_path.read_text(encoding="utf-8").startswith("---")

    build_site(content_dir, dist_dir)

    html_path = dist_dir / "documentation" / "MapKit" / "index.html"
    search_index_path = dist_dir / "__site__" / "search-index.json"

    assert html_path.exists()
    html = html_path.read_text(encoding="utf-8")
    assert "<title>MapKit</title>" in html
    assert "<h1 id=\"mapkit\">MapKit</h1>" in html

    search_index = json.loads(search_index_path.read_text(encoding="utf-8"))
    assert {"route": "/documentation/MapKit", "title": "MapKit"} in search_index
