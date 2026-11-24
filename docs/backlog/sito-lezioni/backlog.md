# Backlog – Sito lezioni (GitHub Pages)

Scope: ./scope.md · Implementer: agent alone · Tracker: none

Order is dependency order. A slice with no "Blocked by" can start in parallel.

---

## S1 · Anyone opens the class website and reaches every HTML lesson
**In brief:** A public website on GitHub Pages lists the class lessons by title; clicking one opens the lesson as it is today. It is rebuilt and republished automatically every time something changes on `main`.
**Why:** proves the riskiest assumption end-to-end: Astro build under the sub-path, lessons copied with their assets, deploy through an Action.
**Size:** M · **Status:** done
**Blocked by:** –
**ADRs:** 0001

### Acceptance criteria
- Given the repo with its 5 lessons that have an `index.html`, when the site is built, then the home lists 5 entries, each with the text of that lesson's `<title>`, and each links to `<base>/lezioni/<lesson path>/`.
- Given the built site, when listing the output folder, then `lezioni/yugioh/assets/video/exodia.mp4` and `lezioni/matematica/derivate/index.html` exist, and no `README.md`, `package.json`, `bun.lock`, `tsconfig.json`, `vite.config.ts`, `Dockerfile`, `compose.yaml` or `metadata.json` exists under `lezioni/`.
- Given `lezioni/inglese/` contains only a PDF, when the site is built, then it is not listed on the home and not copied.
- Given a lesson folder whose `index.html` has no `<title>`, when the site is built, then the entry shows the folder path (e.g. `matematica/derivate`) instead.
- Given a push to `main` that changes a file under `lezioni/`, when the workflow finishes, then `https://panicerid.github.io/2G_soluzioni/` serves the new build (check: workflow run green, page reachable).

### Seams
- `findLessons(lessonsRoot)` in `sito/lib/lessons.mjs`, run against a fixture folder – covers AC1 (titles, paths), AC3, AC4. Catches discovery and title extraction; misses the copy and the deploy.
- `npm run build` in `sito/`, then inspect `sito/dist/` – covers AC1 (links with base), AC2. Catches filtering and base path; misses Pages itself.
- The deployed URL, opened by hand – covers AC5 and the open risk on absolute paths. Catches Pages config; not automatable here.

### Implementation notes
- Build: lesson discovery as the shared one in `sito/lib/lessons.mjs` (see `docs/conventions.md`); both the copy script and the home page import it.
- Touch: new `sito/` (Astro project: `package.json`, `astro.config.mjs` with `site: 'https://panicerid.github.io'` and `base: '/2G_soluzioni'`, `src/pages/index.astro`, `lib/lessons.mjs`, `scripts/copy-lessons.mjs`, `.gitignore` with `dist/`, `node_modules/`, `public/lezioni/`), new `.github/workflows/pages.yml`, `README.md` (one line under "Strumenti" with the site link and how to run `sito/` locally).
- Do not touch: anything under `lezioni/` or `progetti/`.
- Copy: `scripts/copy-lessons.mjs` copies each lesson folder into `sito/public/lezioni/<path>/` skipping the excluded files; wire it as `prebuild` and `predev` in `sito/package.json`. Use only Node standard library (`fs.cp` with a filter), no extra dependency.
- Title extraction: a regex on `<title>…</title>` is enough; no HTML parser dependency.
- Workflow: `on: push` to `main` with `paths: [lezioni/**, sito/**, .github/workflows/pages.yml]` plus `workflow_dispatch`; permissions `contents: read, pages: write, id-token: write`; concurrency group `pages`; build with `withastro/action` (`path: sito`) then `actions/deploy-pages`. Use current major versions of each action.
- Enable Pages once: `gh api -X POST repos/panicerid/2G_soluzioni/pages -f build_type=workflow` (if it already exists, `-X PUT`). Say it in the PR description.
- Tests to add: `sito/lib/lessons.test.mjs` with `node --test` and a fixture tree (`sito/test/fixtures/lezioni/…`): finds nested lessons, ignores a folder with only a PDF, falls back to the folder path without `<title>`. Add `"test": "node --test"` to `sito/package.json`.
- Done when: `npm test` and `npm run build` pass in `sito/`, and after merge the 5 lessons open from the live home (yugioh video plays, derivate formulas render).

---

## S2 · Home shows what each lesson is about, and PRs check the build
**In brief:** On the home page each lesson shows a one-line description next to its title, always in alphabetical order. Every pull request also builds the site, so a change that breaks it is caught before the merge, without publishing anything.
**Why:** makes the home useful to a student choosing a lesson, and protects `main` from a broken deploy.
**Size:** S · **Status:** done
**Blocked by:** S1

### Acceptance criteria
- Given a lesson whose `index.html` has `<meta name="description" content="…">`, when the site is built, then its home entry shows that text under the title.
- Given a lesson without a description meta tag, when the site is built, then its entry shows only the title and no empty line.
- Given any set of lessons, when the site is built twice, then the entries are in the same order, sorted by title (case-insensitive, Italian locale).
- Given a pull request to `main` touching `lezioni/**` or `sito/**`, when the workflow runs, then it runs `npm test` and the build and does not deploy.

### Seams
- `findLessons(lessonsRoot)` against the fixture tree – covers AC1, AC2 (description field present or absent), AC3. Catches extraction and sorting; misses the markup.
- `npm run build`, then inspect `sito/dist/index.html` – covers AC2 (no empty element). Catches rendering.
- A test PR – covers AC4.

### Implementation notes
- Reuse: lesson discovery (`sito/lib/lessons.mjs`) – add `description` to the returned object and do the sorting there, not in the page.
- Touch: `sito/lib/lessons.mjs`, `sito/lib/lessons.test.mjs`, fixtures, `sito/src/pages/index.astro`, `.github/workflows/pages.yml` (add `pull_request` trigger; the deploy job runs only `if: github.event_name != 'pull_request'`; run `npm test` before the build).
- Tests to add: description extracted; missing description gives `undefined`; order sorted by title with `localeCompare(…, 'it', { sensitivity: 'base' })`.
- Done when: tests pass, build passes, a test PR shows the build job green and no deploy job run.

---

## Later (cut from this round)
- Link to the `inglese` PDF from the home.
- Shared look (header with a "back to home" link) injected into the lessons.
- Publishing `progetti/` prototypes on the same site.
- Lessons that need an npm build before publishing.
