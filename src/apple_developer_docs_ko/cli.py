from __future__ import annotations

import argparse
import sys

from .config import Settings
from .pipeline import MirrorPipeline
from .translate import build_translator
from .verification import format_report, verify_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="apple-docs-ko")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_parser = subparsers.add_parser("sync", help="Discover, fetch, translate, and render pages.")
    sync_parser.add_argument(
        "--sections",
        default="docc,hig,videos,archive,public",
        help="Comma-separated adapter list.",
    )
    sync_parser.add_argument("--limit", type=int, default=None, help="Maximum number of routes to process.")
    sync_parser.add_argument("--dry-run", action="store_true", help="Discover/fetch without writing output.")
    sync_parser.add_argument(
        "--identity-translation",
        action="store_true",
        help="Skip real translation and keep translatable blocks unchanged.",
    )

    subparsers.add_parser("build-site", help="Render HTML from content Markdown.")
    subparsers.add_parser("verify-output", help="Audit manifest, Markdown, and HTML outputs.")

    seed_parser = subparsers.add_parser("seed-queue", help="Seed the sequential translation queue with stable top-level routes.")
    seed_parser.add_argument(
        "--sections",
        default="docc,hig,videos,archive,public",
        help="Comma-separated adapter list.",
    )
    seed_parser.add_argument("--limit", type=int, default=None, help="Maximum number of routes to enqueue.")
    seed_parser.add_argument(
        "--per-section-limit",
        type=int,
        default=None,
        help="Maximum number of routes to enqueue per section.",
    )
    seed_parser.add_argument("--reset", action="store_true", help="Clear the existing queue before seeding.")

    extend_parser = subparsers.add_parser(
        "extend-queue",
        help="Incrementally expand persisted discovery frontiers and append newly found routes to the queue.",
    )
    extend_parser.add_argument(
        "--sections",
        default="docc,videos,public",
        help="Comma-separated adapter list.",
    )
    extend_parser.add_argument(
        "--expand-routes",
        type=int,
        default=100,
        help="Number of frontier routes to expand per section.",
    )

    status_parser = subparsers.add_parser("queue-status", help="Show translation queue progress and next routes.")
    status_parser.add_argument("--next", type=int, default=10, help="Number of queued routes to show.")

    subparsers.add_parser("reconcile-queue", help="Update queue progress from current pages/translations.")

    smoke_parser = subparsers.add_parser("smoke-test", help="Run representative adapter fetches.")
    smoke_parser.add_argument("--dry-run", action="store_true")
    smoke_parser.add_argument("--identity-translation", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    settings = Settings.from_env()
    translator = build_translator(
        identity=getattr(args, "identity_translation", False),
        api_key=settings.openai_api_key,
        model=settings.openai_model,
    )
    pipeline = MirrorPipeline(settings, translator)
    try:
        if args.command == "sync":
            sections = [section.strip() for section in args.sections.split(",") if section.strip()]
            result = pipeline.sync(sections=sections, limit=args.limit, dry_run=args.dry_run)
            print(f"Processed {len(result.processed_routes)} routes")
            return 0
        if args.command == "build-site":
            pipeline.build_site()
            print(f"Built site into {settings.dist_dir}")
            return 0
        if args.command == "verify-output":
            report = verify_outputs(settings)
            print(format_report(report))
            return 0 if report.ok else 1
        if args.command == "seed-queue":
            sections = [section.strip() for section in args.sections.split(",") if section.strip()]
            result = pipeline.seed_translation_queue(
                sections=sections,
                limit=args.limit,
                per_section_limit=args.per_section_limit,
                reset=args.reset,
            )
            print(
                f"Seeded queue: inserted={result.inserted} total={result.total} "
                f"translated={result.translated} queued={result.queued}"
            )
            return 0
        if args.command == "extend-queue":
            sections = [section.strip() for section in args.sections.split(",") if section.strip()]
            result = pipeline.extend_translation_queue(
                sections=sections,
                expand_routes=args.expand_routes,
            )
            print(
                f"Extended queue: expanded={result.expanded} discovered={result.discovered} "
                f"total={result.total} translated={result.translated} queued={result.queued}"
            )
            return 0
        if args.command == "queue-status":
            counts, next_items = pipeline.get_translation_queue_status(next_limit=args.next)
            print(
                "Queue status: "
                f"total={counts['total']} translated={counts['translated']} queued={counts['queued']} "
                f"in_progress={counts['in_progress']} blocked={counts['blocked']} skipped={counts['skipped']}"
            )
            if next_items:
                print("Next routes:")
                for row in next_items:
                    title = row["title"] or "-"
                    print(f"- {row['ordinal']}: [{row['section']}] {row['route']} :: {title}")
            return 0
        if args.command == "reconcile-queue":
            updated = pipeline.reconcile_translation_queue()
            print(f"Reconciled queue entries: {updated}")
            return 0
        if args.command == "smoke-test":
            result = pipeline.smoke_test(dry_run=args.dry_run)
            print(f"Smoke-tested {len(result.processed_routes)} routes")
            return 0
        parser.error(f"Unknown command: {args.command}")
    finally:
        pipeline.close()
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
