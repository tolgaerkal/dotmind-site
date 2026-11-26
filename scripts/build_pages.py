#!/usr/bin/env python3
"""Build the Ideas section and the open playbook from Markdown.

Reads content/ideas/*.md and writes ideas.html (the list) and ideas/<slug>.html (one page per post).
Each post starts with "# Title" and a "*Author · Month D, YYYY*" byline.

Reads content/playbook.md and writes playbook.html, plus playbook.md (a downloadable copy with
absolute links). Run from the repo root:

    python3 scripts/build_pages.py

Only standard library, and only the Markdown the posts use: headings, paragraphs, lists, tables,
### subheadings, images on their own line, **bold**, *italic* and [links](url).
"""

import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "ideas"
OUT = ROOT / "ideas"
SITE = "https://www.dotmind.org/"

GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WQM5S88M');</script>
<!-- End Google Tag Manager -->"""

GTM_BODY = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WQM5S88M"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

DISPLAY = "font-family: Space Grotesk, Inter, sans-serif"
DOTS = '<span aria-hidden="true" style="display: inline-flex; gap: 4px; margin-left: -2px">' + (
    '<span style="display: inline-block; width: 6px; height: 6px; background: #C2410C"></span>' * 3
) + "</span>"


def page(title, description, prefix, body, nav=("ideas.html", "All ideas"), width=760):
    return f"""<!doctype html>
