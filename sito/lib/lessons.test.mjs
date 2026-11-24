import { test } from 'node:test';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { findLessons } from './lessons.mjs';

const fixtures = fileURLToPath(new URL('../test/fixtures/lezioni', import.meta.url));

test('finds a lesson with its title, trimmed', () => {
  const lessons = findLessons(fixtures);
  assert.deepEqual(lessons.find((l) => l.path === 'alfa'), {
    path: 'alfa',
    title: 'Lezione Alfa',
    description: 'Prima lezione di prova',
  });
});

test('finds a lesson nested at any depth, with a POSIX path', () => {
  const lessons = findLessons(fixtures);
  assert.deepEqual(lessons.find((l) => l.path === 'annidata/profonda/lezione'), {
    path: 'annidata/profonda/lezione',
    title: 'Lezione Annidata',
    description: undefined,
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
    description: undefined,
  });
});

test('lists exactly the lessons of the fixture tree', () => {
  const paths = findLessons(fixtures).map((l) => l.path).sort();
  assert.deepEqual(paths, ['alfa', 'annidata/profonda/lezione', 'senza-titolo', 'zeta']);
});

test('sorts lessons by title, case-insensitive in Italian, whatever the folder order', () => {
  const paths = findLessons(fixtures).map((l) => l.path);
  assert.deepEqual(paths, ['zeta', 'alfa', 'annidata/profonda/lezione', 'senza-titolo']);
});

test('lessons with the same title are ordered by path', () => {
  const sameTitle = fileURLToPath(new URL('../test/fixtures/stesso-titolo', import.meta.url));
  const paths = findLessons(sameTitle).map((l) => l.path);
  assert.deepEqual(paths, ['a-b', 'a/x']);
});
