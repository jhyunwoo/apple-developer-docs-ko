from __future__ import annotations

from apple_developer_docs_ko.html_tools import parse_html_document


def test_parse_html_document_falls_back_to_meta_description_and_anchor_groups():
    html = """
    <html>
      <head>
        <title>Videos - Apple Developer</title>
        <meta name="Description" content="Browse Apple Developer videos." />
      </head>
      <body>
        <main>
          <div class="section-details">
            <section class="section-block">
              <h4>Featured</h4>
              <a href="/videos/play/wwdc2025/101/">
                <h5>Keynote</h5>
              </a>
              <a href="/videos/play/wwdc2025/102/">
                <h5>Platforms State of the Union</h5>
              </a>
            </section>
          </div>
        </main>
      </body>
    </html>
    """

    title, blocks, links, assets = parse_html_document(html, url="https://developer.apple.com/videos")

    assert title == "Videos - Apple Developer"
    assert any("Browse Apple Developer videos." in block.body for block in blocks)
    assert any(block.kind == "topic-grid" and "## Featured" in block.body for block in blocks)
    assert "/videos/play/wwdc2025/101" in links
    assert assets == []
