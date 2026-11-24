import { test } from 'node:test';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { findLessons } from './lessons.mjs';

const fixtures = fileURLToPath(new URL('../test/fixtures/lezioni', import.meta.url));

test('finds a lesson with its title, trimmed', () => {
  const lessons = findLessons(fixtures);
  assert.deepEqual(lessons.find((l) => l.path === 'alfa'), { path: 'alfa', title: 'Lezione Alfa' });
});

test('finds a lesson nested at any depth, with a POSIX path', () => {
  const lessons = findLessons(fixtures);
  assert.deepEqual(lessons.find((l) => l.path === 'annidata/profonda/lezione'), {
    path: 'annidata/profonda/lezione',
    title: 'Lezione Annidata',
  });
});

test('ignores a folder with only a PDF', () => {
  const paths = findLessons(fixtures).map((l) => l.path);
  assert.ok(!paths.includes('solo-pdf'));
});

test('falls back to the folder path when index.html has no title', () => {
  const lessons = findLessons(fixtures);
  assert.deepEqual(lessons.find((l) => l.path === 'senza-titolo'), {
    path: 'senza-titolo',
    title: 'senza-titolo',
  });
});

test('lists exactly the lessons of the fixture tree', () => {
  const paths = findLessons(fixtures).map((l) => l.path).sort();
  assert.deepEqual(paths, ['alfa', 'annidata/profonda/lezione', 'senza-titolo']);
});
