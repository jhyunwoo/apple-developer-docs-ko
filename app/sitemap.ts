import type { MetadataRoute } from "next";

import { getAllDocuments } from "@/lib/content";
import { toAbsoluteUrl } from "@/lib/seo";

export const dynamic = "force-static";

function getPriority(route: string) {
  if (route === "/") {
    return 1;
  }
  if (route.split("/").filter(Boolean).length <= 2) {
    return 0.8;
  }
  return 0.7;
}

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const documents = await getAllDocuments();

  return documents.map((document) => ({
    url: toAbsoluteUrl(document.route),
    lastModified: document.updatedAt ?? undefined,
    changeFrequency: document.route === "/" ? "daily" : "weekly",
    priority: getPriority(document.route)
  }));
}
