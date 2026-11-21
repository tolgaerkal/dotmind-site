# dotmind.org

Website for **dotmind**, the AI Service Studio for state government.

> Better public services, designed with people and built with agents.

## Pages

- `index.html` — homepage
- `roles.html` — agent roles matrix (six interaction types × six agent roles)
- `journey.html` — example journey: applying for a service

Plain static HTML with inline styles. No build step. Fonts load from Google Fonts.

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

## Before launch

- Replace `[RESPONSE TIME]` in the contact section.
- Replace the funding answer placeholder in the FAQ.
- Connect the contact form to a form service or backend; it is currently design-only.
