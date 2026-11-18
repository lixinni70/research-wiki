#!/usr/bin/env python3
"""
G3 對應閘（CLAUDE.md 4.6）

用法：python tools/check_outline.py outputs/<題目>/slides-outline.md
檢查：
  E1 每一頁（## n｜標題）都有「出處」行
  E2 出處列出的 [[頁面]] 都存在於 wiki
  E3 內容頁的出處不可以是「無」（只有封面、章節頁、測驗頁、延伸閱讀可以）
  E4 notes.md 列出的「wiki 沒有、簡報不能講的內容」沒有出現在大綱
錯誤 > 0 → 回 N4；如果 wiki 真的沒有需要的內容 → 回 N1 補資料。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    names = {f.stem for f in (ROOT / "wiki").rglob("*.md")}
    blocks = re.split(r"^## (?=\d+｜)", text, flags=re.M)[1:]
    errors = []
    for b in blocks:
        title = b.splitlines()[0]
        m = re.search(r"\*\*出處\*\*：(.+)", b)
        if not m:
            errors.append(f"E1 「{title}」沒有出處")
            continue
        src = m.group(1)
        links = re.findall(r"\[\[([^\]|]+)", src)
        if not links:
            if not src.startswith("無（") or not re.search(r"封面|章節|測驗|延伸", src):
                errors.append(f"E3 「{title}」是內容頁，但出處為「{src}」")
        for l in links:
            if l not in names:
                errors.append(f"E2 「{title}」引用不存在的頁面 [[{l}]]")

    notes = path.with_name("notes.md")
    if notes.exists():
        nt = notes.read_text(encoding="utf-8")
        sec = nt.split("## wiki 沒有、簡報不能講的內容")[-1] if "簡報不能講" in nt else ""
        for item in re.findall(r"^- (.+?)(?:\s*→|$)", sec, flags=re.M):
            kw = re.split(r"[（(]", item)[0].strip()
            body = re.sub(r"^## \d+｜延伸閱讀[\s\S]*?(?=^## |\Z)", "", text, flags=re.M)
            if kw and kw in body:
                errors.append(f"E4 大綱提到 wiki 沒有的內容：{kw}")

    print(f"G3 對應閘：{len(blocks)} 頁｜錯誤 {len(errors)}")
    for e in errors:
        print("  " + e)
    print("結果：" + ("通過 ✅" if not errors else "沒通過 ❌ → 回 N4"))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
