from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(slots=True)
class Settings:
    root_dir: Path
    content_dir: Path
    dist_dir: Path
    raw_cache_dir: Path
    asset_cache_dir: Path
    state_dir: Path
    manifest_path: Path
    user_agent: str
    request_timeout: float
    openai_api_key: str | None
    openai_model: str | None

    @classmethod
    def from_env(cls, root_dir: Path | None = None) -> "Settings":
        root = (root_dir or Path.cwd()).resolve()
        cache_dir = root / ".cache"
        state_dir = root / "state"
        return cls(
            root_dir=root,
            content_dir=root / "content",
            dist_dir=root / os.getenv("APPLE_DOCS_KO_DIST_DIR", "out"),
            raw_cache_dir=cache_dir / "raw",
            asset_cache_dir=cache_dir / "assets",
            state_dir=state_dir,
            manifest_path=state_dir / "manifest.sqlite",
            user_agent=os.getenv(
                "APPLE_DOCS_KO_USER_AGENT",
                "apple-developer-docs-ko/0.1 (+https://developer.apple.com/)",
            ),
            request_timeout=float(os.getenv("APPLE_DOCS_KO_TIMEOUT", "30")),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_model=os.getenv("OPENAI_TRANSLATION_MODEL") or os.getenv("OPENAI_MODEL"),
        )

    def ensure_directories(self) -> None:
        for path in (
            self.content_dir,
            self.dist_dir,
            self.raw_cache_dir,
            self.asset_cache_dir,
            self.state_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)
