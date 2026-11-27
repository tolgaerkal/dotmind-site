#!/usr/bin/env python3
"""Build Studio studies (studies, ideas, playbook) from Markdown.

Writes studies.html, the Studio studies hub that lists everything below.
Reads content/studies/*.md and writes studies/<slug>.html (one page per study).
Reads content/ideas/*.md and writes ideas/<slug>.html (one page per idea post).
Each post or study starts with "# Title" and a "*Author · Month D, YYYY*" byline.

Reads content/playbook.md and writes playbook.html, plus playbook.md (a downloadable copy with
absolute links). Run from the repo root:

    python3 scripts/build_pages.py

Only standard library, and only the Markdown the posts use: headings, paragraphs, lists, tables,
### subheadings, images on their own line, "> " notes, **bold**, *italic* and [links](url).
"""

import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "ideas"
OUT = ROOT / "ideas"
STUDIES_SRC = ROOT / "content" / "studies"
STUDIES_OUT = ROOT / "studies"
SITE = "https://www.dotmind.org/"
# Reference pages shown under "Playbook and tools" on studies.html, with illustrations in ideas/images/heroes/.
TOOLS = [
    ("Agent roles matrix", "roles.html", "heroes/tool-roles.svg",
     "Six agent roles, plus Learn, across every kind of resident interaction. See which role does what, row by row."),
    ("Example journey", "journey.html", "heroes/tool-journey.svg",
     "One interaction in detail: who does what at each step, from a resident’s first question to the decision."),
]
PLAYBOOK_CARD = ("Open playbook", "playbook.html", "heroes/tool-playbook.svg",
                 "Five steps and fill-in templates for choosing and running your first agent. Free to copy and adapt.")
# Slug of the idea post to feature at the top of studies.html. None features the newest.
FEATURED = None

GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WQM5S88M');</script>
<!-- End Google Tag Manager -->"""

DISPLAY = "font-family: Space Grotesk, Inter, sans-serif"
DOTS = '<span aria-hidden="true" style="display: inline-flex; gap: 4px; margin-left: -2px">' + (
    '<span style="display: inline-block; width: 6px; height: 6px; background: #121417"></span>' * 3
) + "</span>"


def header(prefix, hub):
    # Same header as index.html, with Studio studies marked as the current section.
    current = ' aria-current="page"' if hub else ""
    return f"""<header class="no-print" style="border-bottom: 1px solid #E2E0D8; background: #F7F6F2">
