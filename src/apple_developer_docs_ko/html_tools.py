from __future__ import annotations

from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.parse import urljoin, urlparse
import re

from .models import AssetLink, ContentBlock
from .utils import clean_text, dedupe, is_public_page_url, is_same_site_url


ASSET_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".pdf",
    ".zip",
    ".mov",
    ".mp4",
    ".m3u8",
    ".vtt",
    ".webvtt",
)


def _inline_to_markdown(node: Tag | NavigableString, base_url: str) -> str:
    if isinstance(node, NavigableString):
        return str(node)
    if node.name == "br":
        return "  \n"
    if node.name == "code":
        return f"`{clean_text(node.get_text(' ', strip=True))}`"
    if node.name in {"strong", "b"}:
        return f"**{''.join(_inline_to_markdown(child, base_url) for child in node.children).strip()}**"
    if node.name in {"em", "i"}:
        return f"*{''.join(_inline_to_markdown(child, base_url) for child in node.children).strip()}*"
    if node.name == "a":
        href = node.get("href") or ""
        text = clean_text(node.get_text(" ", strip=True)) or href
        return f"[{text}]({urljoin(base_url, href)})"
    if node.name == "img":
        src = node.get("src") or ""
        alt = node.get("alt") or ""
        return f"![{alt}]({urljoin(base_url, src)})"
    return "".join(_inline_to_markdown(child, base_url) for child in node.children)


def _table_to_markdown(table: Tag, base_url: str) -> str:
    rows = []
    for tr in table.select("tr"):
        cells = tr.find_all(["th", "td"])
        rows.append([clean_text(_inline_to_markdown(cell, base_url)) for cell in cells])
    if not rows:
        return ""
    header = rows[0]
    divider = ["---"] * len(header)
    body = rows[1:]
    rendered = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(divider) + " |",
    ]
    for row in body:
        padded = row + [""] * (len(header) - len(row))
        rendered.append("| " + " | ".join(padded[: len(header)]) + " |")
    return "\n".join(rendered)


def _list_to_markdown(node: Tag, base_url: str, *, ordered: bool) -> str:
    items = []
    for idx, li in enumerate(node.find_all("li", recursive=False), start=1):
        prefix = f"{idx}." if ordered else "-"
        body = clean_text(_inline_to_markdown(li, base_url))
        if body:
            items.append(f"{prefix} {body}")
    return "\n".join(items)


def _pre_to_markdown(node: Tag) -> str:
    code = node.get_text("\n", strip=False).rstrip()
    language = ""
    code_child = node.find("code")
    if code_child:
        classes = code_child.get("class") or []
        for css_class in classes:
            if css_class.startswith("language-"):
                language = css_class.removeprefix("language-")
                break
    return f"```{language}\n{code}\n```"


def _meta_description(soup: BeautifulSoup) -> str:
    meta = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
    if meta and meta.get("content"):
        return clean_text(meta["content"])
    return ""


def _anchor_group_blocks(soup: BeautifulSoup, *, base_url: str) -> list[ContentBlock]:
    container = soup.select_one("main") or soup.select_one("article") or soup.body
    if container is None:
        return []
    blocks: list[ContentBlock] = []
    seen_signatures: set[tuple[str, tuple[str, ...]]] = set()
    for candidate in container.find_all(["section", "div"]):
        heading = candidate.find(["h1", "h2", "h3", "h4", "h5", "h6"])
        if heading is None:
            continue
        heading_text = clean_text(heading.get_text(" ", strip=True))
        if not heading_text:
            continue
        items: list[str] = []
        seen_links: set[str] = set()
        for anchor in candidate.find_all("a", href=True):
            href = urljoin(base_url, anchor.get("href") or "")
            text = clean_text(anchor.get_text(" ", strip=True))
            if not href or not text or text == heading_text:
                continue
            if href in seen_links:
                continue
            seen_links.add(href)
            items.append(f"- [{text}]({href})")
        if len(items) < 2:
            continue
        signature = (heading_text, tuple(sorted(seen_links)))
        if signature in seen_signatures:
            continue
        seen_signatures.add(signature)
        blocks.append(ContentBlock(kind="topic-grid", body=f"## {heading_text}\n" + "\n".join(items)))
    return blocks


