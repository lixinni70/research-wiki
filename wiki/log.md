---
type: log
title: 更新紀錄
---

# 更新紀錄

> 只增不改。每筆以 `## [YYYY-MM-DD] 類型 | 標題` 開頭。
> 查最近 5 筆：`grep "^## \[" wiki/log.md | tail -5`

## [2026-11-08] setup | 建立 LLM 研究 Wiki
- 建立 `CLAUDE.md`（中文規範）、目錄結構、頁面範本
- 新建：[[index]]、[[overview]]、[[questions]]

## [2026-11-08] ingest | Can Micro Health Insurance Reduce Poverty? Evidence From Bangladesh
- 原檔：`raw/papers/2011-hamid-micro-health-insurance-poverty-bangladesh.pdf`
- 新建來源：[[2011-hamid-micro-health-insurance-poverty-bangladesh]]
- 新建概念：[[micro-health-insurance]]、[[microinsurance]]、[[microcredit]]、[[program-placement-evaluation]]、[[informal-risk-sharing]]、[[insurance-demand-theory]]、[[moral-hazard]]、[[adverse-selection]]、[[cost-of-basic-needs]]
- 新建機構：[[grameen-bank]]、[[grameen-kalyan]]、[[brac]]
- 新建人物：[[syed-abdul-hamid]]、[[jennifer-roberts]]、[[paul-mosley]]、[[muhammad-yunus]]
- 更新：[[index]]、[[overview]]（新增「範圍外的來源」小節）、[[questions]]
- 備註：這是第一篇試跑。來源屬於發展經濟學，不在 LLM 研究範圍內，相關頁面以 `domain` 欄位標示。使用者沒有要求討論，直接匯入。

## [2026-11-08] schema | 新增「先存原檔到 raw/」規則與 domain 欄位
- 匯入流程新增步驟 0：使用者貼上或附上的文章一律先存進 `raw/` 對應子資料夾
- frontmatter 新增選填的 `domain` 欄位，用來標示 LLM 研究範圍外的頁面

## [2026-11-08] schema | 新增研究產出流程（4.4）與 LaTeX 規範（4.5）
- 新增 `outputs/` 資料夾：每個研究題目一個子資料夾，內含 notes.md、slides-outline.md、slides.html
- 鐵則：正文只能使用 wiki 內容；網路搜尋只用來產生「建議參考文獻」（附可直接下載的連結）
- 新增第 8 節「簡報風格」（待討論）

## [2026-11-08] research | 什麼是微型健康保險？為什麼需要討論？
- 產出：`outputs/2026-11-08-what-is-mhi/`（notes.md、slides-outline.md、slides.html，共 11 頁）
- 使用 wiki 頁面：11 頁；wiki 來源數：1
- 建議文獻 4 筆，已同步到 [[questions]]

## [2026-11-08] schema | 選定簡報風格 C（暖灰褐）
- CLAUDE.md 第 8 節寫入色票、版型、圖片與數學式規範
- `templates/slides-template.html` 更新為風格 C，KaTeX 改為內嵌

## [2026-11-08] refactor | 改為不限主題的「研究 Wiki 知識庫」並建立網站
- CLAUDE.md：第 1 節改為不限主題；`domain` 欄位改為一般領域標記；新增第 9 節「網站（GitHub Pages）」
- 新增 `build.py`、`site/`（樣式與 vendor），產生 `docs/` 供 GitHub Pages 發布
- 改寫 [[overview]] 為多領域版本；更新 [[index]]、[[questions]]、README
