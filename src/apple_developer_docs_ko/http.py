from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import hashlib
import json
import mimetypes
import time

from .config import Settings
from .utils import strip_trailing_commas


@dataclass(slots=True)
class HttpResponse:
    url: str
    status: int
    headers: dict[str, str]
    text: str | None = None
    content: bytes | None = None


class HttpClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    def _request(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
        attempts: int = 3,
    ) -> HttpResponse:
        last_error: Exception | None = None
        total_attempts = max(1, attempts)
        effective_timeout = timeout if timeout is not None else self.settings.request_timeout
        for attempt in range(total_attempts):
            req = Request(
                url,
                headers={
                    "User-Agent": self.settings.user_agent,
                    **(headers or {}),
                },
            )
            try:
                with urlopen(req, timeout=effective_timeout) as response:
                    content = response.read()
                    headers_dict = {k.lower(): v for k, v in response.headers.items()}
                    content_type = headers_dict.get("content-type", "")
                    text = None
                    if any(token in content_type for token in ("text", "json", "xml", "javascript", "mpegurl", "vtt")):
                        text = content.decode("utf-8", errors="replace")
                    return HttpResponse(
                        url=response.geturl(),
                        status=response.status,
                        headers=headers_dict,
                        text=text,
                        content=content,
                    )
            except HTTPError as exc:
                return HttpResponse(
                    url=url,
                    status=exc.code,
                    headers={k.lower(): v for k, v in exc.headers.items()},
                    text=exc.read().decode("utf-8", errors="replace"),
                    content=None,
                )
            except (URLError, OSError) as exc:
                last_error = exc
                if attempt < total_attempts - 1:
                    time.sleep(0.5 * (attempt + 1))
                    continue
        raise RuntimeError(f"Failed to fetch {url}: {last_error}") from last_error

    def get_text(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
        attempts: int = 3,
    ) -> str:
        response = self._request(url, headers=headers, timeout=timeout, attempts=attempts)
        if response.status >= 400:
            raise RuntimeError(f"HTTP {response.status} for {url}")
        if response.text is not None:
            return response.text
        if response.content is not None:
            return response.content.decode("utf-8", errors="replace")
        return ""

    def get_json(
        self,
        url: str,
        *,
        tolerant: bool = False,
        timeout: float | None = None,
        attempts: int = 3,
    ) -> object:
        text = self.get_text(url, timeout=timeout, attempts=attempts)
        if tolerant:
            text = strip_trailing_commas(text)
        return json.loads(text)

    def get_bytes(
        self,
        url: str,
        *,
        timeout: float | None = None,
        attempts: int = 3,
    ) -> tuple[bytes, str | None]:
        response = self._request(url, timeout=timeout, attempts=attempts)
        if response.status >= 400:
            raise RuntimeError(f"HTTP {response.status} for {url}")
        content_type = response.headers.get("content-type")
        return response.content or b"", content_type

    def exists(self, url: str, *, timeout: float | None = None, attempts: int = 3) -> bool:
        try:
            response = self._request(url, timeout=timeout, attempts=attempts)
            return response.status < 400
        except Exception:
            return False

    def cache_raw(self, url: str, body: str, suffix: str) -> Path:
        digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
        parsed = urlparse(url)
        file_name = parsed.path.strip("/").replace("/", "__") or "index"
        target = self.settings.raw_cache_dir / digest[:2] / f"{file_name}.{suffix}"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        return target

    def cache_asset(self, url: str, content: bytes, content_type: str | None) -> Path:
        parsed = urlparse(url)
        rel = parsed.netloc.replace(":", "_") + parsed.path
        target = self.settings.asset_cache_dir / rel.lstrip("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.suffix and content_type:
            ext = mimetypes.guess_extension(content_type.split(";")[0].strip())
            if ext:
                target = target.with_suffix(ext)
        target.write_bytes(content)
        return target
