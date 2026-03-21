"use client";

import Link from "next/link";
import { useState } from "react";

import type { SidebarSection } from "@/lib/content";

export function MobileNav({
  sections,
  currentRoute
}: {
  sections: SidebarSection[];
  currentRoute: string;
}) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button type="button" className="mobile-nav-trigger" onClick={() => setOpen(true)}>
        메뉴
      </button>
      {open ? (
        <div className="mobile-nav-overlay">
          <div className="search-backdrop" onClick={() => setOpen(false)} />
          <div className="mobile-nav-panel">
            <div className="mobile-nav-header">
              <strong>문서 탐색</strong>
              <button type="button" className="ghost-button" onClick={() => setOpen(false)}>
                닫기
              </button>
            </div>
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
                        className={item.route === currentRoute ? "sidebar-link active" : "sidebar-link"}
                        onClick={() => setOpen(false)}
                      >
                        {item.title}
                      </Link>
                    ))}
                  </div>
                </section>
              ))}
            </nav>
          </div>
        </div>
      ) : null}
    </>
  );
}
