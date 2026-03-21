from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sqlite3

import yaml

from .config import Settings
from .paths import normalize_route, route_to_content_path, route_to_dist_path


FRONTMATTER_SPLIT = "\n---\n"
HANGUL_RE = re.compile(r"[가-힣]")


@dataclass(slots=True)
class VerificationFinding:
    severity: str
    code: str
    route: str
    message: str
    file_path: str | None = None


@dataclass(slots=True)
class VerificationReport:
    findings: list[VerificationFinding]
    active_page_count: int
    content_page_count: int
    dist_page_count: int

    @property
    def ok(self) -> bool:
        return not self.findings


def _parse_frontmatter(markdown_path: Path) -> tuple[dict, str]:
    raw = markdown_path.read_text(encoding="utf-8")
    if not raw.startswith("---\n") or FRONTMATTER_SPLIT not in raw[4:]:
        return {}, raw
    _, rest = raw.split("---\n", 1)
    frontmatter_text, body = rest.split(FRONTMATTER_SPLIT, 1)
    return yaml.safe_load(frontmatter_text) or {}, body


def _body_without_asset_list(body: str) -> str:
    lines = body.splitlines()
    cleaned: list[str] = []
    skip_directive = False
    for line in lines:
        stripped = line.strip()
        if stripped == ":::asset-list":
            skip_directive = True
            continue
        if skip_directive and stripped == ":::":
            skip_directive = False
            continue
        if skip_directive:
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def _meaningful_body_lines(body: str) -> list[str]:
    lines: list[str] = []
    for raw_line in _body_without_asset_list(body).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line == ":::" or line.startswith(":::"):
            continue
        lines.append(line)
    return lines


def _load_active_pages(manifest_path: Path) -> tuple[dict[str, sqlite3.Row], dict[str, sqlite3.Row]]:
    if not manifest_path.exists():
        return {}, {}
    conn = sqlite3.connect(manifest_path)
    conn.row_factory = sqlite3.Row
    try:
        pages = {
            row["route"]: row
            for row in conn.execute("SELECT * FROM pages WHERE removed_at IS NULL ORDER BY route").fetchall()
        }
        translations = {
            row["route"]: row
            for row in conn.execute("SELECT * FROM translations ORDER BY route").fetchall()
        }
        return pages, translations
    finally:
        conn.close()


def _load_content_pages(content_dir: Path) -> dict[str, dict]:
    pages: dict[str, dict] = {}
    for markdown_path in sorted(content_dir.rglob("index.md")):
        frontmatter, body = _parse_frontmatter(markdown_path)
        route = normalize_route(frontmatter.get("route") or "/" + markdown_path.relative_to(content_dir).parent.as_posix())
        pages[route] = {
            "path": markdown_path,
            "frontmatter": frontmatter,
            "body": body,
        }
    return pages


def _audit_content_quality(
    *,
    findings: list[VerificationFinding],
    settings: Settings,
    route: str,
    content_page: dict,
    source_locale: str,
) -> None:
    body = content_page["body"]
    dist_path = route_to_dist_path(settings.dist_dir, route)

    if not dist_path.exists():
        findings.append(
            VerificationFinding(
                severity="error",
                code="missing-dist-html",
                route=route,
                message="Canonical Markdown exists but rendered HTML output is missing.",
                file_path=str(dist_path),
            )
        )

    body_lines = _meaningful_body_lines(body)
    if len(body_lines) <= 1:
        findings.append(
            VerificationFinding(
                severity="error",
                code="content-too-thin",
                route=route,
                message="Output is too thin to count as a full translated page.",
                file_path=str(content_page["path"]),
            )
        )
    elif source_locale.startswith("ko") and not HANGUL_RE.search(_body_without_asset_list(body)):
        findings.append(
            VerificationFinding(
                severity="warning",
                code="missing-hangul-text",
                route=route,
                message="Page claims Korean output but contains no Hangul outside asset listings.",
                file_path=str(content_page["path"]),
            )
        )


def verify_outputs(settings: Settings) -> VerificationReport:
    findings: list[VerificationFinding] = []
    manifest_pages, translations = _load_active_pages(settings.manifest_path)
    content_pages = _load_content_pages(settings.content_dir)
    audited_content_routes: set[str] = set()

    for route, page_row in manifest_pages.items():
        markdown_path = route_to_content_path(settings.content_dir, route)
        translation_row = translations.get(route)
        page_level_source_locale = str(page_row["source_locale"])

        if translation_row is not None and translation_row["translator"] == "identity":
            findings.append(
                VerificationFinding(
                    severity="error",
                    code="identity-translation",
                    route=route,
                    message="Page was marked translated with the identity translator, so no Korean translation actually occurred.",
                    file_path=str(markdown_path) if markdown_path.exists() else None,
                )
            )
        if page_level_source_locale.startswith("en") and translation_row is None:
            findings.append(
                VerificationFinding(
                    severity="error",
                    code="missing-translation-record",
                    route=route,
                    message="English source page has no translation record.",
                    file_path=str(markdown_path) if markdown_path.exists() else None,
                )
            )

        if route not in content_pages or not markdown_path.exists():
            findings.append(
                VerificationFinding(
                    severity="error",
                    code="missing-markdown",
                    route=route,
                    message="Active manifest page is missing its canonical Markdown output.",
                    file_path=str(markdown_path),
                )
            )
            continue

        content_page = content_pages[route]
        frontmatter = content_page["frontmatter"]
        source_locale = str(frontmatter.get("source_locale") or page_row["source_locale"])
        audited_content_routes.add(route)
        _audit_content_quality(
            findings=findings,
            settings=settings,
            route=route,
            content_page=content_page,
            source_locale=source_locale,
        )

    for route, content_page in content_pages.items():
        if route not in manifest_pages:
            findings.append(
                VerificationFinding(
                    severity="error",
                    code="orphan-markdown",
                    route=route,
                    message="Markdown output exists without an active manifest entry.",
                    file_path=str(content_page["path"]),
                )
            )
        if route not in audited_content_routes:
            _audit_content_quality(
                findings=findings,
                settings=settings,
                route=route,
                content_page=content_page,
                source_locale=str(content_page["frontmatter"].get("source_locale") or ""),
            )

    dist_page_count = sum(1 for _ in settings.dist_dir.rglob("index.html")) if settings.dist_dir.exists() else 0
    return VerificationReport(
        findings=sorted(findings, key=lambda item: (item.severity != "error", item.route, item.code)),
        active_page_count=len(manifest_pages),
        content_page_count=len(content_pages),
        dist_page_count=dist_page_count,
    )


def format_report(report: VerificationReport) -> str:
    lines = [
        f"Active manifest pages: {report.active_page_count}",
        f"Content Markdown pages: {report.content_page_count}",
        f"Rendered HTML pages: {report.dist_page_count}",
    ]
    if report.ok:
        lines.append("Verification passed with no findings.")
        return "\n".join(lines)

    lines.append(f"Findings: {len(report.findings)}")
    for finding in report.findings:
        location = f" ({finding.file_path})" if finding.file_path else ""
        lines.append(
            f"[{finding.severity.upper()}] {finding.route} {finding.code}: {finding.message}{location}"
        )
    return "\n".join(lines)
