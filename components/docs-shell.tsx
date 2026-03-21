import type { ReactNode } from "react";

import Link from "next/link";

import { SiteHeader } from "@/components/site-header";
import type { BreadcrumbItem, DocDocument, DocHeadingWithId, SidebarSection } from "@/lib/content";

function Sidebar({ sections }: { sections: SidebarSection[] }) {
  return (
    <nav className="sidebar-nav">
      {sections.map((section) => (
        <section key={section.id} className="sidebar-group">
          <div className="sidebar-group-header">
            <span>{section.label}</span>
            <small>{section.count}</small>
          </div>
          <div className="sidebar-items">
            {section.items.map((item) => (
              <Link
                key={item.route}
                href={item.route}
                prefetch={false}
                className={item.active ? "sidebar-link active" : "sidebar-link"}
              >
                {item.title}
              </Link>
            ))}
          </div>
        </section>
      ))}
    </nav>
  );
}

function Breadcrumbs({ items }: { items: BreadcrumbItem[] }) {
  return (
    <nav className="breadcrumbs" aria-label="Breadcrumb">
      {items.map((item, index) => (
        <span key={item.href} className="breadcrumb-item">
          <Link href={item.href}>{item.label}</Link>
          {index < items.length - 1 ? <span className="breadcrumb-separator">/</span> : null}
        </span>
      ))}
    </nav>
  );
}

function TableOfContents({ headings }: { headings: DocHeadingWithId[] }) {
  const visibleHeadings = headings.filter((heading) => heading.depth >= 2 && heading.depth <= 3);
  if (visibleHeadings.length === 0) {
    return null;
  }

  return (
    <nav className="toc" aria-label="Table of contents">
      <div className="toc-header">이 문서에서</div>
      <div className="toc-items">
        {visibleHeadings.map((heading) => (
          <a
            key={heading.id}
            href={`#${heading.id}`}
            className={heading.depth === 2 ? "toc-link" : "toc-link toc-link-nested"}
          >
            {heading.text}
          </a>
        ))}
      </div>
    </nav>
  );
}

export function DocsShell({
  document,
  body,
  sidebarSections,
  breadcrumbs,
  headingItems
}: {
  document: DocDocument;
  body: ReactNode;
  sidebarSections: SidebarSection[];
  breadcrumbs: BreadcrumbItem[];
  headingItems: DocHeadingWithId[];
}) {
  return (
    <div className="site-frame">
      <SiteHeader sidebarSections={sidebarSections} currentRoute={document.route} />
      <div className="content-frame">
        <aside className="left-rail">
          <Sidebar sections={sidebarSections} />
        </aside>
        <main className="main-column">
          <div className="article-hero">
            <Breadcrumbs items={breadcrumbs} />
            <div className="article-meta">
              <span className="section-pill">{document.section}</span>
              <span>{document.sourceLocale}</span>
              <span>{document.canonicalSource}</span>
            </div>
            <div className="article-heading">
              <h1>{document.title}</h1>
              {document.originalTitle !== document.title ? <p>{document.originalTitle}</p> : null}
            </div>
          </div>
          <article className="doc-article">{body}</article>
        </main>
        <aside className="right-rail">
          <TableOfContents headings={headingItems} />
        </aside>
      </div>
    </div>
  );
}
