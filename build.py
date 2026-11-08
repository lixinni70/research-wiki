#!/usr/bin/env python3
"""
build.py — 把 wiki/、outputs/、CLAUDE.md 建成 GitHub Pages 網站（輸出到 docs/）。

用法：  python build.py
需求：  只用 Python 3.8+ 標準函式庫，不需要安裝任何套件。
規則：  見 CLAUDE.md 第 9 節。docs/ 是產物，不要手動修改，改來源後重新執行即可。
"""
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
SITE_TITLE = "研究 Wiki 知識庫"

TYPE_LABEL = {
    "source": "來源", "concept": "概念", "model": "模型", "org": "機構", "person": "人物",
    "benchmark": "評測基準", "comparison": "比較", "synthesis": "綜述", "overview": "總覽",
    "index": "目錄", "log": "紀錄", "questions": "問題", "research-note": "研究筆記",
    "slides-outline": "簡報大綱", "rules": "專案規則",
}
NAV = [("首頁", "index.html"), ("目錄", "wiki/index.html"), ("總覽", "wiki/overview.html"),
       ("研究產出", "research/index.html"), ("開放問題", "wiki/questions.html"),
       ("更新紀錄", "wiki/log.html"), ("專案規則", "rules.html")]

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]")
CODE_RE = re.compile(r"(```[\s\S]*?```|`[^`\n]*`)")


# ---------- 讀取 ----------
def parse_frontmatter(text):
    """解析簡單的 YAML frontmatter（key: value / key: [a, b]）。"""
    meta, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block, body = text[3:end], text[end + 4:].lstrip("\n")
            for line in block.splitlines():
                m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(#.*)?$", line)
                if not m:
                    continue
                k, v = m.group(1), m.group(2)
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
                else:
                    v = v.strip('"\'')
                meta[k] = v
    return meta, body


class Page:
    def __init__(self, name, url, src, kind):
        self.name, self.url, self.src, self.kind = name, url, src, kind
        text = src.read_text(encoding="utf-8")
        self.meta, self.body = parse_frontmatter(text)
        h1 = re.search(r"^#\s+(.+)$", self.body, re.M)
        self.title = self.meta.get("title") or (h1.group(1) if h1 else name)
        self.links = set()


def collect():
    pages = {}
    for f in sorted((ROOT / "wiki").rglob("*.md")):
        rel = f.relative_to(ROOT / "wiki")
        folder = rel.parts[0] if len(rel.parts) > 1 else ""
        pages[f.stem] = Page(f.stem, f"wiki/{f.stem}.html", f, folder or "core")
    research = []
    out = ROOT / "outputs"
    if out.exists():
        for d in sorted(out.iterdir(), reverse=True):
            if not d.is_dir():
                continue
            item = {"dir": d, "slug": d.name, "notes": None, "outline": None, "slides": None}
            if (d / "notes.md").exists():
                p = Page(f"{d.name}/notes", f"research/{d.name}/index.html", d / "notes.md", "research")
                pages[p.name] = p
                item["notes"] = p
            if (d / "slides-outline.md").exists():
                p = Page(f"{d.name}/outline", f"research/{d.name}/outline.html", d / "slides-outline.md", "research")
                pages[p.name] = p
                item["outline"] = p
            if (d / "slides.html").exists():
                item["slides"] = f"research/{d.name}/slides.html"
            research.append(item)
    rules = Page("rules", "rules.html", ROOT / "CLAUDE.md", "rules")
    rules.meta["type"] = "rules"
    pages["__rules"] = rules
    return pages, research


# ---------- 轉換 ----------
def rel(from_url, to_url):
    depth = from_url.count("/")
    return "../" * depth + to_url


def convert_links(page, pages):
    """把 [[頁面|文字]] 換成 Markdown 連結；程式碼區塊內不轉換。"""
    def sub(m):
        target = m.group(1).strip()
        p = pages.get(target)
        label = (m.group(2) or (p.title if p else target)).strip()
        if p:
            page.links.add(target)
            return f"[{label}]({rel(page.url, p.url)})"
        return f'<span class="missing" title="尚未建立的頁面">{html.escape(label)}</span>'
    parts = CODE_RE.split(page.body)
    return "".join(p if i % 2 else LINK_RE.sub(sub, p) for i, p in enumerate(parts))


def meta_links(value, page, pages):
    vals = value if isinstance(value, list) else [value]
    out = []
    for v in vals:
        m = LINK_RE.search(v)
        if m and m.group(1).strip() in pages:
            p = pages[m.group(1).strip()]
            out.append(f'<a href="{rel(page.url, p.url)}">{html.escape(p.title)}</a>')
        elif v:
            out.append(html.escape(LINK_RE.sub(lambda x: x.group(2) or x.group(1), v)))
    return out


# ---------- 版面 ----------
def layout(url, title, main, aside="", full=False, active=""):
    up = "../" * url.count("/")
    nav = "".join(
        f'<a href="{up}{href}"{" class=on" if href == active else ""}>{label}</a>' for label, href in NAV)
    return f"""<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {SITE_TITLE}</title>
<link rel="stylesheet" href="{up}assets/katex.min.css">
<link rel="stylesheet" href="{up}assets/site.css">
</head><body>
<header class="top"><div class="in"><a class="brand" href="{up}index.html">{SITE_TITLE}</a><nav class="main">{nav}</nav></div></header>
<div class="wrap{' full' if full else ''}"><main>{main}</main>{f'<aside>{aside}</aside>' if aside else ''}</div>
<footer>由 AI 依 <a href="{up}rules.html">CLAUDE.md</a> 規則維護 · 最後建置 {date.today().isoformat()}</footer>
<script src="{up}assets/marked.min.js"></script>
<script src="{up}assets/katex.min.js"></script>
<script src="{up}assets/auto-render.min.js"></script>
<script src="{up}assets/site.js"></script>
</body></html>"""


def md_block(md):
    safe = md.replace("</script", "<\\/script")
    return f'<script type="text/markdown" id="md">{safe}</script><article id="content"></article>'


def render_page(page, pages, backlinks):
    md = convert_links(page, pages)
    m = page.meta
    typ = m.get("type", page.kind)
    crumb = TYPE_LABEL.get(typ, typ)
    if m.get("domain"):
        crumb += " · " + m["domain"]
    rows = []
    if m.get("status"):
        rows.append(("狀態", f'<span class="status-{m["status"]}">{m["status"]}</span>'))
    for k, label in [("authors", "作者"), ("year", "年份"), ("venue", "出處"), ("org", "機構"),
                     ("created", "建立"), ("updated", "更新"), ("ingested", "匯入")]:
        if m.get(k):
            rows.append((label, "、".join(meta_links(m[k], page, pages))))
    if m.get("url", "").startswith("http"):
        rows.append(("連結", f'<a href="{html.escape(m["url"])}">原文</a>'))
    aside = ""
    if rows or m.get("tags"):
        dl = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows)
        tags = "".join(f'<span class="tag">{html.escape(t)}</span>' for t in (m.get("tags") or []))
        aside += f'<div class="box"><h4>頁面資訊</h4><dl>{dl}</dl>{"<p>" + tags + "</p>" if tags else ""}'
        srcs = meta_links(m.get("sources") or m.get("wiki_pages") or [], page, pages)
        if srcs:
            title = "使用的 wiki 頁面" if m.get("wiki_pages") else "來源"
            aside += f"<h4 style='margin-top:16px'>{title}</h4><ul>" + "".join(f"<li>{s}</li>" for s in srcs) + "</ul>"
        bl = sorted(backlinks.get(page.name, []), key=lambda p: p.title)
        if bl:
            aside += "<h4 style='margin-top:16px'>反向連結</h4><ul>" + "".join(
                f'<li><a href="{rel(page.url, p.url)}">{html.escape(p.title)}</a></li>' for p in bl) + "</ul>"
        aside += "</div>"
    main = f'<div class="crumb">{html.escape(crumb)}</div>' + md_block(md)
    active = page.url if page.url in [h for _, h in NAV] else ""
    return layout(page.url, page.title, main, aside, full=not aside, active=active)


