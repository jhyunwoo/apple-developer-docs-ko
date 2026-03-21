import type { Metadata } from "next";
import Link from "next/link";

import { DocsShell } from "@/components/docs-shell";
import { SiteHeader } from "@/components/site-header";
import { StructuredData } from "@/components/structured-data";
import {
  buildBreadcrumbs,
  buildSidebarSections,
  getAllDocuments,
  getDocumentByRoute,
  getRecentDocuments,
  getSectionLabel,
  withHeadingIds
} from "@/lib/content";
import { renderMdxDocument } from "@/lib/mdx";
import { getHomeMetadata, getWebsiteStructuredData } from "@/lib/seo";

export async function generateMetadata(): Promise<Metadata> {
  const documents = await getAllDocuments();
  return getHomeMetadata(documents.length);
}

export default async function HomePage() {
  const documents = await getAllDocuments();
  const routeSet = new Set(documents.map((document) => document.route));
  const rootDocument = await getDocumentByRoute("/");

  if (rootDocument) {
    const body = await renderMdxDocument(rootDocument.body, routeSet);
    return (
      <DocsShell
        document={rootDocument}
        body={
          <>
            <StructuredData data={getWebsiteStructuredData(documents.length)} />
            {body}
          </>
        }
        sidebarSections={buildSidebarSections(documents, rootDocument.route)}
        breadcrumbs={buildBreadcrumbs(rootDocument.route, documents)}
        headingItems={withHeadingIds(rootDocument.headings)}
      />
    );
  }

  const recentDocuments = getRecentDocuments(documents);
  const sectionSummaries = buildSidebarSections(documents, "/");

  return (
    <div className="site-frame">
      <StructuredData data={getWebsiteStructuredData(documents.length)} />
      <SiteHeader sidebarSections={sectionSummaries} currentRoute="/" subtitle="정적 사이트 레이어가 현재 번역 코퍼스를 서비스합니다." />
      <main className="landing-page">
        <section className="landing-hero">
          <div className="landing-copy">
            <span className="landing-pill">Static Docs Site</span>
            <h1>Apple Developer 번역 문서를 Next.js 정적 사이트로 제공합니다.</h1>
            <p>
              현재 저장소의 `content/` Markdown을 그대로 읽어 한국어 문서를 서비스합니다. 원본 크롤링과 번역은
              Python 파이프라인이 담당하고, 웹사이트는 Next.js App Router와 MDX 렌더링 레이어가 맡습니다.
            </p>
            <div className="landing-actions">
              <Link
                href={recentDocuments[0]?.route ?? "/design/human-interface-guidelines"}
                prefetch={false}
                className="primary-button"
              >
                문서 둘러보기
              </Link>
              <a href="/__search__/manifest.json" className="secondary-button">
                검색 인덱스 확인
              </a>
            </div>
          </div>
          <div className="landing-stats">
            <div className="stat-card">
              <strong>{documents.length}</strong>
              <span>현재 서비스 중인 문서</span>
            </div>
            <div className="stat-card">
              <strong>{sectionSummaries.length}</strong>
              <span>섹션 단위 탐색</span>
            </div>
          </div>
        </section>

        <section className="landing-grid">
          <div className="landing-panel">
            <div className="panel-header">
              <h2>섹션</h2>
              <p>현재 빌드된 문서를 섹션별로 살펴볼 수 있습니다.</p>
            </div>
            <div className="section-card-grid">
              {sectionSummaries.map((section) => (
                <article key={section.id} className="section-card">
                  <div className="section-card-header">
                    <strong>{section.label}</strong>
                    <span>{section.count}</span>
                  </div>
                  <div className="section-card-links">
                    {section.items.slice(0, 4).map((item) => (
                      <Link key={item.route} href={item.route} prefetch={false}>
                        {item.title}
                      </Link>
                    ))}
                  </div>
                </article>
              ))}
            </div>
          </div>

          <div className="landing-panel">
            <div className="panel-header">
              <h2>최근 반영 문서</h2>
              <p>최근 번역/동기화 시간이 기록된 순서대로 보여 줍니다.</p>
            </div>
            <div className="recent-list">
              {recentDocuments.map((document) => (
                <Link key={document.route} href={document.route} prefetch={false} className="recent-item">
                  <div>
                    <strong>{document.title}</strong>
                    <p>{document.snippet}</p>
                  </div>
                  <span>{getSectionLabel(document.section)}</span>
                </Link>
              ))}
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
