# Apple Developer Docs KO Mirror

Resumable crawler, normalizer, translator, markdown renderer, and Next.js static docs
site for public Apple Developer content.

## What It Does

- Crawls public Apple Developer sections with specialized adapters.
- Prefers Apple's official Korean pages when available.
- Stores Korean Markdown as the canonical content format.
- Mirrors public assets into a local cache tree.
- Builds a static-export Next.js site from the generated Markdown.

## Quick Start

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
apple-docs-ko sync --limit 5 --identity-translation

export PATH="/opt/homebrew/bin:$PATH"
npm install
npm run build
```

`--identity-translation` is useful for parser smoke tests when no external translator
credentials are configured. For real English-to-Korean translation, configure a
translator backend such as `OPENAI_API_KEY`.

## Website Workflow

The root folder now acts as a Next.js App Router project.

```bash
export PATH="/opt/homebrew/bin:$PATH"
npm install
export NEXT_PUBLIC_SITE_URL="https://your-domain.example"
npm run dev
npm run build
npm run lint
```

Build-time preparation happens automatically before `dev` and `build`:

- parses every `content/**/index.md`
- generates `.generated/content-manifest.json`
- generates section-sharded search indexes under `public/__search__/`
- copies mirrored assets from `.cache/assets/` to `public/__mirror__/`

The website preserves canonical Apple-style routes from frontmatter `route` values.
Set `NEXT_PUBLIC_SITE_URL` or `SITE_URL` in production so canonical URLs, `sitemap.xml`,
and `robots.txt` use the real deployment domain instead of the local default.

## Python CLI

```bash
apple-docs-ko sync [--sections docc,hig,videos,archive,public] [--limit N] [--dry-run]
apple-docs-ko build-site
apple-docs-ko verify-output
apple-docs-ko seed-queue [--sections docc,hig,videos,archive,public] [--limit N] [--per-section-limit N] [--reset]
apple-docs-ko queue-status [--next N]
apple-docs-ko reconcile-queue
apple-docs-ko extend-queue [--sections docc,hig,videos,archive,public] [--expand-routes N]
apple-docs-ko smoke-test
```

## Sequential Workflow

```bash
# 1. Seed a deterministic translation queue from the start of the site crawl
apple-docs-ko seed-queue --sections docc,hig,videos,archive,public --per-section-limit 10 --reset

# 2. Check progress and the next routes to translate
apple-docs-ko queue-status --next 10

# 3. After writing/refreshing translated pages, reconcile progress
apple-docs-ko reconcile-queue
apple-docs-ko verify-output
```
