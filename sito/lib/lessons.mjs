import fs from 'node:fs';
import path from 'node:path';

const TITLE = /<title[^>]*>([\s\S]*?)<\/title>/i;

// A lesson is any folder under lessonsRoot, at any depth, containing an index.html.
export function findLessons(lessonsRoot) {
  const lessons = [];

  function visit(folder, relativePath) {
    const indexFile = path.join(folder, 'index.html');
    if (relativePath && fs.existsSync(indexFile)) {
      const title = TITLE.exec(fs.readFileSync(indexFile, 'utf8'))?.[1].trim();
      lessons.push({ path: relativePath, title: title || relativePath });
    }
    for (const entry of fs.readdirSync(folder, { withFileTypes: true })) {
      if (entry.isDirectory()) {
        visit(path.join(folder, entry.name), relativePath ? `${relativePath}/${entry.name}` : entry.name);
      }
    }
  }

  visit(lessonsRoot, '');
  return lessons;
}
