/* eslint-disable @next/next/no-img-element */

import type { ComponentPropsWithoutRef, ReactElement, ReactNode } from "react";

import Link from "next/link";
import { compileMDX } from "next-mdx-remote/rsc";
import clsx from "clsx";
import remarkGfm from "remark-gfm";

import { slugifyHeading } from "@/lib/content";

type RouteSet = Set<string>;

function isSafeHref(href: string) {
  if (!href) {
    return false;
  }
  if (href.startsWith("#") || href.startsWith("/")) {
    return true;
  }

  try {
    const url = new URL(href);
    return ["http:", "https:", "mailto:", "tel:"].includes(url.protocol.toLowerCase());
  } catch {
    return false;
  }
}

function sanitizeTextSegment(segment: string) {
  return segment
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\{/g, "&#123;")
    .replace(/\}/g, "&#125;");
}

function sanitizeLinePreservingInlineCode(line: string) {
  const parts = line.split(/(`+[^`]*`+)/g);
  return parts
    .map((part) => (part.startsWith("`") && part.endsWith("`") ? part : sanitizeTextSegment(part)))
    .join("");
}

function sanitizeExternalMarkdown(source: string) {
  const lines = source.split(/\r?\n/);
  const sanitized: string[] = [];
  let inFence = false;

  for (const line of lines) {
    const trimmed = line.trimStart();
    if (/^(```|~~~)/.test(trimmed)) {
      inFence = !inFence;
      sanitized.push(line);
      continue;
    }

    if (inFence) {
      sanitized.push(line);
      continue;
    }

    if (/^(import|export)\b/.test(trimmed)) {
      sanitized.push(`\\${line}`);
      continue;
    }

    sanitized.push(sanitizeLinePreservingInlineCode(line));
  }

  return sanitized.join("\n");
}

function childrenToText(children: ReactNode): string {
  if (typeof children === "string" || typeof children === "number") {
    return String(children);
  }
  if (Array.isArray(children)) {
    return children.map(childrenToText).join("");
  }
  if (children && typeof children === "object" && "props" in children) {
    return childrenToText((children as ReactElement<{ children?: ReactNode }>).props.children);
  }
  return "";
}

function normalizeDeveloperHref(href: string): string | null {
  if (!href) {
    return null;
  }
  if (href.startsWith("#")) {
    return href;
  }
  if (href.startsWith("/")) {
    return href;
  }

  try {
    const url = new URL(href);
    if (url.hostname !== "developer.apple.com") {
      return null;
    }
    const normalizedPathname = url.pathname.replace(/^\/kr(?=\/|$)/, "") || "/";
    return `${normalizedPathname}${url.hash}`;
  } catch {
    return null;
  }
}

function SmartLink({
  children,
  href = "",
  routeSet,
  ...props
}: ComponentPropsWithoutRef<"a"> & { routeSet: RouteSet }) {
  const safeHref = isSafeHref(String(href)) ? String(href) : null;
  const normalized = safeHref ? normalizeDeveloperHref(safeHref) : null;
  const candidateRoute = normalized?.split("#")[0] ?? null;
  const isInternal = normalized !== null && candidateRoute !== null && routeSet.has(candidateRoute);

  if (isInternal && normalized) {
    return (
      <Link href={normalized} className={clsx("inline-link", props.className)}>
        {children}
      </Link>
    );
  }

  if (!safeHref) {
    return <span className={clsx("inline-link", props.className)}>{children}</span>;
  }

  return (
    <a
      {...props}
      className={clsx("inline-link", props.className)}
      href={safeHref}
      rel={safeHref.startsWith("http") ? "noopener noreferrer" : props.rel}
      target={safeHref.startsWith("http") ? "_blank" : props.target}
    >
      {children}
    </a>
  );
}

function Aside({
  kind,
  title,
  children
}: {
  kind: string;
  title: string;
  children: ReactNode;
}) {
  return (
    <aside className={clsx("directive", "aside-block", `aside-${kind}`)}>
      <div className="directive-label">
        <span className="directive-badge">{kind.toUpperCase()}</span>
        <strong>{title}</strong>
      </div>
      <div className="directive-body">{children}</div>
    </aside>
  );
}

function TopicGrid({ children }: { children: ReactNode }) {
  return <section className="directive topic-grid">{children}</section>;
}

function DeclarationBlock({
  language,
  children
}: {
  language?: string;
  children: ReactNode;
}) {
  return (
    <section className="directive code-shell">
      <div className="directive-label">
        <span className="directive-badge">API</span>
        <strong>{language ? `${language} 선언` : "선언"}</strong>
      </div>
      <div className="directive-body">{children}</div>
    </section>
  );
}

function AvailabilityBlock({ children }: { children: ReactNode }) {
  return (
    <section className="directive availability-block">
      <div className="directive-label">
        <span className="directive-badge">AVAILABILITY</span>
        <strong>지원 범위</strong>
      </div>
      <div className="directive-body">{children}</div>
    </section>
  );
}

