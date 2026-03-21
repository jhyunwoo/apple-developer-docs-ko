from __future__ import annotations

from pathlib import Path
import hashlib

from .http import HttpClient
from .models import AssetLink
from .paths import mirrored_asset_relpath


def mirror_asset(http: HttpClient, asset: AssetLink) -> AssetLink:
    try:
        content, content_type = http.get_bytes(asset.url)
    except Exception:
        asset.status = "external"
        return asset
    target = http.settings.asset_cache_dir / mirrored_asset_relpath(asset.url)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    asset.local_path = str(target.relative_to(http.settings.root_dir))
    asset.content_type = content_type
    asset.sha256 = hashlib.sha256(content).hexdigest()
    asset.status = "mirrored"
    return asset


def public_asset_url(asset: AssetLink) -> str:
    if not asset.local_path:
        return asset.url
    rel = Path(asset.local_path).as_posix()
    if rel.startswith(".cache/assets/"):
        rel = rel[len(".cache/assets/") :]
    return f"/__mirror__/{rel}"
