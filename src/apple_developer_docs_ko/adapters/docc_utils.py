from __future__ import annotations

from urllib.parse import urlparse

from ..models import AssetLink, ContentBlock
from ..utils import absolutize, clean_text, dedupe


def _reference_label(ref: dict) -> str:
    for key in ("title", "name", "navigatorTitle", "roleHeading", "url"):
        value = ref.get(key)
        if value:
            return clean_text(str(value))
    return "Link"


def render_inline(items: list[dict] | None, references: dict[str, dict]) -> str:
    if not items:
        return ""
    parts: list[str] = []
    for item in items:
        item_type = item.get("type")
        if item_type == "text":
            parts.append(item.get("text", ""))
        elif item_type == "codeVoice":
            parts.append(f"`{item.get('code', '')}`")
        elif item_type == "reference":
            ref = references.get(item.get("identifier", ""), {})
            url = absolutize(ref.get("url", ""))
            parts.append(f"[{_reference_label(ref)}]({url})")
        elif item_type == "emphasis":
            parts.append(f"*{render_inline(item.get('inlineContent'), references)}*")
        elif item_type == "strong":
            parts.append(f"**{render_inline(item.get('inlineContent'), references)}**")
        elif item_type == "link":
            dest = item.get("destination") or item.get("url") or ""
            parts.append(f"[{render_inline(item.get('inlineContent'), references)}]({absolutize(dest)})")
        elif item_type == "image":
            ref = references.get(item.get("identifier", ""), {})
            url = absolutize(ref.get("url", ""))
            alt = ref.get("alt") or ref.get("title") or ""
            parts.append(f"![{alt}]({url})")
        else:
            parts.append(item.get("text") or item.get("code") or "")
    return clean_text("".join(parts))


def render_content_items(items: list[dict], references: dict[str, dict]) -> list[ContentBlock]:
    blocks: list[ContentBlock] = []
    for item in items:
        item_type = item.get("type")
        if item_type == "heading":
            level = int(item.get("level", 2))
            blocks.append(ContentBlock(kind="markdown", body=f"{'#' * level} {item.get('text', '').strip()}"))
        elif item_type == "paragraph":
            body = render_inline(item.get("inlineContent"), references)
            if body:
                blocks.append(ContentBlock(kind="markdown", body=body))
        elif item_type == "codeListing":
            code = "\n".join(item.get("code", []))
            syntax = item.get("syntax", "")
            blocks.append(ContentBlock(kind="markdown", body=f"```{syntax}\n{code}\n```", translatable=False))
        elif item_type == "unorderedList":
            lines = []
            for child in item.get("items", []):
                content = child.get("content", [])
                rendered = "\n".join(
                    block.body for block in render_content_items(content, references) if block.body
                )
                if rendered:
                    lines.append(f"- {rendered}")
            if lines:
                blocks.append(ContentBlock(kind="markdown", body="\n".join(lines)))
        elif item_type == "orderedList":
            lines = []
            for idx, child in enumerate(item.get("items", []), start=1):
                content = child.get("content", [])
                rendered = "\n".join(
                    block.body for block in render_content_items(content, references) if block.body
                )
                if rendered:
                    lines.append(f"{idx}. {rendered}")
            if lines:
                blocks.append(ContentBlock(kind="markdown", body="\n".join(lines)))
        elif item_type == "aside":
            inner_blocks = render_content_items(item.get("content", []), references)
            body = "\n\n".join(block.body for block in inner_blocks if block.body)
            blocks.append(
                ContentBlock(
                    kind="aside",
                    body=body,
                    metadata={"style": item.get("style", "note"), "name": item.get("name", "Note")},
                )
            )
        elif item_type == "table":
            rows = item.get("rows", [])
            matrix = []
            for row in rows:
                cells = []
                for cell in row:
                    cell_text_parts = []
                    for block in cell:
                        if block.get("type") == "paragraph":
                            cell_text_parts.append(render_inline(block.get("inlineContent"), references))
                    cells.append(clean_text(" ".join(cell_text_parts)))
                matrix.append(cells)
            if matrix:
                header = matrix[0]
                divider = ["---"] * len(header)
                body = ["| " + " | ".join(header) + " |", "| " + " | ".join(divider) + " |"]
                for row in matrix[1:]:
                    padded = row + [""] * (len(header) - len(row))
                    body.append("| " + " | ".join(padded[: len(header)]) + " |")
                blocks.append(ContentBlock(kind="markdown", body="\n".join(body)))
        elif item_type == "termList":
            lines = []
            for entry in item.get("items", []):
                term = render_inline(entry.get("term", {}).get("inlineContent"), references)
                definition_blocks = render_content_items(entry.get("definition", {}).get("content", []), references)
                definition = " ".join(block.body for block in definition_blocks if block.body)
                lines.append(f"{term}: {definition}")
            if lines:
                blocks.append(ContentBlock(kind="term-list", body="\n".join(lines)))
    return blocks


def collect_discovered_routes(doc: dict) -> list[str]:
    refs = doc.get("references", {})
    routes: list[str] = []
    for ref in refs.values():
        url = ref.get("url")
        if not url:
            continue
        parsed = urlparse(url)
        if parsed.path.startswith(("/documentation/", "/design/")):
            routes.append(parsed.path.rstrip("/"))
    return dedupe(routes)


def collect_assets(doc: dict) -> list[AssetLink]:
    assets: list[AssetLink] = []
    for ref in doc.get("references", {}).values():
        url = ref.get("url")
        if not url:
            continue
        absolute = absolutize(url)
        parsed = urlparse(absolute)
        if parsed.netloc and not parsed.path.startswith(("/documentation/", "/design/")):
            if any(parsed.path.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".svg", ".pdf", ".zip")):
                assets.append(AssetLink(url=absolute))
    return assets
