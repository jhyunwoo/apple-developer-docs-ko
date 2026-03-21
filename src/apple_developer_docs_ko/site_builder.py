from __future__ import annotations

from pathlib import Path
import json
import shutil

import markdown as md
import yaml

from .paths import route_to_dist_path


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="/__site__/site.css">
</head>
<body>
  <header class="site-header">
    <a href="/">Apple Developer Docs KO</a>
    <input id="site-search" type="search" placeholder="Search">
  </header>
  <main>
    <article class="doc">
      {body}
    </article>
  </main>
  <script src="/__site__/search.js"></script>
</body>
</html>
"""


SITE_CSS = """
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;margin:0;background:#fafafa;color:#111}
.site-header{display:flex;gap:1rem;align-items:center;padding:1rem 1.25rem;background:#fff;border-bottom:1px solid #ddd;position:sticky;top:0}
.site-header a{color:#111;text-decoration:none;font-weight:700}
#site-search{max-width:26rem;width:100%;padding:.65rem .8rem}
main{max-width:980px;margin:0 auto;padding:2rem 1.25rem 5rem}
.doc{background:#fff;padding:2rem;border:1px solid #e5e5e5;border-radius:14px}
pre{overflow:auto;background:#0f172a;color:#e2e8f0;padding:1rem;border-radius:10px}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
img{max-width:100%}
table{border-collapse:collapse;width:100%}
th,td{border:1px solid #d8d8d8;padding:.5rem;text-align:left}
blockquote{border-left:4px solid #cbd5e1;margin:1rem 0;padding:.25rem 1rem;background:#f8fafc}
"""


SEARCH_JS = """
async function loadIndex() {
  const response = await fetch('/__site__/search-index.json');
  return response.json();
}
document.getElementById('site-search')?.addEventListener('change', async (event) => {
  const query = event.target.value.trim().toLowerCase();
  if (!query) return;
  const index = await loadIndex();
  const hit = index.find((item) =>
    item.title.toLowerCase().includes(query) || item.route.toLowerCase().includes(query)
  );
  if (hit) {
    window.location.href = hit.route;
  }
});
"""


def _parse_frontmatter(content: str) -> tuple[dict, str]:
    if not content.startswith("---\n"):
        return {}, content
    _, rest = content.split("---\n", 1)
    frontmatter_text, body = rest.split("\n---\n", 1)
    return yaml.safe_load(frontmatter_text) or {}, body


def build_site(content_dir: Path, dist_dir: Path) -> None:
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir(parents=True, exist_ok=True)
    search_index: list[dict[str, str]] = []

    for md_path in sorted(content_dir.rglob("index.md")):
        raw = md_path.read_text(encoding="utf-8")
        frontmatter, body_md = _parse_frontmatter(raw)
        title = frontmatter.get("title") or frontmatter.get("original_title") or md_path.parent.name
        html = md.markdown(body_md, extensions=["tables", "fenced_code", "toc"])
        route = "/" + md_path.relative_to(content_dir).parent.as_posix().strip("/")
        if route == "/.":
            route = "/"
        dist_path = route_to_dist_path(dist_dir, route)
        dist_path.parent.mkdir(parents=True, exist_ok=True)
        dist_path.write_text(HTML_TEMPLATE.format(title=title, body=html), encoding="utf-8")
        search_index.append({"route": route, "title": title})

    site_dir = dist_dir / "__site__"
    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "site.css").write_text(SITE_CSS, encoding="utf-8")
    (site_dir / "search.js").write_text(SEARCH_JS, encoding="utf-8")
    (site_dir / "search-index.json").write_text(
        json.dumps(search_index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
