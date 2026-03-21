"use client";

import dynamic from "next/dynamic";

import type { SidebarSection } from "@/lib/content";

const SearchDialog = dynamic(
  () => import("@/components/search-dialog").then((module) => module.SearchDialog),
  {
    ssr: false,
    loading: () => (
      <button type="button" className="search-trigger" disabled>
        <span>문서 검색</span>
        <kbd>⌘K</kbd>
      </button>
    )
  }
);

const ThemeToggle = dynamic(
  () => import("@/components/theme-toggle").then((module) => module.ThemeToggle),
  {
    ssr: false,
    loading: () => (
      <button type="button" className="theme-toggle" aria-label="테마 전환" disabled>
        <span>테마</span>
      </button>
    )
  }
);

const MobileNav = dynamic(
  () => import("@/components/mobile-nav").then((module) => module.MobileNav),
  {
    ssr: false,
    loading: () => (
      <button type="button" className="mobile-nav-trigger" disabled>
        메뉴
      </button>
    )
  }
);

export function HeaderActions({
  sidebarSections,
  currentRoute
}: {
  sidebarSections: SidebarSection[];
  currentRoute: string;
}) {
  return (
    <div className="site-header-actions">
      <SearchDialog />
      <ThemeToggle />
      <MobileNav sections={sidebarSections} currentRoute={currentRoute} />
    </div>
  );
}
