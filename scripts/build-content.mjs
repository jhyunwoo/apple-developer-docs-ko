import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";

import matter from "gray-matter";
import { globby } from "globby";

const rootDir = process.cwd();
const generatedDir = path.join(rootDir, ".generated");
const publicDir = path.join(rootDir, "public");
const searchDir = path.join(publicDir, "__search__");
const searchSectionsDir = path.join(searchDir, "sections");
const mirrorSourceDir = path.join(rootDir, ".cache", "assets");
const mirrorTargetDir = path.join(publicDir, "__mirror__");

function toRoute(relativePath, frontmatterRoute) {
  if (typeof frontmatterRoute === "string" && frontmatterRoute.trim()) {
    return frontmatterRoute.trim();
  }
  const normalized = relativePath.replaceAll(path.sep, "/");
  const fallback = normalized.replace(/^content/, "").replace(/\/index\.md$/, "");
  return fallback || "/";
}

function extractHeadings(markdown) {
  const headings = [];
  const lines = markdown.split(/\r?\n/);
  let inFence = false;
  for (const line of lines) {
    if (line.trimStart().startsWith("```")) {
      inFence = !inFence;
      continue;
    }
    if (inFence) {
      continue;
    }
    const match = /^(#{1,6})\s+(.*)$/.exec(line);
    if (!match) {
      continue;
    }
    headings.push({
      depth: match[1].length,
      text: match[2].trim()
    });
  }
  return headings;
}

function stripMarkdown(markdown) {
  return markdown
    .replace(/^:::[^\n]*$/gm, "")
    .replace(/`{3}[\s\S]*?`{3}/g, " ")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, "$1")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, "$1")
    .replace(/^>\s?/gm, "")
    .replace(/[*_~]/g, "")
    .replace(/^#+\s+/gm, "")
    .replace(/^\s*[-*+]\s+/gm, "")
    .replace(/^\s*\d+\.\s+/gm, "")
    .replace(/\r?\n+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function snippetFromText(text, title) {
  const basis = text.startsWith(title) ? text.slice(title.length).trim() : text;
  return basis.slice(0, 220).trim();
}

function buildSearchDoc(entry) {
  return {
    route: entry.route,
    section: entry.section,
    title: entry.title,
    headings: entry.headings.map((heading) => heading.text),
    snippet: entry.snippet,
    body: entry.bodyText
  };
}

async function resetDir(targetDir) {
  await fs.rm(targetDir, { recursive: true, force: true });
  await fs.mkdir(targetDir, { recursive: true });
}

async function copyMirrorAssets() {
  await fs.rm(mirrorTargetDir, { recursive: true, force: true });
  try {
    await fs.access(mirrorSourceDir);
  } catch {
    await fs.mkdir(mirrorTargetDir, { recursive: true });
    return 0;
  }
  await fs.cp(mirrorSourceDir, mirrorTargetDir, { recursive: true });
  const files = await globby("**/*", { cwd: mirrorSourceDir, onlyFiles: true });
  return files.length;
}

async function writeJson(targetPath, value) {
  await fs.mkdir(path.dirname(targetPath), { recursive: true });
  await fs.writeFile(targetPath, JSON.stringify(value, null, 2), "utf8");
}

async function main() {
  const files = await globby("content/**/index.md", {
    cwd: rootDir,
    onlyFiles: true,
    followSymbolicLinks: false
  });

  const entries = [];
  for (const relativePath of files.sort()) {
    const absolutePath = path.join(rootDir, relativePath);
    const raw = await fs.readFile(absolutePath, "utf8");
    const parsed = matter(raw);
    const route = toRoute(relativePath, parsed.data.route);
    const slugSegments = route === "/" ? [] : route.split("/").filter(Boolean);
    const section = typeof parsed.data.section === "string" && parsed.data.section
      ? parsed.data.section
      : slugSegments[0] ?? "misc";
    const headings = extractHeadings(parsed.content);
    const bodyText = stripMarkdown(parsed.content);
    const title = typeof parsed.data.title === "string" && parsed.data.title
      ? parsed.data.title
      : headings[0]?.text ?? path.basename(path.dirname(relativePath));
    const entry = {
      route,
      slugSegments,
      section,
      title,
      originalTitle: parsed.data.original_title ?? title,
      sourceLocale: parsed.data.source_locale ?? "unknown",
      canonicalSource: parsed.data.canonical_source ?? "unknown",
      body: parsed.content.trim(),
      bodyText,
      headings,
      relativePath,
      snippet: snippetFromText(bodyText, title),
      sourceUrl: parsed.data.source_url ?? null,
      contentType: parsed.data.content_type ?? null,
      updatedAt: parsed.data.last_translated_at ?? parsed.data.last_crawled_at ?? null
    };
    entries.push(entry);
  }

  const manifest = {
    generatedAt: new Date().toISOString(),
    contentHash: crypto
      .createHash("sha256")
      .update(entries.map((entry) => `${entry.route}:${entry.relativePath}`).join("\n"))
      .digest("hex"),
    count: entries.length,
    sections: [...new Set(entries.map((entry) => entry.section))].sort(),
    documents: entries
  };

  await fs.mkdir(generatedDir, { recursive: true });
  await resetDir(searchSectionsDir);
  const mirroredAssets = await copyMirrorAssets();

  await writeJson(path.join(generatedDir, "content-manifest.json"), manifest);

  const sections = new Map();
  for (const entry of entries) {
    const sectionDocs = sections.get(entry.section) ?? [];
    sectionDocs.push(buildSearchDoc(entry));
    sections.set(entry.section, sectionDocs);
  }

  const searchManifest = {
    generatedAt: manifest.generatedAt,
    totalDocuments: entries.length,
    sections: []
  };

  for (const [section, docs] of [...sections.entries()].sort(([left], [right]) => left.localeCompare(right))) {
    const shardPath = `/__search__/sections/${section}.json`;
    await writeJson(path.join(searchSectionsDir, `${section}.json`), docs);
    searchManifest.sections.push({
      id: section,
      count: docs.length,
      path: shardPath
    });
  }

  await writeJson(path.join(searchDir, "manifest.json"), searchManifest);

  process.stdout.write(
    `Prepared ${entries.length} content documents, ${searchManifest.sections.length} search shards, and ${mirroredAssets} mirrored assets.\n`
  );
}

main().catch((error) => {
  process.stderr.write(`${error instanceof Error ? error.stack ?? error.message : String(error)}\n`);
  process.exitCode = 1;
});