<div style="max-width: 1200px; margin: 0 auto; padding: 18px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px">
<a href="{prefix}index.html" style="display: flex; align-items: baseline; gap: 6px; text-decoration: none; color: #121417; {DISPLAY}; font-weight: 600; font-size: 24px; letter-spacing: -0.02em">dotmind{DOTS}</a>
<nav aria-label="Main" style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px 28px; font-size: 16px">
<a href="{prefix}index.html#journey" style="color: #121417; text-decoration: none">How it works</a>
<a href="{prefix}studies.html"{current} style="color: #121417; text-decoration: underline; text-decoration-color: #C2410C; text-decoration-thickness: 2px; text-underline-offset: 6px; font-weight: 600">Studio studies</a>
<a href="{prefix}index.html#about" style="color: #121417; text-decoration: none">About</a>
</nav></div></header>"""


def footer(prefix):
    # The homepage footer, with its links rewritten to work from any page.
    markup = re.search(r"<footer.*?</footer>", (ROOT / "index.html").read_text(encoding="utf-8"), re.S).group(0)
    def fix(m):
        href = m.group(1)
        if href.startswith("#"):
            href = f"index.html{href}"
        if not re.match(r"(https?:|mailto:)", href):
            href = prefix + href
        return f'href="{href}"'
    return re.sub(r'href="([^"]*)"', fix, markup).replace("<footer ", '<footer class="no-print" ', 1)


def page(title, description, prefix, body, width=760, hub=False, head="", cta=""):
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
{head}</head>
<body>
<div style="font-family: Inter, system-ui, -apple-system, Segoe UI, sans-serif; color: #121417; background: #F7F6F2; line-height: 1.5; min-height: 100vh">
{header(prefix, hub)}
<div style="max-width: {width}px; margin: 0 auto; padding: 48px 24px 80px; display: flex; flex-direction: column; gap: 28px">
{body}
<p class="no-print" style="margin: 24px 0 0; padding-top: 24px; border-top: 1px solid #E2E0D8; font-size: 16px; display: flex; flex-wrap: wrap; align-items: center; gap: 12px 20px"><a href="{prefix}index.html#contact" style="display: inline-flex; align-items: center; min-height: 44px; padding: 0 18px; border-radius: 999px; background: #121417; color: #FFFFFF; text-decoration: none; font-weight: 500">Bring us a service</a>{cta}</p>
</div>
{footer(prefix)}
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
        elif line.startswith(">"):
            note = []
            while i < len(lines) and lines[i].startswith(">"):
                note.append(lines[i].lstrip("> ").strip())
                i += 1
            out.append(f'<div role="note" style="padding: 18px 20px; border-left: 4px solid #C2410C; border-radius: 8px; background: #FFF4EC; font-size: 16px">{inline(" ".join(note))}</div>')
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
            while i < len(lines) and lines[i].strip() and not re.match(r"(#{2,3} |\||- |\d+\. |!\[|>)", lines[i]):
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
    paragraphs = [l.strip() for l in body if l.strip() and not re.match(r"(#|!\[|\||- |\d+\. |>)", l)]
    image = next((img.group(2) for l in body if (img := re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", l.strip()))), None)
    words = len(re.findall(r"\w+", " ".join(body)))
    return {
        "slug": re.sub(r"^\d+-", "", path.stem),
        "title": lines[0][2:].strip(),
        "author": m.group(1),
        "date": datetime.strptime(m.group(2), "%B %d, %Y"),
        "date_text": m.group(2),
        "summary": plain(paragraphs[0]),
        "lead": [plain(t) for t in paragraphs[:2]],
        "image": image,
        "minutes": max(1, round(words / 230)),
        "body": body,
    }


def main():
    posts = sorted((load(p) for p in SRC.glob("*.md")), key=lambda p: p["date"], reverse=True)
    studies = sorted((load(p) for p in STUDIES_SRC.glob("*.md")), key=lambda p: p["date"], reverse=True)
    write_articles(posts, OUT, "Ideas")
    write_articles(studies, STUDIES_OUT, "Studio study")
    (ROOT / "studies.html").write_text(studio_index(posts, studies), encoding="utf-8")
    print(f"Built studies.html, {len(studies)} studies in studies/ and {len(posts)} posts in ideas/")
    build_playbook()


def banner(post):
    hero = f'ideas/images/heroes/{post["slug"]}.svg'
    if not (ROOT / hero).exists():
        return ""
    return f'''<img src="../{hero}" alt="" style="display: block; width: 100%; height: auto; aspect-ratio: 16 / 9; max-height: 340px; object-fit: cover; border-radius: 16px">'''


def write_articles(items, out, eyebrow):
    out.mkdir(exist_ok=True)
    for post in items:
        body = f"""<article style="display: flex; flex-direction: column; gap: 18px; font-size: 18px; line-height: 1.65">
