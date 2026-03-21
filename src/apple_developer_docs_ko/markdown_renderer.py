from __future__ import annotations

from pathlib import Path
import yaml

from .assets import public_asset_url
from .models import ContentBlock, NormalizedPage
from .paths import route_to_content_path


def _render_block(block: ContentBlock) -> str:
    if block.kind == "aside":
        style = block.metadata.get("style", "note")
        name = block.metadata.get("name", style.title())
        return f":::{style} {name}\n{block.body.rstrip()}\n:::\n"
    if block.kind == "declaration":
        syntax = block.metadata.get("syntax", "")
        return f":::declaration {syntax}\n{block.body.rstrip()}\n:::\n"
    if block.kind == "availability":
        return f":::availability\n{block.body.rstrip()}\n:::\n"
    if block.kind == "topic-grid":
        return f":::topic-grid\n{block.body.rstrip()}\n:::\n"
    if block.kind == "term-list":
        return f":::term-list\n{block.body.rstrip()}\n:::\n"
    if block.kind == "video-transcript":
        return f":::video-transcript\n{block.body.rstrip()}\n:::\n"
    if block.kind == "asset-list":
        return f":::asset-list\n{block.body.rstrip()}\n:::\n"
    return block.body.rstrip() + "\n"


def page_to_markdown(page: NormalizedPage) -> str:
    frontmatter = yaml.safe_dump(page.frontmatter(), allow_unicode=True, sort_keys=False).strip()
    body = "\n\n".join(_render_block(block).rstrip() for block in page.content_blocks if block.body.strip())
    if page.asset_links:
        items = []
        for asset in page.asset_links:
            items.append(f"- `{asset.url}` -> `{public_asset_url(asset)}` ({asset.status})")
        body = body.rstrip() + "\n\n" + _render_block(ContentBlock(kind="asset-list", body="\n".join(items)))
    return f"---\n{frontmatter}\n---\n\n{body.strip()}\n"


def write_page_markdown(content_dir: Path, page: NormalizedPage) -> Path:
    target = route_to_content_path(content_dir, page.route)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page_to_markdown(page), encoding="utf-8")
    return target
