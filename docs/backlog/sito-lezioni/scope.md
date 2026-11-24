# Sito lezioni (GitHub Pages)

**Status:** scoped 2026-11-24 · **Implementer:** agent alone · **Tracker:** none (github:panicerid/2G_soluzioni available, not published)

## Product in brief
- Students and teachers open one public website that lists every lesson of the class that has a web page (S1).
- Each lesson opens on its own address, exactly as it looks today when the `index.html` is opened locally (S1).
- A new lesson appears on the site by itself: adding a folder with an `index.html` under `lezioni/` and merging to `main` is enough (S1).
- The home page shows a short description for each lesson, in a stable order (S2).
- Every pull request checks that the site still builds, so a broken change is seen before the merge (S2).

## Riskiest assumption
A GitHub Actions workflow can build an Astro container site under the project base path (`/2G_soluzioni/`) and publish it to GitHub Pages, with the existing lessons copied as-is still loading their relative assets (videos of `yugioh`, CDN scripts) from a sub-folder. The walking skeleton goes through it. Prototype: skipped (the skeleton S1 is as cheap as a spike and answers the same question on the real repo).
Reference mock: skipped (the only new screen is a plain list of links; the lessons keep their own design).

## Success signal
After S1 is merged, `https://panicerid.github.io/2G_soluzioni/` lists all 5 HTML lessons and each of the 5 opens and works (yugioh videos play, derivate formulas render). Not met → fix the paths in the copy step before any other slice.

## In scope (this round)
- Astro site in `sito/` that generates the home page with the list of lessons.
- Automatic discovery: every folder under `lezioni/` (any depth) containing an `index.html` is a lesson.
- Lessons copied as static files into the site, keeping their path: `lezioni/matematica/derivate/` → `<site>/lezioni/matematica/derivate/`.
- Development files excluded from the copy: `*.md`, `package.json`, `bun.lock`, `tsconfig.json`, `vite.config.ts`, `Dockerfile`, `compose.yaml`, `metadata.json`.
- Workflow `.github/workflows/pages.yml`: deploy on push to `main` touching `lezioni/**`, `sito/**` or the workflow itself, plus manual run.
- Enabling GitHub Pages with source "GitHub Actions" on the repo.

## Out of scope / non-goals
- Rewriting the lessons as Astro pages – they are self-contained HTML and work as they are (ADR 0001).
- The PDF of `inglese` – not an HTML page; can be linked later.
- Building lessons that need npm/Vite – none needs it today (`csharp-file-stream` ships a self-contained `index.html`).
- Publishing `progetti/` – the request is about lessons.
- Custom domain, search, shared theme across lessons, PR preview deploys – not needed for a class site.
- Analytics, sign-in – the site is public and static.

## Constraints
- Repo is public; Pages free tier: site ≤ 1 GB, file ≤ 100 MB (today: ~21 MB total, largest lesson `yugioh` 20 MB).
- Project page under a sub-path: every link on the home must go through Astro's `base`.
- No build step for the lessons themselves; they rely only on public CDNs.

## Open risks
- Pages must be enabled with source "GitHub Actions" by a repo admin (the user is admin) – handled inside S1.
- A lesson linking an asset with an absolute path (`/assets/...`) would break under the sub-path; none does today – carried into S1 as a manual check.