<header style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 8px">
<p style="margin: 0; font-size: 15px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: #C2410C">{eyebrow}</p>
<h1 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(32px, 5vw, 48px); letter-spacing: -0.02em; line-height: 1.08">{inline(re.sub(r"^Studio study: ", "", post["title"]))}</h1>
<p style="margin: 0; font-size: 16px; color: #57554F">{html.escape(post["author"])} · <time datetime="{post["date"]:%Y-%m-%d}">{post["date_text"]}</time> · {post["minutes"]} min read</p>
</header>
{banner(post)}
{render(post["body"])}
</article>"""
        (out / f'{post["slug"]}.html').write_text(page(f'{post["title"]} — dotmind', post["summary"], "../", body), encoding="utf-8")


def meta(p):
    return f'''<time datetime="{p["date"]:%Y-%m-%d}">{p["date_text"]}</time> · {p["minutes"]} min read'''


def thumb(p, height):
    # Listing image: the abstract hero in ideas/images/heroes/<slug>.svg if there is one,
    # else the post's first diagram, else a plain brand panel so the grid stays even.
    hero = f'ideas/images/heroes/{p["slug"]}.svg'
    if (ROOT / hero).exists():
        return f'''<img src="{hero}" alt="" style="display: block; width: 100%; height: {height}px; object-fit: cover; border-radius: 12px">'''
    if p["image"]:
        return f'''<img src="ideas/{html.escape(p["image"])}" alt="" style="display: block; width: 100%; height: {height}px; object-fit: contain; background: #FFFFFF; border: 1px solid #E2E0D8; border-radius: 12px; box-sizing: border-box">'''
    return f'''<div aria-hidden="true" style="height: {height}px; border-radius: 12px; background: #FFF4EC; display: flex; align-items: flex-end; padding: 20px; box-sizing: border-box"><span style="display: inline-flex; gap: 6px">{'<span style="width: 10px; height: 10px; background: #C2410C"></span>' * 3}</span></div>'''


def linked(markup, href):
    # Make a card image clickable without adding a second link for keyboard and screen reader users.
    return f'<a href="{href}" tabindex="-1" aria-hidden="true" style="display: block">{markup}</a>'


TAGS = {
    "Study": ("#C2410C", "#FFFFFF"),
    "Idea": ("#FFE4D3", "#8A2E08"),
    "Playbook": ("#121417", "#FFFFFF"),
    "Tool": ("#ECEAE4", "#3F3D38"),
}


def tag(kind):
    background, color = TAGS[kind]
    return f'<span style="display: inline-block; padding: 3px 10px; border-radius: 999px; background: {background}; color: {color}; font-size: 13px; font-weight: 600; letter-spacing: 0.03em; text-transform: uppercase; line-height: 1.5">{kind}</span>'


def tag_line(kind, extra, color="#57554F"):
    return f'<p style="margin: 0; display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; font-size: 15px; color: {color}">{tag(kind)}{extra}</p>'


def section(anchor, title, text, items):
    intro = f'<p style="margin: 0; font-size: 17px; color: #3F3D38">{text}</p>' if text else ""
    return f'''<section id="{anchor}" aria-labelledby="{anchor}-title" style="display: flex; flex-direction: column; gap: 20px">
<div style="display: flex; flex-direction: column; gap: 6px; max-width: 760px"><h2 id="{anchor}-title" style="margin: 0; {DISPLAY}; font-weight: 600; font-size: 26px">{title}</h2>{intro}</div>
<ul style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px">
{items}
</ul>
</section>'''


def studio_index(posts, studies):
    featured = next((p for p in posts if p["slug"] == FEATURED), posts[0])
    rest = [p for p in posts if p is not featured]
    lead = "".join(f'<p style="margin: 0; font-size: 18px; color: #3F3D38">{html.escape(t)}</p>' for t in featured["lead"])
    hero = f'ideas/images/heroes/{featured["slug"]}.svg'
    if (ROOT / hero).exists():
        # Show the whole image, with the panel filled in the image's own background colour.
        bg = re.search(r'<rect width="640" height="360" fill="(#[0-9A-Fa-f]{6})"', (ROOT / hero).read_text()).group(1)
        picture = f'<div style="display: flex; align-items: center; height: 100%; background: {bg}; min-height: 260px"><img src="{hero}" alt="" style="display: block; width: 100%; height: auto"></div>'
    else:
        picture = f'<div style="padding: 32px 0 0 32px">{thumb(featured, 320)}</div>'
    feature = f'''<article style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); background: #FFFFFF; border: 1px solid #E2E0D8; border-radius: 20px; overflow: hidden">
{linked(picture, f"ideas/{featured['slug']}.html")}
<div style="display: flex; flex-direction: column; justify-content: center; gap: 14px; padding: 36px">
{tag_line("Idea", f'<span style="font-weight: 600; color: #C2410C">Featured</span><span>{meta(featured)}</span>')}
<h2 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(28px, 3.5vw, 40px); letter-spacing: -0.02em; line-height: 1.1"><a href="ideas/{featured["slug"]}.html" style="color: #121417; text-decoration: none">{inline(featured["title"])}</a></h2>
{lead}
<a href="ideas/{featured["slug"]}.html" style="align-self: flex-start; display: inline-flex; align-items: center; min-height: 48px; padding: 0 22px; border-radius: 999px; background: #121417; color: #FFFFFF; text-decoration: none; font-weight: 600">Read the post<span style="position: absolute; left: -10000px">: {html.escape(featured["title"])}</span></a>
</div>
</article>'''
    study_cards = "\n".join(
        f'''<li style="display: flex; flex-direction: column; gap: 14px; background: #FFFFFF; border: 1px solid #E2E0D8; border-radius: 20px; padding: 20px">
{linked(thumb(p, 200), f"studies/{p['slug']}.html")}
{tag_line("Study", f"<span>{meta(p)}</span>")}
<h3 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: 24px; line-height: 1.2"><a href="studies/{p["slug"]}.html" style="color: #121417; text-decoration: none">{inline(re.sub(r"^Studio study: ", "", p["title"]))}</a></h3>
<p style="margin: 0; font-size: 16px; color: #3F3D38; flex: 1">{html.escape(p["summary"])}</p>
<a href="studies/{p["slug"]}.html" style="font-size: 16px; font-weight: 500">Read the study<span style="position: absolute; left: -10000px">: {html.escape(p["title"])}</span></a>
</li>'''
        for p in studies
    )
    idea_cards = "\n".join(
        f'''<li style="display: flex; flex-direction: column; gap: 14px; background: #FFFFFF; border: 1px solid #E2E0D8; border-radius: 20px; padding: 20px">
{linked(thumb(p, 180), f"ideas/{p['slug']}.html")}
{tag_line("Idea", f"<span>{meta(p)}</span>")}
<h3 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: 22px; line-height: 1.2"><a href="ideas/{p["slug"]}.html" style="color: #121417; text-decoration: none">{inline(p["title"])}</a></h3>
<p style="margin: 0; font-size: 16px; color: #3F3D38; flex: 1">{html.escape(p["summary"])}</p>
<a href="ideas/{p["slug"]}.html" style="font-size: 16px; font-weight: 500">Read<span style="position: absolute; left: -10000px"> {html.escape(p["title"])}</span></a>
</li>'''
        for p in rest
    )
    tool_cards = f'''<li style="display: flex; flex-direction: column; gap: 14px; background: #FFFFFF; border: 1px solid #E2E0D8; border-radius: 20px; padding: 20px">
<a href="{PLAYBOOK_CARD[1]}" tabindex="-1" aria-hidden="true" style="display: block"><img src="ideas/images/{PLAYBOOK_CARD[2]}" alt="" style="display: block; width: 100%; height: 180px; object-fit: cover; border: 1px solid #E2E0D8; border-radius: 12px; box-sizing: border-box"></a>
{tag_line("Playbook", "<span>Do it yourself</span>")}
<h3 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: 22px; line-height: 1.2"><a href="{PLAYBOOK_CARD[1]}" style="color: #121417; text-decoration: none">{PLAYBOOK_CARD[0]}</a></h3>
<p style="margin: 0; font-size: 16px; color: #3F3D38; flex: 1">{PLAYBOOK_CARD[3]}</p>
<a href="{PLAYBOOK_CARD[1]}" style="font-size: 16px; font-weight: 500">Open the playbook</a>
</li>''' + "\n".join(
        f'''<li style="display: flex; flex-direction: column; gap: 14px; background: #FFFFFF; border: 1px solid #E2E0D8; border-radius: 20px; padding: 20px">
<a href="{href}" tabindex="-1" aria-hidden="true" style="display: block"><img src="ideas/images/{image}" alt="" style="display: block; width: 100%; height: 180px; object-fit: cover; border: 1px solid #E2E0D8; border-radius: 12px; box-sizing: border-box"></a>
{tag_line("Tool", "")}
<h3 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: 22px; line-height: 1.2"><a href="{href}" style="color: #121417; text-decoration: none">{title}</a></h3>
<p style="margin: 0; font-size: 16px; color: #3F3D38; flex: 1">{html.escape(text)}</p>
<a href="{href}" style="font-size: 16px; font-weight: 500">Open<span style="position: absolute; left: -10000px"> the {title.lower()}</span></a>
</li>'''
        for title, href, image, text in TOOLS
    )
    intro = "What we’re learning about AI agents in public services, shared openly: studies of real services, ideas on doing it well, and a playbook and tools your agency can use."
    body = f'''<header style="display: flex; flex-direction: column; gap: 10px; max-width: 760px">
<h1 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(36px, 5vw, 56px); letter-spacing: -0.02em; line-height: 1.05">Studio studies</h1>
<p style="margin: 0; font-size: 19px; color: #3F3D38">{intro}</p>
</header>
{feature}
{section("studies", "Studies", "How our agent roles could work on real public services. Built only from what agencies publish; not commissioned projects, and not reviewed or endorsed by the agencies.", study_cards)}
{section("ideas", "Ideas", "", idea_cards)}
{section("tools", "Playbook and tools", "Free to use, adapt and share inside your agency.", tool_cards)}'''
    return page("Studio studies — dotmind", intro, "", body, width=1100, hub=True)


PLAYBOOK_URL = f"{SITE}playbook.html"
PLAYBOOK_IMAGE = f"{SITE}ideas/images/og-playbook.png"
PLAYBOOK_PRINT = """<style>
.print-only{display:none}
@media print{
  @page{margin:18mm}
  .print-only{display:block}
  .cover{min-height:85vh;display:flex;flex-direction:column;justify-content:center;gap:14px;break-after:page}
  main{font-size:12pt!important;line-height:1.5!important}
  h2,h3{break-after:avoid}
  table,tr,figure{break-inside:avoid}
  main a[href]::after{content:" (" attr(href) ")";font-size:0.85em;color:#57554F;word-break:break-all}
  main a[href$=".html"]:not([href^="http"])::after,main a[href*=".html#"]:not([href^="http"])::after{content:" (dotmind.org/" attr(href) ")"}
  main a[href^="#"]::after,main a[href^="mailto:"]::after{content:""}
}
</style>
"""


def build_playbook():
    source = (ROOT / "content" / "playbook.md").read_text(encoding="utf-8")
    lines = source.splitlines()
    assert lines[0].startswith("# "), "playbook.md: first line must be '# Title'"
    title = lines[0][2:].strip()
    rest = lines[1:]
    # An italic line straight after the title is the version line: "*v1.0 · Month YYYY · by ...*"
    first = next(i for i, l in enumerate(rest) if l.strip())
    version = ""
    if re.fullmatch(r"\*v[\d.]+ ·.+\*", rest[first].strip()):
        version = rest[first].strip().strip("*")
        rest = rest[first + 1:]
    summary = plain(next(l for l in rest if l.strip()))
    download = (
        '<p class="no-print" style="margin: 0; display: flex; flex-wrap: wrap; gap: 10px 20px; font-size: 16px">'
        '<a href="playbook.md" download>Download as Markdown</a>'
        '<a href="playbook-worksheet.csv" download>Download the scoring worksheet (CSV)</a>'
        '<button type="button" onclick="window.print()" style="padding: 0; border: 0; background: none; font: inherit; color: #C2410C; text-decoration: underline; cursor: pointer">Print or save as PDF</button></p>'
    )
    cover = f"""<div class="print-only cover">
<p style="margin: 0; font-size: 12pt; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase">dotmind · Open playbook</p>
<h1 style="margin: 0; {DISPLAY}; font-size: 30pt; line-height: 1.1">{inline(title)}</h1>
<p style="margin: 0; font-size: 13pt">{html.escape(plain(version))}</p>
<p style="margin: 0; font-size: 11pt">{PLAYBOOK_URL.replace("https://", "")} · Free to use under CC BY 4.0</p>
</div>"""
    byline = f'<p style="margin: 0; font-size: 16px; color: #57554F">{inline(version)}</p>' if version else ""
    body = f"""<main style="display: flex; flex-direction: column; gap: 18px; font-size: 18px; line-height: 1.65">
{cover}
<header class="no-print" style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 8px">
<p style="margin: 0; font-size: 15px; font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; color: #C2410C">Open playbook</p>
<h1 style="margin: 0; {DISPLAY}; font-weight: 600; font-size: clamp(32px, 5vw, 48px); letter-spacing: -0.02em; line-height: 1.08">{inline(title)}</h1>
{byline}
</header>
{download}
{render(rest)}
</main>"""
    og = f"""<meta property="og:type" content="article">
<meta property="og:site_name" content="dotmind">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(summary)}">
<meta property="og:url" content="{PLAYBOOK_URL}">
<meta property="og:image" content="{PLAYBOOK_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{PLAYBOOK_URL}">
"""
    walkthrough = ('<span style="color: #3F3D38">Want a walkthrough of the playbook for your team? We run a free 45-minute session. '
                   '<a href="mailto:hello@dotmind.org?subject=Playbook%20walkthrough">Book a walkthrough</a></span>')
    (ROOT / "playbook.html").write_text(
        page(f"{title} — dotmind", summary, "", body, width=960, head=og + PLAYBOOK_PRINT, cta=walkthrough), encoding="utf-8")
    # The downloadable copy travels on its own, so point its links at the live site.
    absolute = re.sub(r"\]\((?!https?:|#|mailto:)([^)]+)\)", lambda m: f"]({SITE}{m.group(1)})", source)
    (ROOT / "playbook.md").write_text(absolute, encoding="utf-8")
    print("Built playbook.html and playbook.md")


if __name__ == "__main__":
    main()
