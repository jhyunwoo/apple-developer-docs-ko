import type { MetadataRoute } from "next";

import { getSiteOrigin } from "@/lib/seo";

export const dynamic = "force-static";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        disallow: ["/__search__/", "/__mirror__/", "/_next/"]
      }
    ],
    sitemap: `${getSiteOrigin()}/sitemap.xml`,
    host: getSiteOrigin()
  };
}