<html lang="en">
<head>
{GTM_HEAD}
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Space+Grotesk:wght@500;600&amp;display=swap">
<style>body{{margin:0}}a{{color:#C2410C}}a:hover{{color:#9A3412}}@media print{{.no-print{{display:none!important}}body *{{background:none!important}}table{{min-width:0!important;font-size:12px!important}}}}</style>
</head>
<body>
{GTM_BODY}
<div style="font-family: Inter, system-ui, -apple-system, Segoe UI, sans-serif; color: #121417; background: #F7F6F2; line-height: 1.5; min-height: 100vh">
<div style="max-width: {width}px; margin: 0 auto; padding: 56px 24px 80px; display: flex; flex-direction: column; gap: 28px">
<nav aria-label="Site" class="no-print" style="display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 12px">
<a href="{prefix}index.html" style="display: flex; align-items: baseline; gap: 6px; {DISPLAY}; font-weight: 600; font-size: 22px; color: #121417; text-decoration: none">dotmind{DOTS}</a>
<a href="{prefix}{nav[0]}" style="font-size: 16px">{nav[1]}</a>
</nav>
{body}
<p class="no-print" style="margin: 24px 0 0; padding-top: 24px; border-top: 1px solid #E2E0D8; font-size: 16px"><a href="{prefix}index.html#contact" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 18px; border-radius: 999px; background: #121417; color: #FFFFFF; text-decoration: none; font-weight: 500">Bring us a service</a></p>
</div>
</div>
</body>
</html>
"""


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: f'<a href="{link(m.group(2))}">{m.group(1)}</a>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)


def link(url):
    # Keep the call to action on whichever domain is serving the site.
    if url.startswith("https://dotmind.org/"):
        url = "../index.html" + url[len("https://dotmind.org/"):]
    return html.escape(url)


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def render(lines):
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("## "):
            out.append(f'<h2 style="margin: 28px 0 0; {DISPLAY}; font-weight: 600; font-size: 26px; letter-spacing: -0.01em; line-height: 1.2">{inline(line[3:])}</h2>')
            i += 1
        elif line.startswith("### "):
            out.append(f'<h3 style="margin: 12px 0 0; {DISPLAY}; font-weight: 600; font-size: 20px; line-height: 1.25">{inline(line[4:])}</h3>')
            i += 1
        elif m := re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", line.strip()):
            alt = html.escape(m.group(1))
            out.append(f'<figure style="margin: 8px 0"><img src="{html.escape(m.group(2))}" alt="{alt}" style="display: block; width: 100%; height: auto; border: 1px solid #E2E0D8; border-radius: 12px; background: #FFFFFF"></figure>')
            i += 1
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(cells(lines[i]))
                i += 1
            head, body = rows[0], [r for r in rows[1:] if not all(c and set(c) <= set("-: ") for c in r)]
            th = "".join(f'<th scope="col" style="text-align: left; padding: 10px 12px; background: #ECEAE4; font-weight: 600">{inline(c)}</th>' for c in head)
            trs = "".join(
                "<tr>" + "".join(f'<td style="padding: 10px 12px; height: 24px; border-top: 1px solid #E2E0D8; vertical-align: top">{inline(c) or "&nbsp;"}</td>' for c in r) + "</tr>"
                for r in body
            )
            out.append(f'<div style="overflow-x: auto"><table style="width: 100%; min-width: 520px; border-collapse: collapse; font-size: 16px; background: #FFFFFF; border: 1px solid #E2E0D8"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
        elif re.match(r"(- |\d+\. )", line):
            tag = "ul" if line.startswith("- ") else "ol"
            items = []
            while i < len(lines) and re.match(r"(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            lis = "".join(f'<li style="margin: 0 0 10px">{inline(t)}</li>' for t in items)
            out.append(f'<{tag} style="margin: 0; padding-left: 24px">{lis}</{tag}>')
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"(#{2,3} |\||- |\d+\. |!\[)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f'<p style="margin: 0">{inline(" ".join(para))}</p>')
    return "\n".join(out)


def plain(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.replace("**", "").replace("*", "")


def load(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0].startswith("# "), f"{path.name}: first line must be '# Title'"
    byline = next(l for l in lines[1:] if l.strip())
    m = re.fullmatch(r"\*(.+) · (\w+ \d{1,2}, \d{4})\*", byline.strip())
    assert m, f"{path.name}: second line must be '*Author · Month D, YYYY*'"
    body = lines[lines.index(byline) + 1:]
    summary = next(l for l in body if l.strip() and not l.startswith(("#", "!", "|", "-")))
    return {
        "slug": re.sub(r"^\d+-", "", path.stem),
        "title": lines[0][2:].strip(),
        "author": m.group(1),
        "date": datetime.strptime(m.group(2), "%B %d, %Y"),
        "date_text": m.group(2),
        "summary": plain(summary.strip()),
        "body": body,
    }


def main():
    posts = sorted((load(p) for p in SRC.glob("*.md")), key=lambda p: p["date"], reverse=True)
    OUT.mkdir(exist_ok=True)
    for post in posts:
        body = f"""<article style="display: flex; flex-direction: column; gap: 18px; font-size: 18px; line-height: 1.65">
<header style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 8px">
<p style="margin: 0; font-size: 15px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: #C2410C">Ideas</p>
<h1 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(32px, 5vw, 48px); letter-spacing: -0.02em; line-height: 1.08">{inline(post["title"])}</h1>
<p style="margin: 0; font-size: 16px; color: #57554F">{html.escape(post["author"])} · <time datetime="{post["date"]:%Y-%m-%d}">{post["date_text"]}</time></p>
</header>
{render(post["body"])}
</article>"""
        (OUT / f'{post["slug"]}.html').write_text(page(f'{post["title"]} — dotmind', post["summary"], "../", body), encoding="utf-8")

    cards = "\n".join(
        f"""<li style="padding: 24px 0; border-top: 1px solid #E2E0D8; display: flex; flex-direction: column; gap: 8px">
<time datetime="{p["date"]:%Y-%m-%d}" style="font-size: 15px; color: #57554F">{p["date_text"]}</time>
<h2 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: 24px; line-height: 1.2"><a href="ideas/{p["slug"]}.html" style="color: #121417; text-decoration: none">{inline(p["title"])}</a></h2>
<p style="margin: 0; font-size: 17px; color: #3F3D38">{html.escape(p["summary"])}</p>
<a href="ideas/{p["slug"]}.html" style="font-size: 16px; font-weight: 500">Read more<span style="position: absolute; left: -10000px"> about {html.escape(p["title"])}</span></a>
</li>"""
        for p in posts
    )
    intro = "How we think about AI agents in public services: where to start, how to keep them fair and safe, and how states stay in control."
    body = f"""<header style="display: flex; flex-direction: column; gap: 10px">
<h1 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(36px, 5vw, 56px); letter-spacing: -0.02em; line-height: 1.05">Ideas</h1>
<p style="margin: 0; font-size: 19px; color: #3F3D38">{intro}</p>
</header>
<ul style="list-style: none; margin: 0; padding: 0">
{cards}
</ul>"""
    (ROOT / "ideas.html").write_text(page("dotmind — Ideas", intro, "", body), encoding="utf-8")
    print(f"Built ideas.html and {len(posts)} posts in ideas/")
    build_playbook()


def build_playbook():
    source = (ROOT / "content" / "playbook.md").read_text(encoding="utf-8")
    lines = source.splitlines()
    assert lines[0].startswith("# "), "playbook.md: first line must be '# Title'"
    title = lines[0][2:].strip()
    summary = plain(next(l for l in lines[1:] if l.strip()))
    download = (
        '<p class="no-print" style="margin: 0; display: flex; flex-wrap: wrap; gap: 10px 20px; font-size: 16px">'
        '<a href="playbook.md" download>Download as Markdown</a>'
        '<a href="playbook-worksheet.csv" download>Download the scoring worksheet (CSV)</a>'
        '<button type="button" onclick="window.print()" style="padding: 0; border: 0; background: none; font: inherit; color: #C2410C; text-decoration: underline; cursor: pointer">Print or save as PDF</button></p>'
    )
    body = f"""<main style="display: flex; flex-direction: column; gap: 18px; font-size: 18px; line-height: 1.65">
<header style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 8px">
<p style="margin: 0; font-size: 15px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: #C2410C">Open playbook</p>
<h1 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(32px, 5vw, 48px); letter-spacing: -0.02em; line-height: 1.08">{inline(title)}</h1>
</header>
{download}
{render(lines[1:])}
</main>"""
    (ROOT / "playbook.html").write_text(page(f"{title} — dotmind", summary, "", body, nav=("ideas.html", "Ideas"), width=960), encoding="utf-8")
    # The downloadable copy travels on its own, so point its links at the live site.
    absolute = re.sub(r"\]\((?!https?:|#|mailto:)([^)]+)\)", lambda m: f"]({SITE}{m.group(1)})", source)
    (ROOT / "playbook.md").write_text(absolute, encoding="utf-8")
    print("Built playbook.html and playbook.md")


if __name__ == "__main__":
    main()
