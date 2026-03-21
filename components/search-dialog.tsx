"use client";

import Link from "next/link";
import { useEffect, useMemo, useRef, useState } from "react";

interface SearchManifestSection {
  id: string;
  count: number;
  path: string;
}

interface SearchManifest {
  generatedAt: string;
  totalDocuments: number;
  sections: SearchManifestSection[];
}

interface SearchDocument {
  route: string;
  section: string;
  title: string;
  headings: string[];
  snippet: string;
  body: string;
}

interface SearchResult extends SearchDocument {
  score: number;
  preview: string;
}

function createSnippet(document: SearchDocument, query: string) {
  const source = `${document.title} ${document.body}`.trim();
  const index = source.toLowerCase().indexOf(query);
  if (index === -1) {
    return document.snippet;
  }
  const start = Math.max(0, index - 70);
  const end = Math.min(source.length, index + 150);
  return source.slice(start, end).trim();
}

function scoreDocument(document: SearchDocument, query: string) {
  let score = 0;
  if (document.title.toLowerCase().includes(query)) {
    score += 120;
  }
  if (document.route.toLowerCase().includes(query)) {
    score += 60;
  }
  for (const heading of document.headings) {
    if (heading.toLowerCase().includes(query)) {
      score += 24;
    }
  }
  const bodyIndex = document.body.toLowerCase().indexOf(query);
  if (bodyIndex >= 0) {
    score += Math.max(8, 32 - Math.min(bodyIndex / 120, 24));
  }
  return score;
}

export function SearchDialog() {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [manifest, setManifest] = useState<SearchManifest | null>(null);
  const [loading, setLoading] = useState(false);
  const [documents, setDocuments] = useState<SearchDocument[]>([]);
  const loadedSections = useRef(new Set<string>());
  const inputRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    function onKeydown(event: KeyboardEvent) {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        setOpen(true);
      }
      if (event.key === "/" && !open) {
        const target = event.target as HTMLElement | null;
        const isTypingTarget = target?.tagName === "INPUT" || target?.tagName === "TEXTAREA" || target?.isContentEditable;
        if (!isTypingTarget) {
          event.preventDefault();
          setOpen(true);
        }
      }
      if (event.key === "Escape") {
        setOpen(false);
      }
    }

    window.addEventListener("keydown", onKeydown);
    return () => window.removeEventListener("keydown", onKeydown);
  }, [open]);

  useEffect(() => {
    if (!open) {
      return;
    }

    inputRef.current?.focus();

    if (manifest) {
      return;
    }

    void (async () => {
      setLoading(true);
      const response = await fetch("/__search__/manifest.json");
      const nextManifest = (await response.json()) as SearchManifest;
      setManifest(nextManifest);
      setLoading(false);
    })();
  }, [manifest, open]);

  useEffect(() => {
    if (!manifest || !open || !query.trim()) {
      return;
    }

    const missingSections = manifest.sections.filter((section) => !loadedSections.current.has(section.id));
    if (missingSections.length === 0) {
      return;
    }

    void (async () => {
      setLoading(true);
      const batches = await Promise.all(
        missingSections.map(async (section) => {
          const response = await fetch(section.path);
          const docs = (await response.json()) as SearchDocument[];
          loadedSections.current.add(section.id);
          return docs;
        })
      );
      setDocuments((current) => [...current, ...batches.flat()]);
      setLoading(false);
    })();
  }, [manifest, open, query]);

  const results = useMemo<SearchResult[]>(() => {
    const normalized = query.trim().toLowerCase();
    if (!normalized) {
      return [];
    }

    return documents
      .map((document) => ({
        ...document,
        score: scoreDocument(document, normalized),
        preview: createSnippet(document, normalized)
      }))
      .filter((document) => document.score > 0)
      .sort((left, right) => right.score - left.score)
      .slice(0, 18);
  }, [documents, query]);

  return (
    <>
      <button type="button" className="search-trigger" onClick={() => setOpen(true)}>
        <span>문서 검색</span>
        <kbd>⌘K</kbd>
      </button>

      {open ? (
        <div className="search-overlay" role="dialog" aria-modal="true">
          <div className="search-backdrop" onClick={() => setOpen(false)} />
          <div className="search-panel">
            <div className="search-panel-header">
              <input
                ref={inputRef}
                type="search"
                placeholder="제목, 경로, 본문까지 검색합니다"
                value={query}
                onChange={(event) => setQuery(event.target.value)}
              />
              <button type="button" className="ghost-button" onClick={() => setOpen(false)}>
                닫기
              </button>
            </div>

            <div className="search-panel-body">
              {!query.trim() ? (
                <div className="search-empty">
                  <p>문서 본문 전체를 기준으로 정적 인덱스를 검색합니다.</p>
                  <p className="muted">`/`, `⌘K`, `Ctrl+K`로 언제든 다시 열 수 있습니다.</p>
                </div>
              ) : null}

              {loading ? <p className="muted">검색 인덱스를 불러오는 중입니다...</p> : null}

              {query.trim() && !loading && results.length === 0 ? (
                <p className="muted">일치하는 문서를 찾지 못했습니다.</p>
              ) : null}

              <div className="search-results">
                {results.map((result) => (
                  <Link
                    key={result.route}
                    href={result.route}
                    prefetch={false}
                    className="search-result"
                    onClick={() => setOpen(false)}
                  >
                    <div className="search-result-meta">
                      <span>{result.section}</span>
                      <code>{result.route}</code>
                    </div>
                    <strong>{result.title}</strong>
                    <p>{result.preview}</p>
                  </Link>
                ))}
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </>
  );
}
