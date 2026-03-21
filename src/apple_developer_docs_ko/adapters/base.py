from __future__ import annotations

from abc import ABC, abstractmethod

from ..http import HttpClient
from ..models import NormalizedPage


class BaseAdapter(ABC):
    name = "base"
    section = "base"
    incremental_discovery = False

    def __init__(self, http: HttpClient) -> None:
        self.http = http

    @abstractmethod
    def discover(self, *, limit: int | None = None) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def fetch(self, route: str) -> NormalizedPage:
        raise NotImplementedError

    def preferred_locale(self, route: str) -> str:
        return "en-US"

    def list_assets(self, route: str) -> list[str]:
        return []

    def seed_routes(self, *, limit: int | None = None) -> list[str]:
        return self.discover(limit=limit)

    def expand_route(self, route: str) -> list[str]:
        return []

    def can_handle(self, route: str) -> bool:
        return route.startswith("/")
