from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import replace
from urllib.request import Request, urlopen
import json

from .models import ContentBlock, NormalizedPage, utc_now


SYSTEM_PROMPT = """You translate Apple developer documentation into Korean.
Rules:
- Never summarize, omit, or simplify content.
- Preserve Markdown structure, tables, lists, links, and inline code.
- Preserve URLs, file paths, symbol names, API names, and executable code exactly.
- Translate natural language fully and faithfully.
- If code comments are present, translate only the human-language comment text without changing code tokens.
Return only translated Markdown."""


class Translator(ABC):
    name = "base"

    @abstractmethod
    def translate_text(self, text: str, *, route: str) -> str:
        raise NotImplementedError

    def translate_page(self, page: NormalizedPage) -> NormalizedPage:
        translated_blocks: list[ContentBlock] = []
        for block in page.content_blocks:
            if block.translatable and page.source_locale.startswith("en"):
                translated_blocks.append(
                    replace(
                        block,
                        body=self.translate_text(block.body, route=page.route),
                    )
                )
            else:
                translated_blocks.append(block)
        page.content_blocks = translated_blocks
        page.last_translated_at = utc_now()
        return page


class IdentityTranslator(Translator):
    name = "identity"

    def translate_text(self, text: str, *, route: str) -> str:
        return text


class MissingTranslator(Translator):
    name = "missing"

    def translate_text(self, text: str, *, route: str) -> str:
        raise RuntimeError(
            f"No translator backend is configured for English page {route}. "
            "Use --identity-translation for parser smoke runs or set OPENAI_API_KEY."
        )


class OpenAIResponsesTranslator(Translator):
    name = "openai-responses"

    def __init__(self, *, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model

    def translate_text(self, text: str, *, route: str) -> str:
        payload = {
            "model": self.model,
            "input": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Route: {route}\n\nTranslate this content to Korean:\n\n{text}",
                },
            ],
        }
        req = Request(
            "https://api.openai.com/v1/responses",
            data=json.dumps(payload).encode("utf-8"),
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
        )
        with urlopen(req, timeout=120) as response:
            body = json.loads(response.read().decode("utf-8"))
        if "output_text" in body and body["output_text"]:
            return body["output_text"]
        parts: list[str] = []
        for item in body.get("output", []):
            for content in item.get("content", []):
                text_value = content.get("text")
                if text_value:
                    parts.append(text_value)
        if not parts:
            raise RuntimeError(f"OpenAI response did not include translated text for {route}")
        return "".join(parts)


def build_translator(*, identity: bool, api_key: str | None, model: str | None) -> Translator:
    if identity:
        return IdentityTranslator()
    if api_key:
        return OpenAIResponsesTranslator(api_key=api_key, model=model or "gpt-4.1-mini")
    return MissingTranslator()
