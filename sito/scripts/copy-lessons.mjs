import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { findLessons } from '../lib/lessons.mjs';

const lessonsRoot = fileURLToPath(new URL('../../lezioni', import.meta.url));
const target = fileURLToPath(new URL('../public/lezioni', import.meta.url));

// Development files of a lesson, not part of what the class opens.
const EXCLUDED = new Set([
  'package.json',
  'bun.lock',
  'tsconfig.json',
  'vite.config.ts',
  'Dockerfile',
  'compose.yaml',
  'metadata.json',
]);

const isExcluded = (file) => EXCLUDED.has(path.basename(file)) || file.endsWith('.md');

fs.rmSync(target, { recursive: true, force: true });
for (const { path: lessonPath } of findLessons(lessonsRoot)) {
  fs.cpSync(path.join(lessonsRoot, lessonPath), path.join(target, lessonPath), {
    recursive: true,
    filter: (source) => !isExcluded(source),
  });
}
