from __future__ import annotations

from collections import deque
import json
from urllib.parse import urljoin

from ..models import ContentBlock, NormalizedPage, PageSourceRecord
from ..utils import absolutize, clean_text, dedupe, text_hash
from .base import BaseAdapter
from .docc_utils import collect_assets, collect_discovered_routes, render_content_items, render_inline


DOCC_DATA_BASE = "https://developer.apple.com/tutorials/data"


def _declaration_blocks(section: dict) -> list[ContentBlock]:
    blocks: list[ContentBlock] = []
    for declaration in section.get("declarations", []):
        tokens = declaration.get("tokens", [])
        code = "".join(token.get("text", "") for token in tokens).strip()
        if code:
            blocks.append(
                ContentBlock(
                    kind="declaration",
                    body=code,
                    metadata={"syntax": ",".join(declaration.get("languages", [])) or "swift"},
                    translatable=False,
                )
            )
        platforms = declaration.get("platforms", [])
        if platforms:
            blocks.append(
                ContentBlock(
                    kind="availability",
                    body="\n".join(f"- {platform}" for platform in platforms),
                    translatable=False,
                )
            )
    return blocks


def normalize_docc_page(
    *,
    route: str,
    raw_text: str,
    doc: dict,
    section: str,
    source_locale: str = "en-US",
    canonical_source: str = "machine-translation",
) -> NormalizedPage:
    references = doc.get("references", {})
    original_title = doc.get("metadata", {}).get("title") or clean_text(route.rsplit("/", 1)[-1])
    blocks: list[ContentBlock] = []

    abstract = render_inline(doc.get("abstract"), references)
    if abstract:
        blocks.append(ContentBlock(kind="markdown", body=f"# {original_title}\n\n{abstract}"))
    else:
        blocks.append(ContentBlock(kind="markdown", body=f"# {original_title}"))

    for section_block in doc.get("primaryContentSections", []):
        kind = section_block.get("kind")
        if kind == "content":
            blocks.extend(render_content_items(section_block.get("content", []), references))
        elif kind == "declarations":
            blocks.extend(_declaration_blocks(section_block))

    for task_group in doc.get("topicSections", []):
        title = task_group.get("title", "Topics")
        lines = [f"## {title}"]
        for identifier in task_group.get("identifiers", []):
            ref = references.get(identifier, {})
            url = absolutize(ref.get("url", ""))
            label = ref.get("title") or ref.get("name") or url
            abstract = ref.get("abstract") or ""
            if isinstance(abstract, list):
                abstract = " ".join(item.get("text", "") for item in abstract if isinstance(item, dict))
            line = f"- [{clean_text(label)}]({url})"
            if abstract:
                line += f": {clean_text(str(abstract))}"
            lines.append(line)
        blocks.append(ContentBlock(kind="topic-grid", body="\n".join(lines)))

    for rel_group in doc.get("relationshipsSections", []):
        title = rel_group.get("title", "Related")
        lines = [f"## {title}"]
        for identifier in rel_group.get("identifiers", []):
            ref = references.get(identifier, {})
            url = absolutize(ref.get("url", ""))
            label = ref.get("title") or ref.get("name") or url
            abstract = ref.get("abstract") or ""
            if isinstance(abstract, list):
                abstract = " ".join(item.get("text", "") for item in abstract if isinstance(item, dict))
            line = f"- [{clean_text(label)}]({url})"
            if abstract:
                line += f": {clean_text(str(abstract))}"
            lines.append(line)
        blocks.append(ContentBlock(kind="topic-grid", body="\n".join(lines), translatable=source_locale.startswith("en")))

    source_url = absolutize(route)
    source_record = PageSourceRecord(
        url=f"{DOCC_DATA_BASE}{route}.json",
        locale="en-US" if source_locale.startswith("en") else source_locale,
        content_type="application/json",
        raw_text=raw_text,
    )
    source_hash = text_hash(raw_text)
    return NormalizedPage(
        route=route,
        source_url=source_url,
        source_locale=source_locale,
        section=section,
        content_type=doc.get("kind", "docc"),
        title=original_title,
        original_title=original_title,
        source_hash=source_hash,
        canonical_source=canonical_source,
        discovered_links=collect_discovered_routes(doc),
        asset_links=collect_assets(doc),
        content_blocks=blocks,
        source_variants=[source_record],
    )


class DoccAdapter(BaseAdapter):
    name = "docc"
    section = "docc"
    incremental_discovery = True

    def can_handle(self, route: str) -> bool:
        return route.startswith("/documentation/")

    def seed_routes(self, *, limit: int | None = None) -> list[str]:
        root = self.http.get_json(f"{DOCC_DATA_BASE}/documentation/technologies.json")
        routes = collect_discovered_routes(root)
        if limit:
            return routes[:limit]
        return routes

    def expand_route(self, route: str) -> list[str]:
        try:
            doc = self.http.get_json(f"{DOCC_DATA_BASE}{route}.json")
        except Exception:
            return []
        return collect_discovered_routes(doc)

    def discover(self, *, limit: int | None = None) -> list[str]:
        queue = deque(self.seed_routes())
        seen: set[str] = set()
        routes: list[str] = []
        while queue:
            route = queue.popleft()
            if route in seen or not route.startswith("/documentation/"):
                continue
            seen.add(route)
            routes.append(route)
            if limit and len(routes) >= limit:
                break
            for next_route in self.expand_route(route):
                if next_route not in seen:
                    queue.append(next_route)
        return dedupe(routes)

    def fetch(self, route: str) -> NormalizedPage:
        raw = self.http.get_text(f"{DOCC_DATA_BASE}{route}.json")
        doc = json.loads(raw)
        return normalize_docc_page(route=route, raw_text=raw, doc=doc, section=self.section)


def normalize_document(*, route: str, document: dict) -> NormalizedPage:
    return normalize_docc_page(
        route=route,
        raw_text="{}",
        doc=document,
        section="docc",
    )
