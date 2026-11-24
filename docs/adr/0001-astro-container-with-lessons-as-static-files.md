# Astro container site, lessons published as static copies

The site is an Astro project in `sito/` that generates only the home page; each lesson's folder is copied as-is into the build output instead of being ported to Astro pages. Lessons are self-contained HTML written by different students with their own styles and scripts, and porting them would cost a rewrite per lesson and break the "open `index.html` locally" workflow the class uses.

## Considered options
- Plain workflow that generates the index with a script, no framework – simpler, rejected because the user wants an Astro site to grow on.
- Lessons as Astro pages – rejected, see above.

## Consequences
- A lesson that needs a build step (npm/Vite) is not supported until a slice adds it.
- Lesson assets must use relative paths, because the site lives under `/2G_soluzioni/`.
