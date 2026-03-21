import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { DocsShell } from "@/components/docs-shell";
import { StructuredData } from "@/components/structured-data";
import {
  buildBreadcrumbs,
  buildSidebarSections,
  getAllDocuments,
  getDocumentBySegments,
  withHeadingIds
} from "@/lib/content";
import { renderMdxDocument } from "@/lib/mdx";
import { getDocumentMetadata, getDocumentStructuredData } from "@/lib/seo";

export async function generateStaticParams() {
  const documents = await getAllDocuments();
  return documents
    .filter((document) => document.route !== "/")
    .map((document) => ({
      slug: document.slugSegments
    }));
}

export async function generateMetadata({
  params
}: {
  params: Promise<{ slug: string[] }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const document = await getDocumentBySegments(slug);
  if (!document) {
    return {};
  }
  return getDocumentMetadata(document);
}

export default async function DocumentPage({
  params
}: {
  params: Promise<{ slug: string[] }>;
}) {
  const { slug } = await params;
  const documents = await getAllDocuments();
  const document = await getDocumentBySegments(slug);

  if (!document) {
    notFound();
  }

  const routeSet = new Set(documents.map((entry) => entry.route));
  const breadcrumbs = buildBreadcrumbs(document.route, documents);
  const body = await renderMdxDocument(document.body, routeSet);

  return (
    <DocsShell
      document={document}
      body={
        <>
          <StructuredData data={getDocumentStructuredData(document, breadcrumbs)} />
          {body}
        </>
      }
      sidebarSections={buildSidebarSections(documents, document.route)}
      breadcrumbs={breadcrumbs}
      headingItems={withHeadingIds(document.headings)}
    />
  );
}
