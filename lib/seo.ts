import type { Metadata } from "next";

import type { BreadcrumbItem, DocDocument } from "@/lib/content";
import { getSectionLabel } from "@/lib/content";

const defaultSiteOrigin = "http://localhost:3000";
const siteName = "Apple Developer Docs KO";
const defaultDescription = "Apple Developer 공개 문서를 한국어 Markdown으로 제공하는 정적 문서 사이트입니다.";

function dedupe(items: string[]) {
  return [...new Set(items.filter(Boolean))];
}

function trimDescription(value: string | null | undefined, fallback = defaultDescription) {
  const basis = (value ?? "").trim() || fallback;
  return basis.length <= 160 ? basis : `${basis.slice(0, 157).trimEnd()}...`;
}

export function getSiteOrigin() {
  const raw = process.env.NEXT_PUBLIC_SITE_URL ?? process.env.SITE_URL ?? defaultSiteOrigin;
  return raw.replace(/\/+$/, "");
}

export function toAbsoluteUrl(route: string) {
  const normalizedRoute = route === "/" ? "/" : `${route.replace(/\/+$/, "")}/`;
  return new URL(normalizedRoute, `${getSiteOrigin()}/`).toString();
}

export function getBaseMetadata(): Metadata {
  const origin = getSiteOrigin();
  return {
    metadataBase: new URL(origin),
    applicationName: siteName,
    title: {
      default: siteName,
      template: "%s · Apple Developer Docs KO"
    },
    description: defaultDescription,
    category: "technology",
    alternates: {
      canonical: "/"
    },
    openGraph: {
      type: "website",
      locale: "ko_KR",
      siteName,
      title: siteName,
      description: defaultDescription,
      url: toAbsoluteUrl("/")
    },
    twitter: {
      card: "summary",
      title: siteName,
      description: defaultDescription
    },
    referrer: "strict-origin-when-cross-origin",
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        "max-image-preview": "large",
        "max-snippet": -1,
        "max-video-preview": -1
      }
    }
  };
}

export function getHomeMetadata(documentCount: number): Metadata {
  const description = trimDescription(
    `${defaultDescription} 현재 ${documentCount}개의 번역 문서를 정적 사이트에서 탐색하고 검색할 수 있습니다.`
  );

  return {
    title: "한국어 Apple Developer 문서",
    description,
    keywords: [
      "Apple Developer",
      "Apple 문서 번역",
      "한국어 개발자 문서",
      "Swift 문서",
      "iOS 문서",
      "macOS 문서"
    ],
    alternates: {
      canonical: "/"
    },
    openGraph: {
      type: "website",
      locale: "ko_KR",
      siteName,
      title: "한국어 Apple Developer 문서",
      description,
      url: toAbsoluteUrl("/")
    },
    twitter: {
      card: "summary",
      title: "한국어 Apple Developer 문서",
      description
    }
  };
}

export function getDocumentMetadata(document: DocDocument): Metadata {
  const sectionLabel = getSectionLabel(document.section);
  const description = trimDescription(document.snippet);
  const keywords = dedupe([
    document.title,
    document.originalTitle,
    document.section,
    sectionLabel,
    document.contentType ?? "",
    ...document.headings.slice(0, 8).map((heading) => heading.text)
  ]);

  return {
    title: document.title,
    description,
    keywords,
    category: sectionLabel,
    alternates: {
      canonical: document.route
    },
    authors: [{ name: siteName }],
    other: document.sourceUrl
      ? {
          "source-url": document.sourceUrl
        }
      : undefined,
    openGraph: {
      type: document.section === "videos" ? "video.other" : "article",
      locale: "ko_KR",
      siteName,
      title: document.title,
      description,
      url: toAbsoluteUrl(document.route)
    },
    twitter: {
      card: "summary",
      title: document.title,
      description
    },
    robots: {
      index: true,
      follow: true,
      googleBot: {
        index: true,
        follow: true,
        "max-image-preview": "large",
        "max-snippet": -1,
        "max-video-preview": -1
      }
    }
  };
}

export function getWebsiteStructuredData(documentCount: number) {
  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": `${toAbsoluteUrl("/")}#website`,
        name: siteName,
        url: toAbsoluteUrl("/"),
        inLanguage: "ko-KR",
        description: defaultDescription
      },
      {
        "@type": "CollectionPage",
        "@id": `${toAbsoluteUrl("/")}#collection`,
        name: siteName,
        url: toAbsoluteUrl("/"),
        inLanguage: "ko-KR",
        description: trimDescription(
          `${defaultDescription} 현재 ${documentCount}개의 번역 문서를 탐색하고 검색할 수 있습니다.`
        ),
        isPartOf: {
          "@id": `${toAbsoluteUrl("/")}#website`
        }
      }
    ]
  };
}

export function getDocumentStructuredData(document: DocDocument, breadcrumbs: BreadcrumbItem[]) {
  const breadcrumbList = breadcrumbs.map((item, index) => ({
    "@type": "ListItem",
    position: index + 1,
    name: item.label,
    item: toAbsoluteUrl(item.href)
  }));

  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": `${toAbsoluteUrl("/")}#website`,
        name: siteName,
        url: toAbsoluteUrl("/"),
        inLanguage: "ko-KR"
      },
      {
        "@type": "BreadcrumbList",
        "@id": `${toAbsoluteUrl(document.route)}#breadcrumbs`,
        itemListElement: breadcrumbList
      },
      {
        "@type": document.section === "videos" ? "VideoObject" : "TechArticle",
        "@id": `${toAbsoluteUrl(document.route)}#document`,
        headline: document.title,
        alternativeHeadline: document.originalTitle !== document.title ? document.originalTitle : undefined,
        description: trimDescription(document.snippet),
        inLanguage: "ko-KR",
        url: toAbsoluteUrl(document.route),
        dateModified: document.updatedAt ?? undefined,
        articleSection: getSectionLabel(document.section),
        isPartOf: {
          "@id": `${toAbsoluteUrl("/")}#website`
        },
        isBasedOn: document.sourceUrl ?? undefined,
        keywords: dedupe([
          document.title,
          document.originalTitle,
          ...document.headings.slice(0, 8).map((heading) => heading.text)
        ]).join(", ")
      }
    ]
  };
}
