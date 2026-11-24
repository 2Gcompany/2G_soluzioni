# Code conventions

The shared shape of the code: patterns more than one slice uses. Read before writing code (implement) and used as the yardstick (kets-review). One rule per pattern; a rule changes only with the user's ok.

- **Lesson discovery**: the only code that decides what a lesson is (a folder under `lezioni/` with an `index.html`), its path, title and description is `findLessons()`; the copy script and the home page import it and never scan `lezioni/` themselves. Lives in `sito/lib/lessons.mjs`. Since sito-lezioni S1.
- **Site links**: every link on a page of `sito/` is built from `import.meta.env.BASE_URL`, never hard-coded with `/2G_soluzioni/` or a leading `/`. Lives in `sito/src/pages/`. Since sito-lezioni S1.
- **Lesson files untouched**: the site never edits lesson files; it only copies them. Lives in `sito/scripts/copy-lessons.mjs`. Since sito-lezioni S1.
