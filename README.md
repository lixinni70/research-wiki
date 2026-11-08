# 研究 Wiki 知識庫

一個由 AI（Claude）維護的個人研究知識庫，參考 [Karpathy 的 LLM Wiki 模式](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。
放入論文 → AI 消化成互相連結的 wiki → 產出研究筆記與簡報 → 自動建成網站。

## 結構

| 資料夾 | 內容 | 誰寫 |
|---|---|---|
| `raw/` | 原始來源（論文、文章） | 我，只放不改 |
| `wiki/` | 互相連結的知識頁面 | AI |
| `outputs/` | 研究筆記、簡報 | AI |
| `templates/` | 頁面與簡報的樣板 | 共同 |
| `docs/` | 網站（GitHub Pages，由 `build.py` 產生） | 自動 |
| `CLAUDE.md` | 給 AI 的完整規則 | 共同 |

## 常用指令（對 AI 說）

- 「匯入 raw/papers/檔名.pdf」→ 建立或更新 wiki 頁面
- 「研究：題目」→ 產出 `outputs/日期-題目/notes.md`
- 「做簡報」→ 產出逐頁大綱與 HTML 簡報
- 「健檢」→ 檢查矛盾、孤兒頁、缺口
- 「更新網站」→ 執行 `python build.py`，重新產生 `docs/`

## 建網站

```bash
python build.py      # 只用 Python 標準函式庫，不需要安裝套件
```

之後把整個資料夾推上 GitHub，在 Settings → Pages 選 `main` 分支的 `/docs`。
