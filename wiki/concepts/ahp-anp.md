---
type: concept
title: AHP 與 ANP 多準則決策
aliases: [AHP, ANP, Analytic Hierarchy Process, Analytic Network Process, 成對比較]
tags: [研究方法, 決策分析]
domain: 研究方法
created: 2026-11-18
updated: 2026-11-18
sources: ["[[2022-li-light-steel-housing-anp]]"]
status: draft
---

# AHP 與 ANP 多準則決策

## 定義
- **分析層級程序法（AHP）**：Saaty 於 1971 年提出。把決策拆成「目標 → 準則 → 方案」的樹狀層級，透過兩兩比較算出各準則的權重；假設同一層的準則彼此獨立（[[2022-li-light-steel-housing-anp]]）。
- **分析網路程序法（ANP）**：AHP 的進階版，允許準則之間互相影響、有回饋關係，用超級矩陣計算（[[2022-li-light-steel-housing-anp]]）。

## 直覺解釋
一次比較 11 個條件很難；但「維護和造價哪個重要？重要多少？」一次只比兩個就容易多了。把所有兩兩比較的答案整理起來，就能算出每個條件的權重。

## 步驟
1. 建立層級架構（目標、構面、要素、方案）。
2. 用 1–9 點尺度做成對比較：1 同等重要、3 稍微重要、5 頗為重要、7 極為重要、9 絕對重要（[[2022-li-light-steel-housing-anp]]）。
3. 由成對比較矩陣求特徵向量：$AW=\lambda W$。
4. 一致性檢定，CR 不超過 0.1 才算合格：

$$CI=\frac{\lambda_{max}-n}{n-1},\qquad CR=\frac{CI}{RI}\le 0.1$$

例如受訪者說 A 比 B 重要、B 比 C 重要，卻又說 C 比 A 重要，CR 就會偏高，這份答案不可靠。

5. ANP 另外建立超級矩陣，反覆自乘到收斂，得到考慮相依性的權重。

## 實例
[[2022-li-light-steel-housing-anp]] 用 4 個構面、11 項要素評估小型住宅：
- 民眾最看重建築維護 0.1267（[[2022-li-light-steel-housing-anp]]）。
- 考慮相依性後，專家最看重造價預算 0.1858（[[2022-li-light-steel-housing-anp]]）。
- 283 份有效問卷中只有 182 份（64%）通過一致性檢定（[[2022-li-light-steel-housing-anp]]）。

## 優點與限制
- 優點：把主觀判斷變成可比較的數字；適合沒有現成資料的決策問題。
- 限制：成對比較題目多，受訪者容易前後矛盾；結果反映的是「受訪者的偏好」，不是客觀事實。

## 相關概念
[[research-methods-comparison]]
