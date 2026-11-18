#!/usr/bin/env python3
"""
G4 簡報檢查閘（CLAUDE.md 4.6）

用法：python tools/check_slides.py outputs/<題目>/slides.html [--render]
檢查：
  E1 每個 <section class="slide"> 都有 data-src
  E2 data-src 列出的 wiki 頁面都存在
  E3 投影片裡的每個數字，都能在它引用的 wiki 頁面中找到（防止編造或抄錯數字）
  E4（加 --render 且有安裝 playwright 時）內容超出 1280×720 版面
  W1（--render）內容頁只用到不到 75% 的高度，投影時字太小、版面太空
不檢查：<span class="note-inference"> 內的文字、頁碼、程式碼。
錯誤 > 0 時結束碼為 1：數字或出處錯 → 回 N5；結構錯 → 回 N4。
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NUM = re.compile(r"(?<![\w.])-?\d+(?:,\d{3})*(?:\.\d+)?%?")


class Slides(HTMLParser):
    """把每張投影片的 data-src 和可見文字取出來。"""
    SKIP = {"script", "style", "code"}
    VOID = {"br", "img", "hr", "input", "meta", "link", "source", "wbr", "col", "area"}

    def __init__(self):
        super().__init__()
        self.slides, self.cur, self.depth, self.skip = [], None, 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag == "section" and "slide" in cls.split():
            self.cur = {"src": a.get("data-src"), "text": [], "line": self.getpos()[0]}
            self.depth = 0
        if self.cur is None or tag in self.VOID:
            return
        self.depth += 1
        if tag in self.SKIP or "note-inference" in cls or "notes" in cls.split() or "foot" in cls.split():
            self.skip += 1
            self.cur.setdefault("skipstack", []).append(self.depth)

    def handle_endtag(self, tag):
        if self.cur is None or tag in self.VOID:
            return
        st = self.cur.get("skipstack", [])
        if st and st[-1] == self.depth:
            st.pop()
            self.skip -= 1
        self.depth -= 1
        if tag == "section" and self.depth <= 0:
            self.slides.append(self.cur)
            self.cur = None

    def handle_data(self, data):
        if self.cur is not None and self.skip == 0:
            self.cur["text"].append(data)


def norm(n):
    return n.replace(",", "").rstrip("%").lstrip("-")


def wiki_text(name):
    hits = list((ROOT / "wiki").rglob(f"{name}.md"))
    return hits[0].read_text(encoding="utf-8") if hits else None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    path = Path(sys.argv[1])
    p = Slides()
    p.feed(path.read_text(encoding="utf-8"))
    errors, warns, checked = [], [], 0
    for i, s in enumerate(p.slides, 1):
        title = re.sub(r"\s+", " ", "".join(s["text"])).strip()[:28]
        if not s["src"]:
            errors.append(f"E1 第 {i} 頁「{title}」沒有 data-src → 回 N4")
            continue
        if s["src"] == "none":
            continue
        pages = [x.strip() for x in s["src"].split(",") if x.strip()]
        corpus = ""
        for pg in pages:
            t = wiki_text(pg)
            if t is None:
                errors.append(f"E2 第 {i} 頁引用不存在的 wiki 頁面：{pg} → 回 N4")
            else:
                corpus += t
        pool = {norm(n) for n in NUM.findall(corpus)}
        text = " ".join(s["text"])
        for n in NUM.findall(text):
            k = norm(n)
            if len(k) == 1 and "." not in k:      # 個位數（單元編號、1 題）略過
                continue
            checked += 1
            if k not in pool:
                errors.append(f"E3 第 {i} 頁的數字「{n}」在 {', '.join(pages)} 找不到 → 回 N5")

    if "--render" in sys.argv:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                b = pw.chromium.launch()
                pg = b.new_page(viewport={"width": 1280, "height": 720})
                pg.goto(path.resolve().as_uri())
                pg.wait_for_timeout(800)
                over = pg.evaluate("""() => [...document.querySelectorAll('.slide')].map((s,i)=>{
                    s.style.display='flex'; s.style.transform='none';
                    const r=s.scrollHeight>s.clientHeight+2||s.scrollWidth>s.clientWidth+2;
                    s.style.display=''; return r?i+1:0}).filter(Boolean)""")
                fill = pg.evaluate("""() => [...document.querySelectorAll('.slide')].map((s,i)=>{
                    if(s.dataset.src==='none') return null;
                    s.style.display='flex'; s.style.transform='none';
                    const top=s.getBoundingClientRect().top; let b=0;
                    s.querySelectorAll('*').forEach(c=>{if(c.closest('.foot,.notes')||c.children.length)return;
                      const r=c.getBoundingClientRect(); if(r.height>0) b=Math.max(b,r.bottom-top)});
                    s.style.display=''; return [i+1, Math.round(b/7.2)]}).filter(Boolean)""")
                b.close()
            for i, pct in fill:
                if pct < 75:
                    warns.append(f"W1 第 {i} 頁內容只用到 {pct}% 高度 → 放大字級或重排（回 N5）")
            for i in over:
                errors.append(f"E4 第 {i} 頁內容超出版面 → 回 N5")
        except ImportError:
            print("（沒有安裝 playwright，略過版面檢查 E4）")

    expected = len(re.findall(r'<section class="slide', path.read_text(encoding="utf-8")))
    if expected != len(p.slides):
        errors.append(f"E0 解析到 {len(p.slides)} 頁，但檔案有 {expected} 個 slide → 檢查腳本或 HTML 結構有誤")
    print(f"G4 簡報檢查：{len(p.slides)} 頁｜檢查數字 {checked} 個｜錯誤 {len(errors)}｜警告 {len(warns)}")
    for e in errors + warns:
        print("  " + e)
    print("結果：" + ("通過 ✅" if not errors else "沒通過 ❌"))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
