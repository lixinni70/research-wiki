#!/usr/bin/env python3
r"""
G2 wiki 檢查閘（CLAUDE.md 4.6）

用法：python tools/check_wiki.py
檢查：
  E1 [[連結]] 指向的頁面都存在
  E2 frontmatter 必填欄位齊全（type、title、created、updated）
  E3 檔名全 wiki 唯一
  E4 數學式 $ 沒有成對（例如被 shell 吃掉，只剩單獨的 $）
  E5 連結目標含反斜線（表格中 [[頁面\|文字]] 的寫法會讓連結失效）
  W1 孤兒頁（沒有任何頁面連到它）
  W2 概念／比較頁中含數字的句子沒有附 [[出處]]
錯誤（E）> 0 時結束碼為 1，代表沒通過，要回到 N2 修正。
只用 Python 標準函式庫。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
LINK = re.compile(r"\[\[([^\]|#]+)")
CODE = re.compile(r"```[\s\S]*?```|`[^`\n]*`")
NUM = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)?%?")
REQUIRED = ["type", "title", "created", "updated"]
CORE = {"index", "log", "questions"}          # 這幾頁格式不同，不檢查 E2


def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    meta = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta, text[end + 4:]


def main():
    files = sorted(WIKI.rglob("*.md"))
    names = {}
    errors, warns = [], []
    for f in files:
        if f.stem in names:
            errors.append(f"E3 檔名重複：{f.stem}（{names[f.stem]} 與 {f.relative_to(ROOT)}）")
        names[f.stem] = f.relative_to(ROOT)

    inbound = {n: 0 for n in names}
    for f in files:
        text = f.read_text(encoding="utf-8")
        meta, body = frontmatter(text)
        rel = f.relative_to(ROOT)
        if f.stem not in CORE:
            miss = [k for k in REQUIRED if not meta.get(k)]
            if miss:
                errors.append(f"E2 {rel} 缺少 frontmatter：{', '.join(miss)}")
        plain = CODE.sub("", text)
        for target in set(t.strip() for t in LINK.findall(plain)):
            if target not in names:
                errors.append(f"E1 {rel} 連到不存在的頁面：[[{target}]]")
            elif target != f.stem:
                inbound[target] += 1
        for i, line in enumerate(plain.splitlines(), 1):
            if line.count("$") % 2 == 1:
                errors.append(f"E4 {rel}:{i} 數學式 $ 沒有成對：{line.strip()[:40]}")
            if re.search(r"\[\[[^\]]*\\", line):
                errors.append(f"E5 {rel}:{i} 連結目標含反斜線：{line.strip()[:40]}")
        if f.parent.name in ("concepts", "comparisons"):
            for i, line in enumerate(CODE.sub("", body).splitlines(), 1):
                if line.startswith(("|", "#", ">", "$$")) or "$" in line:
                    continue                       # 表格、標題、引文、數學式另外處理
                line = re.sub(r"^\s*(\d+\.|[-*])\s+", "", line)   # 去掉清單編號
                nums = [n for n in NUM.findall(line) if not re.fullmatch(r"(19|20)\d\d", n)]
                if nums and "[[" not in line:
                    warns.append(f"W2 {rel}:{i} 有數字 {nums[:3]} 但沒有 [[出處]]")

    for n, c in inbound.items():
        if c == 0 and n not in CORE | {"overview"}:
            warns.append(f"W1 孤兒頁：{n}")

    print(f"G2 wiki 檢查：{len(files)} 頁｜錯誤 {len(errors)}｜警告 {len(warns)}")
    for e in errors:
        print("  " + e)
    for w in warns:
        print("  " + w)
    print("結果：" + ("通過 ✅" if not errors else "沒通過 ❌ → 回到 N2 修正"))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