def render_home(pages, research):
    wiki = [p for p in pages.values() if p.url.startswith("wiki/")]
    n_src = sum(1 for p in wiki if p.kind == "sources")
    n_con = sum(1 for p in wiki if p.kind == "concepts")
    log = (ROOT / "wiki" / "log.md").read_text(encoding="utf-8")
    entries = re.findall(r"^## \[(\d{4}-\d{2}-\d{2})\] (\w+) \| (.+)$", log, re.M)[::-1][:6]
    kind_label = {"ingest": "匯入", "query": "查詢", "lint": "健檢", "research": "研究",
                  "refactor": "重構", "schema": "規則", "setup": "建立"}
    log_html = "".join(f'<li><span class="d">{d}</span><span class="k">{kind_label.get(k, k)}</span>'
                       f'<span>{html.escape(t)}</span></li>' for d, k, t in entries)
    res_html = "".join(research_item(r, "index.html") for r in research[:5]) or "<li>（尚無）</li>"
    stats = [(n_src, "來源", "var(--primary)"), (len(wiki), "wiki 頁面", "var(--c2)"),
             (n_con, "概念", "var(--c3)"), (len(research), "研究產出", "var(--c4)")]
    cards = [("目錄", "wiki/index.html", "所有頁面一覽，依類型分類", "var(--primary)"),
             ("領域總覽", "wiki/overview.html", "領域地圖、核心論點、時間線", "var(--c2)"),
             ("開放問題", "wiki/questions.html", "待研究問題與建議閱讀", "var(--c3)"),
             ("研究產出", "research/index.html", "根據 wiki 寫成的筆記與簡報", "var(--c4)"),
             ("更新紀錄", "wiki/log.html", "每次匯入、研究、修改的時間序紀錄", "var(--c5)"),
             ("專案規則", "rules.html", "給 AI 的完整規則（CLAUDE.md）", "var(--primary)")]
    main = f"""
<section class="hero"><h1>{SITE_TITLE}</h1>
<p>一個由 AI 維護的個人研究知識庫。我負責挑選資料和提出問題；AI 依照 <a href="rules.html">CLAUDE.md</a> 的規則，
把每份來源消化成互相連結的 wiki 頁面，再產出研究筆記、簡報和這個網站。</p>
<div class="flowline"><span>放入來源 raw/</span><i>→</i><span>匯入成 wiki/</span><i>→</i><span>研究筆記與簡報 outputs/</span><i>→</i><span>build.py 產生網站 docs/</span></div></section>
<div class="stats">{''.join(f'<div class="stat" style="--c:{c}"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l, c in stats)}</div>
<div class="cards">{''.join(f'<a class="card" style="--c:{c}" href="{h}"><h3>{t}</h3><p>{d}</p></a>' for t, h, d, c in cards)}</div>
<h2 class="sec-title">最新研究產出</h2><ul class="list">{res_html}</ul>
<h2 class="sec-title">最近更新</h2><ul class="list">{log_html}</ul>"""
    return layout("index.html", "首頁", main, full=True, active="index.html")


