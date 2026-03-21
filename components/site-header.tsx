import Link from "next/link";

import { HeaderActions } from "@/components/header-actions";
import type { SidebarSection } from "@/lib/content";

export function SiteHeader({
  sidebarSections,
  currentRoute,
  subtitle = "번역 파이프라인이 생성한 Markdown을 정적으로 서비스합니다."
}: {
  sidebarSections: SidebarSection[];
  currentRoute: string;
  subtitle?: string;
}) {
  return (
    <header className="site-header">
      <div className="site-header-inner">
        <div className="site-brand">
          <Link href="/" className="site-brand-link">
            Apple Developer Docs KO
          </Link>
          <p>{subtitle}</p>
        </div>
        <HeaderActions sidebarSections={sidebarSections} currentRoute={currentRoute} />
      </div>
    </header>
  );
}
