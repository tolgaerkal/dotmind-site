# dotmind.org

Website for **dotmind**, the AI Service Studio for state government.

> Better public services, designed with people and built with agents.

## Pages

- `index.html` — homepage
- `roles.html` — agent roles matrix (six interaction types × six agent roles)
- `journey.html` — example journey: applying for a service
- `studies.html` — Studio studies hub: studies, ideas, the playbook and tools
- `ideas/` — idea posts (the old `ideas.html` redirects to `studies.html`)
- `studies/` — studies: how our roles could work on real services (from `content/studies/`)
- `playbook.html` — open playbook (CC BY 4.0) for agencies, with `playbook.md` and `playbook-worksheet.csv` downloads
- `privacy.html`, `accessibility.html` — privacy notice and accessibility statement

Plain static HTML with inline styles. No build step on deploy. Fonts load from Google Fonts.

## Run locally

Open `index.html` in a browser, or serve the folder:

```
python3 -m http.server 8000
```

## Publish with GitHub Pages

1. Push this folder to a new GitHub repository.
2. In the repository, go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
4. The `CNAME` file sets the custom domain to `dotmind.org`. Point your domain's DNS at GitHub Pages
   (see GitHub's docs on configuring a custom domain), then tick **Enforce HTTPS** once it's available.

## Contact

The contact section links to `hello@dotmind.org` with a pre-filled subject and prompts. There is no form or backend.
Clicks on any email link push a `contact_email_click` event to Google Tag Manager.

## Studio studies (studies, ideas and the playbook)

The playbook is written in `content/playbook.md`; the same script builds `playbook.html` and a downloadable `playbook.md`.

Posts are written in Markdown in `content/ideas/`, then turned into `ideas/*.html` (and listed on `studies.html`) by a small script.
Commit the generated HTML; Vercel serves it as-is.

1. Add a file like `content/ideas/06-my-post.md`. Start it with `# Title`, then a byline line
   `*Your Name · November 26, 2026*`. Put diagrams in `ideas/images/` and reference them as `images/name.svg`.
2. Run `python3 scripts/build_pages.py`.
3. Commit and push.

Each listing card shows an abstract hero image from `ideas/images/heroes/<slug>.svg` (the slug is the file name without its number). Without one, it falls back to the post's first diagram, then a plain panel.

Every page except the homepage gets the homepage footer: generated pages copy it from `index.html` at build time; `roles.html`, `journey.html`, `privacy.html` and `accessibility.html` hold their own copy, so update those by hand if the footer changes.

Studio studies work the same way: add a Markdown file to `content/studies/` and rebuild. A line starting with `> ` becomes a highlighted note.

Posts are listed newest first by their byline date. The newest is featured at the top of `studies.html`; to pin a different one, set `FEATURED` in `scripts/build_pages.py` to its slug. The page URL is the filename without the number prefix.

Files in `content/ideas/drafts/` are not published. To publish one, move it up to `content/ideas/`
(and any diagram it uses into `ideas/images/`), then rebuild.