def research_item(r, from_url):
    title = r["notes"].title if r["notes"] else r["slug"]
    d = r["slug"][:10]
    btns = []
    if r["notes"]:
        btns.append(f'<a class="btn" href="{rel(from_url, r["notes"].url)}">研究筆記</a>')
    if r["outline"]:
        btns.append(f'<a class="btn" href="{rel(from_url, r["outline"].url)}">逐頁大綱</a>')
    if r["slides"]:
        btns.append(f'<a class="btn solid" href="{rel(from_url, r["slides"])}">開啟簡報</a>')
    return (f'<li><span class="d">{d}</span><div><div>{html.escape(title)}</div>'
            f'<div class="btns">{"".join(btns)}</div></div></li>')


def render_research_index(research):
    url = "research/index.html"
    items = "".join(research_item(r, url) for r in research) or "<li>（尚無）</li>"
    main = (f'<div class="crumb">研究產出</div><article><h1>研究產出</h1>'
            f'<p>每個題目都依 CLAUDE.md 4.4 節產出：正文只使用 wiki 內容，最後附建議參考文獻。'
            f'簡報可以用 ←／→ 翻頁，按 N 顯示講者備註，按 F 全螢幕。</p></article><ul class="list">{items}</ul>')
    return layout(url, "研究產出", main, full=True, active=url)


# ---------- 主程式 ----------
def build():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "assets").mkdir(parents=True)
    for f in ["site.css", "site.js"]:
        shutil.copy(SITE / f, DOCS / "assets" / f)
    for f in (SITE / "vendor").iterdir():
        shutil.copy(f, DOCS / "assets" / f.name)
    for sub in ["raw/assets", "wiki/assets"]:   # 圖片
        if (ROOT / sub).exists():
            shutil.copytree(ROOT / sub, DOCS / sub, dirs_exist_ok=True)
    (DOCS / ".nojekyll").write_text("")

    pages, research = collect()
    for p in pages.values():          # 先轉一次以收集連結
        convert_links(p, pages)
    backlinks = {}
    for p in pages.values():
        for t in p.links:
            if t != p.name:
                backlinks.setdefault(t, []).append(p)

    count = 0
    for p in pages.values():
        out = DOCS / p.url
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(p, pages, backlinks), encoding="utf-8")
        count += 1
    for r in research:
        if r["slides"]:
            dst = DOCS / r["slides"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(r["dir"] / "slides.html", dst)
            if (r["dir"] / "assets").exists():
                shutil.copytree(r["dir"] / "assets", dst.parent / "assets", dirs_exist_ok=True)
    (DOCS / "index.html").write_text(render_home(pages, research), encoding="utf-8")
    (DOCS / "research").mkdir(exist_ok=True)
    (DOCS / "research" / "index.html").write_text(render_research_index(research), encoding="utf-8")

    missing = sorted({m.group(1) for p in pages.values() if p.kind != "rules" for m in LINK_RE.finditer(CODE_RE.sub("", p.body))
                      if m.group(1).strip() not in pages})
    print(f"完成：{count + 2} 個頁面、{len(research)} 個研究產出 → docs/")
    if missing:
        print("尚未建立的連結：", "、".join(missing))


if __name__ == "__main__":
    build()
