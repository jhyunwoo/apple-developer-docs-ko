import "server-only";

import fs from "node:fs/promises";
import path from "node:path";

import { cache } from "react";

export interface DocHeading {
  depth: number;
  text: string;
}

export interface DocHeadingWithId extends DocHeading {
  id: string;
}

export interface DocDocument {
  route: string;
  slugSegments: string[];
  section: string;
  title: string;
  originalTitle: string;
  sourceLocale: string;
  canonicalSource: string;
  body: string;
  bodyText: string;
  headings: DocHeading[];
  relativePath: string;
  snippet: string;
  sourceUrl: string | null;
  contentType: string | null;
  updatedAt: string | null;
}

export interface ContentManifest {
  generatedAt: string;
  contentHash: string;
  count: number;
  sections: string[];
  documents: DocDocument[];
}

export interface SidebarItem {
  route: string;
  title: string;
  active: boolean;
}

export interface SidebarSection {
  id: string;
  label: string;
  count: number;
  items: SidebarItem[];
}

export interface BreadcrumbItem {
  href: string;
  label: string;
}

const manifestPath = path.join(process.cwd(), ".generated", "content-manifest.json");

const sectionLabels: Record<string, string> = {
  archive: "Archive",
  docc: "Documentation",
  hig: "Human Interface Guidelines",
  public: "Apple Developer",
  videos: "Videos"
};

export const getManifest = cache(async (): Promise<ContentManifest> => {
  const raw = await fs.readFile(manifestPath, "utf8");
  return JSON.parse(raw) as ContentManifest;
});

export async function getAllDocuments(): Promise<DocDocument[]> {
  const manifest = await getManifest();
  return [...manifest.documents].sort((left, right) => left.route.localeCompare(right.route));
}

export async function getDocumentByRoute(route: string): Promise<DocDocument | null> {
  const documents = await getAllDocuments();
  return documents.find((document) => document.route === route) ?? null;
}

export async function getDocumentBySegments(slugSegments: string[]): Promise<DocDocument | null> {
  const route = slugSegments.length === 0 ? "/" : `/${slugSegments.join("/")}`;
  return getDocumentByRoute(route);
}

export function getSectionLabel(section: string): string {
  return sectionLabels[section] ?? prettifySegment(section);
}

export function prettifySegment(segment: string): string {
  return segment
    .replace(/[-_]+/g, " ")
    .replace(/\b\w/g, (character) => character.toUpperCase());
}

export function slugifyHeading(text: string, counts?: Map<string, number>): string {
  const base = text
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^\p{L}\p{N}\s-]/gu, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "") || "section";

  if (!counts) {
    return base;
  }

  const nextCount = (counts.get(base) ?? 0) + 1;
  counts.set(base, nextCount);
  return nextCount === 1 ? base : `${base}-${nextCount}`;
}

export function withHeadingIds(headings: DocHeading[]): DocHeadingWithId[] {
  const counts = new Map<string, number>();
  return headings.map((heading) => ({
    ...heading,
    id: slugifyHeading(heading.text, counts)
  }));
}

export function buildSidebarSections(documents: DocDocument[], currentRoute: string): SidebarSection[] {
  const bySection = new Map<string, DocDocument[]>();
  for (const document of documents) {
    const sectionDocs = bySection.get(document.section) ?? [];
    sectionDocs.push(document);
    bySection.set(document.section, sectionDocs);
  }

  return [...bySection.entries()]
    .sort(([left], [right]) => getSectionLabel(left).localeCompare(getSectionLabel(right)))
    .map(([section, sectionDocs]) => ({
      id: section,
      label: getSectionLabel(section),
      count: sectionDocs.length,
      items: [...sectionDocs]
        .sort((left, right) => left.title.localeCompare(right.title))
        .map((document) => ({
          route: document.route,
          title: document.title,
          active: document.route === currentRoute
        }))
    }));
}

export function buildBreadcrumbs(route: string, documents: DocDocument[]): BreadcrumbItem[] {
  if (route === "/") {
    return [{ href: "/", label: "홈" }];
  }

  const items: BreadcrumbItem[] = [{ href: "/", label: "홈" }];
  const segments = route.split("/").filter(Boolean);
  for (let index = 0; index < segments.length; index += 1) {
    const href = `/${segments.slice(0, index + 1).join("/")}`;
    const matchingDocument = documents.find((document) => document.route === href);
    items.push({
      href,
      label: matchingDocument?.title ?? prettifySegment(segments[index] ?? "")
    });
  }
  return items;
}

export function getRecentDocuments(documents: DocDocument[], limit = 8): DocDocument[] {
  return [...documents]
    .sort((left, right) => (right.updatedAt ?? "").localeCompare(left.updatedAt ?? ""))
    .slice(0, limit);
}
