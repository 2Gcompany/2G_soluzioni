import fs from 'node:fs';
import path from 'node:path';

const TITLE = /<title[^>]*>([\s\S]*?)<\/title>/i;
const DESCRIPTION = /<meta\s+name="description"\s+content="([^"]*)"/i;

// A lesson is any folder under lessonsRoot, at any depth, containing an index.html.
// Lessons come back sorted by title, so the order does not depend on the filesystem.
export function findLessons(lessonsRoot) {
  const lessons = [];

  function visit(folder, relativePath) {
    const indexFile = path.join(folder, 'index.html');
    if (relativePath && fs.existsSync(indexFile)) {
      const html = fs.readFileSync(indexFile, 'utf8');
      const title = TITLE.exec(html)?.[1].trim();
      const description = DESCRIPTION.exec(html)?.[1].trim();
      lessons.push({
        path: relativePath,
        title: title || relativePath,
        description: description || undefined,
      });
    }
    for (const entry of fs.readdirSync(folder, { withFileTypes: true })) {
      if (entry.isDirectory()) {
        visit(path.join(folder, entry.name), relativePath ? `${relativePath}/${entry.name}` : entry.name);
      }
    }
  }

  visit(lessonsRoot, '');
  return lessons.sort((a, b) => a.title.localeCompare(b.title, 'it', { sensitivity: 'base' }) || a.path.localeCompare(b.path));
}
