from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

from ..html_tools import parse_html_document
from ..models import AssetLink, ContentBlock, NormalizedPage, PageSourceRecord
from ..utils import absolutize, clean_text, dedupe, text_hash
from .base import BaseAdapter


def _parse_hls_attributes(line: str) -> dict[str, str]:
    payload = line.split(":", 1)[1]
    matches = re.findall(r'([A-Z0-9\-]+)=(".*?"|[^,]+)', payload)
    return {key: value.strip('"') for key, value in matches}


def parse_webvtt(text: str) -> list[dict[str, str]]:
    cues: list[tuple[str, str]] = []
    current_time: str | None = None
    current_lines: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line == "WEBVTT" or line.startswith("NOTE"):
            if current_time and current_lines:
                cues.append((current_time, clean_text(" ".join(current_lines))))
            current_time = None
            current_lines = []
            continue
        if "-->" in line:
            current_time = line.split("-->", 1)[0].strip()
            current_lines = []
            continue
        if current_time:
            current_lines.append(line)
    if current_time and current_lines:
        cues.append((current_time, clean_text(" ".join(current_lines))))
    return [{"start": start, "text": text} for start, text in cues]


def _parse_vtt_cues(text: str) -> list[tuple[str, str]]:
    return [(cue["start"], cue["text"]) for cue in parse_webvtt(text)]


def parse_subtitle_playlist(text: str) -> dict[str, dict[str, str]]:
    tracks: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        if line.startswith("#EXT-X-MEDIA:") and "TYPE=SUBTITLES" in line:
            attrs = _parse_hls_attributes(line)
            uri = attrs.get("URI")
            language = attrs.get("LANGUAGE")
            if uri and language:
                tracks[language] = {
                    "name": attrs.get("NAME", language),
                    "uri": uri,
                }
    return tracks


