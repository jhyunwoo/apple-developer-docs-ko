from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse


def normalize_route(route: str) -> str:
    if not route:
        return "/"
    parsed = urlparse(route)
    cleaned = parsed.path or route
    if not cleaned.startswith("/"):
        cleaned = "/" + cleaned
    if cleaned != "/" and cleaned.endswith("/"):
        cleaned = cleaned[:-1]
    return cleaned


def route_to_content_path(content_dir: Path, route: str) -> Path:
    normalized = normalize_route(route).strip("/")
    if not normalized:
        return content_dir / "index.md"
    return content_dir / normalized / "index.md"


def route_to_dist_path(dist_dir: Path, route: str) -> Path:
    normalized = normalize_route(route).strip("/")
    if not normalized:
        return dist_dir / "index.html"
    return dist_dir / normalized / "index.html"


def mirrored_asset_relpath(url: str) -> Path:
    parsed = urlparse(url)
    host = parsed.netloc.replace(":", "_")
    path = parsed.path.lstrip("/")
    if not path:
        path = "index"
    return Path(host) / path