def soup_to_content_blocks(soup: BeautifulSoup, *, base_url: str) -> list[ContentBlock]:
    container = soup.select_one("main") or soup.select_one("article") or soup.body
    if container is None:
        return []

    for selector in ("script", "style", "nav", "footer", "header.form", ".globalnav", ".footer"):
        for node in container.select(selector):
            node.decompose()

    blocks: list[ContentBlock] = []
    for child in container.children:
        if isinstance(child, NavigableString):
            continue
        if not isinstance(child, Tag):
            continue
        if child.name in {"section", "article", "main", "div"} and not clean_text(child.get_text(" ", strip=True)):
            continue
        if child.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(child.name[1])
            blocks.append(ContentBlock(kind="markdown", body=f"{'#' * level} {clean_text(child.get_text(' ', strip=True))}"))
        elif child.name == "p":
            text = clean_text(_inline_to_markdown(child, base_url))
            if text:
                blocks.append(ContentBlock(kind="markdown", body=text))
        elif child.name == "blockquote":
            text = clean_text(_inline_to_markdown(child, base_url))
            if text:
                blocks.append(ContentBlock(kind="aside", body=text, metadata={"style": "note", "name": "Quote"}))
        elif child.name == "pre":
            blocks.append(ContentBlock(kind="markdown", body=_pre_to_markdown(child), translatable=False))
        elif child.name == "table":
            table = _table_to_markdown(child, base_url)
            if table:
                blocks.append(ContentBlock(kind="markdown", body=table))
        elif child.name == "ul":
            rendered = _list_to_markdown(child, base_url, ordered=False)
            if rendered:
                blocks.append(ContentBlock(kind="markdown", body=rendered))
        elif child.name == "ol":
            rendered = _list_to_markdown(child, base_url, ordered=True)
            if rendered:
                blocks.append(ContentBlock(kind="markdown", body=rendered))
        elif child.name in {"section", "article", "main", "div"}:
            inner = soup_to_content_blocks(BeautifulSoup(str(child), "html.parser"), base_url=base_url)
            blocks.extend(inner)
        elif child.name == "img":
            src = child.get("src")
            if src:
                blocks.append(
                    ContentBlock(
                        kind="markdown",
                        body=f"![{child.get('alt', '')}]({urljoin(base_url, src)})",
                        translatable=False,
                    )
                )
    return blocks


def extract_links_and_assets(soup: BeautifulSoup, *, base_url: str) -> tuple[list[str], list[AssetLink]]:
    links: list[str] = []
    assets: list[AssetLink] = []
    for anchor in soup.find_all("a", href=True):
        absolute = urljoin(base_url, anchor["href"])
        parsed = urlparse(absolute)
        if parsed.path.endswith(ASSET_EXTENSIONS):
            assets.append(AssetLink(url=absolute))
        elif is_same_site_url(absolute) and is_public_page_url(absolute):
            route = parsed.path.rstrip("/") or "/"
            links.append(route)
    for tag in soup.find_all(src=True):
        assets.append(AssetLink(url=urljoin(base_url, tag["src"])))
    for tag in soup.find_all(href=True):
        href = urljoin(base_url, tag["href"])
        if href.lower().endswith(ASSET_EXTENSIONS):
            assets.append(AssetLink(url=href))
    unique_assets: list[AssetLink] = []
    seen_assets: set[str] = set()
    for asset in assets:
        if asset.url in seen_assets:
            continue
        seen_assets.add(asset.url)
        unique_assets.append(asset)
    return dedupe(links), unique_assets


def parse_html_document(html: str, *, url: str) -> tuple[str, list[ContentBlock], list[str], list[AssetLink]]:
    soup = BeautifulSoup(html, "html.parser")
    title = clean_text(
        (soup.select_one("main h1") or soup.select_one("article h1") or soup.select_one("title") or soup).get_text(" ", strip=True)
    )
    blocks = soup_to_content_blocks(soup, base_url=url)
    meaningful_blocks = [block for block in blocks if block.body.strip()]
    if len(meaningful_blocks) <= 1:
        fallback_blocks: list[ContentBlock] = []
        if title:
            fallback_blocks.append(ContentBlock(kind="markdown", body=f"# {title}"))
        description = _meta_description(soup)
        if description:
            fallback_blocks.append(ContentBlock(kind="markdown", body=description))
        fallback_blocks.extend(_anchor_group_blocks(soup, base_url=url))
        if len(fallback_blocks) > len(meaningful_blocks):
            blocks = fallback_blocks
    links, assets = extract_links_and_assets(soup, base_url=url)
    if not blocks and title:
        blocks = [ContentBlock(kind="markdown", body=f"# {title}")]
    return title, blocks, links, assets