class VideosAdapter(BaseAdapter):
    name = "videos"
    section = "videos"
    incremental_discovery = True
    locale_probe_timeout = 5.0
    locale_probe_attempts = 1
    playlist_timeout = 8.0
    playlist_attempts = 1
    segment_timeout = 5.0
    segment_attempts = 1
    segment_workers = 16
    max_transcript_segments: int | None = None

    def can_handle(self, route: str) -> bool:
        return route.startswith("/videos/")

    def seed_routes(self, *, limit: int | None = None) -> list[str]:
        routes = ["/videos"]
        if limit:
            return routes[:limit]
        return routes

    def expand_route(self, route: str) -> list[str]:
        try:
            html = self.http.get_text(absolutize(route))
        except Exception:
            return []
        soup = BeautifulSoup(html, "html.parser")
        routes: list[str] = []
        for anchor in soup.find_all("a", href=True):
            href = anchor["href"]
            if not href.startswith("/videos/"):
                continue
            next_route = href.rstrip("/")
            if next_route and not next_route.startswith("/videos/images"):
                routes.append(next_route)
        return dedupe(routes)

    def preferred_locale(self, route: str) -> str:
        return (
            "ko-KR"
            if self.http.exists(
                absolutize(f"/kr{route}"),
                timeout=self.locale_probe_timeout,
                attempts=self.locale_probe_attempts,
            )
            else "en-US"
        )

    def discover(self, *, limit: int | None = None) -> list[str]:
        queue = self.seed_routes()
        seen: set[str] = set()
        routes: list[str] = []
        while queue:
            route = queue.pop(0).rstrip("/") or "/videos"
            if route in seen or not route.startswith("/videos"):
                continue
            seen.add(route)
            if route != "/videos/images":
                routes.append(route)
            if limit and len(routes) >= limit:
                break
            for next_route in self.expand_route(route):
                if next_route not in seen and not next_route.startswith("/videos/images"):
                    queue.append(next_route)
        return dedupe(routes)

    def _extract_video_stream(self, html: str) -> str | None:
        soup = BeautifulSoup(html, "html.parser")
        meta = soup.find("meta", attrs={"property": "og:video"})
        if meta and meta.get("content"):
            return meta["content"]
        video = soup.find("video")
        if video and video.get("src"):
            return video["src"]
        return None

    def _subtitle_track_and_assets(self, master_url: str, preferred_language: str) -> tuple[str | None, list[AssetLink]]:
        master_text = self.http.get_text(
            master_url,
            timeout=self.playlist_timeout,
            attempts=self.playlist_attempts,
        )
        assets = [AssetLink(url=master_url)]
        tracks: dict[str, str] = {}
        parsed_tracks = parse_subtitle_playlist(master_text)
        for language, payload in parsed_tracks.items():
            track_url = urljoin(master_url, payload["uri"])
            tracks[language] = track_url
            assets.append(AssetLink(url=track_url))
        for line in master_text.splitlines():
            if line and not line.startswith("#"):
                assets.append(AssetLink(url=urljoin(master_url, line.strip())))
        chosen = tracks.get(preferred_language) or tracks.get(preferred_language.split("-")[0]) or tracks.get("ko") or tracks.get("en")
        return chosen, dedupe_asset_links(assets)

    def _fetch_transcript(self, playlist_url: str) -> tuple[list[tuple[str, str]], list[AssetLink]]:
        playlist_text = self.http.get_text(
            playlist_url,
            timeout=self.playlist_timeout,
            attempts=self.playlist_attempts,
        )
        assets = [AssetLink(url=playlist_url)]
        segment_urls = [
            urljoin(playlist_url, line.strip())
            for line in playlist_text.splitlines()
            if line and not line.startswith("#")
        ]
        assets.extend(AssetLink(url=segment_url) for segment_url in segment_urls)
        if self.max_transcript_segments is not None:
            segment_urls = segment_urls[: self.max_transcript_segments]

        def fetch_segment(segment_url: str) -> list[tuple[str, str]]:
            try:
                segment_text = self.http.get_text(
                    segment_url,
                    timeout=self.segment_timeout,
                    attempts=self.segment_attempts,
                )
            except Exception:
                return []
            return _parse_vtt_cues(segment_text)

        cues: list[tuple[str, str]] = []
        if segment_urls:
            worker_count = min(self.segment_workers, len(segment_urls))
            with ThreadPoolExecutor(max_workers=worker_count) as executor:
                for segment_cues in executor.map(fetch_segment, segment_urls):
                    cues.extend(segment_cues)
        return cues, dedupe_asset_links(assets)

    def fetch(self, route: str) -> NormalizedPage:
        canonical_locale = self.preferred_locale(route)
        english_url = absolutize(route)
        canonical_url = absolutize(f"/kr{route}") if canonical_locale.startswith("ko") else english_url
        canonical_html = self.http.get_text(canonical_url)
        title, blocks, links, assets = parse_html_document(canonical_html, url=canonical_url)
        english_html = canonical_html if canonical_url == english_url else self.http.get_text(english_url)
        stream_url = self._extract_video_stream(english_html)
        transcript_text = ""
        if stream_url:
            assets.append(AssetLink(url=stream_url))
            try:
                track_url, media_assets = self._subtitle_track_and_assets(
                    stream_url, "ko" if canonical_locale.startswith("ko") else "en"
                )
            except Exception:
                track_url = None
                media_assets = []
            assets.extend(media_assets)
            if track_url:
                try:
                    cues, transcript_assets = self._fetch_transcript(track_url)
                except Exception:
                    cues, transcript_assets = [], []
                assets.extend(transcript_assets)
                if cues:
                    transcript_text = "\n".join(f"- [{timecode}] {text}" for timecode, text in cues)
                    blocks.append(
                        ContentBlock(
                            kind="video-transcript",
                            body=transcript_text,
                            translatable=not canonical_locale.startswith("ko"),
                        )
                    )
        original_title = clean_text(BeautifulSoup(english_html, "html.parser").title.get_text(" ", strip=True)) if BeautifulSoup(english_html, "html.parser").title else title
        source_payload = canonical_html + "\n" + transcript_text
        return NormalizedPage(
            route=route,
            source_url=english_url,
            source_locale=canonical_locale,
            section=self.section,
            content_type="video-html",
            title=title or original_title or clean_text(route.rsplit("/", 1)[-1]),
            original_title=original_title or title or clean_text(route.rsplit("/", 1)[-1]),
            source_hash=text_hash(source_payload),
            canonical_source="official-ko" if canonical_locale.startswith("ko") else "machine-translation",
            discovered_links=[link for link in links if link.startswith("/videos/")],
            asset_links=dedupe_asset_links(assets),
            content_blocks=blocks,
            source_variants=[
                PageSourceRecord(url=canonical_url, locale=canonical_locale, content_type="text/html", raw_text=canonical_html),
                PageSourceRecord(url=english_url, locale="en-US", content_type="text/html", raw_text=english_html),
            ],
        )


def dedupe_asset_links(assets: list[AssetLink]) -> list[AssetLink]:
    seen: set[str] = set()
    out: list[AssetLink] = []
    for asset in assets:
        if asset.url in seen:
            continue
        seen.add(asset.url)
        out.append(asset)
    return out