function TermList({ children }: { children: ReactNode }) {
  return <section className="directive term-list">{children}</section>;
}

function VideoTranscript({ children }: { children: ReactNode }) {
  return (
    <section className="directive transcript-block">
      <div className="directive-label">
        <span className="directive-badge">TRANSCRIPT</span>
        <strong>비디오 대본</strong>
      </div>
      <div className="directive-body">{children}</div>
    </section>
  );
}

function AssetList({ children }: { children: ReactNode }) {
  return (
    <details className="directive asset-list">
      <summary>자산 추적 보기</summary>
      <div className="directive-body">{children}</div>
    </details>
  );
}

function createHeadingComponent(level: 1 | 2 | 3 | 4 | 5 | 6, counts: Map<string, number>) {
  const tag = `h${level}` as const;

  return function Heading({
    children,
    className,
    ...props
  }: ComponentPropsWithoutRef<typeof tag>) {
    const text = childrenToText(children);
    const id = slugifyHeading(text, counts);
    const Tag = tag;
    return (
      <Tag id={id} className={clsx("doc-heading", `doc-heading-${level}`, className)} {...props}>
        <a href={`#${id}`} className="heading-anchor">
          {children}
        </a>
      </Tag>
    );
  };
}

function directiveToJsx(name: string, label: string, body: string): string {
  const trimmedBody = body.trim();
  switch (name) {
    case "topic-grid":
      return `<TopicGrid>\n\n${trimmedBody}\n\n</TopicGrid>`;
    case "term-list":
      return `<TermList>\n\n${trimmedBody}\n\n</TermList>`;
    case "video-transcript":
      return `<VideoTranscript>\n\n${trimmedBody}\n\n</VideoTranscript>`;
    case "asset-list":
      return `<AssetList>\n\n${trimmedBody}\n\n</AssetList>`;
    case "declaration":
      return `<DeclarationBlock language=${JSON.stringify(label)}>\n\n${trimmedBody}\n\n</DeclarationBlock>`;
    case "availability":
      return `<AvailabilityBlock>\n\n${trimmedBody}\n\n</AvailabilityBlock>`;
    default:
      return `<Aside kind=${JSON.stringify(name)} title=${JSON.stringify(label || name)}>\n\n${trimmedBody}\n\n</Aside>`;
  }
}

export function transformDirectiveBlocks(markdown: string): string {
  const lines = markdown.split(/\r?\n/);
  const output: string[] = [];
  let active:
    | {
        name: string;
        label: string;
        lines: string[];
      }
    | null = null;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!active && trimmed.startsWith(":::") && trimmed !== ":::") {
      const raw = trimmed.slice(3).trim();
      const [name, ...rest] = raw.split(/\s+/);
      active = {
        name,
        label: rest.join(" ").trim(),
        lines: []
      };
      continue;
    }

    if (active && trimmed === ":::") {
      output.push(directiveToJsx(active.name, active.label, active.lines.join("\n")));
      active = null;
      continue;
    }

    if (active) {
      active.lines.push(line);
      continue;
    }

    output.push(line);
  }

  if (active) {
    output.push(`:::${active.name}${active.label ? ` ${active.label}` : ""}`);
    output.push(...active.lines);
  }

  return output.join("\n");
}

export async function renderMdxDocument(source: string, routeSet: RouteSet) {
  const headingCounts = new Map<string, number>();
  const mdxSource = transformDirectiveBlocks(sanitizeExternalMarkdown(source));
  const { content } = await compileMDX({
    source: mdxSource,
    options: {
      parseFrontmatter: false,
      mdxOptions: {
        remarkPlugins: [remarkGfm]
      }
    },
    components: {
      a: (props) => <SmartLink {...props} routeSet={routeSet} />,
      img: (props) => {
        const safeSrc = isSafeHref(String(props.src ?? "")) ? String(props.src) : null;
        if (!safeSrc) {
          return props.alt ? <span className="image-fallback">{props.alt}</span> : null;
        }

        return (
          <img
            {...props}
            src={safeSrc}
            className={clsx("doc-image", props.className)}
            alt={props.alt ?? ""}
            loading={props.loading ?? "lazy"}
            decoding="async"
          />
        );
      },
      pre: (props) => <pre {...props} className={clsx("doc-pre", props.className)} />,
      code: (props) => <code {...props} className={clsx("doc-code", props.className)} />,
      table: (props) => <div className="table-wrap"><table {...props} /></div>,
      TopicGrid,
      Aside,
      DeclarationBlock,
      AvailabilityBlock,
      TermList,
      VideoTranscript,
      AssetList,
      h1: createHeadingComponent(1, headingCounts),
      h2: createHeadingComponent(2, headingCounts),
      h3: createHeadingComponent(3, headingCounts),
      h4: createHeadingComponent(4, headingCounts),
      h5: createHeadingComponent(5, headingCounts),
      h6: createHeadingComponent(6, headingCounts)
    }
  });

  return content;
}
