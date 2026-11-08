---
type: concept
title: 方案設置評估法
aliases: [Program Placement Evaluation, 方案設置偏誤, Program Placement Bias, 設置模型]
tags: [影響評估, 計量經濟學, 研究方法]
domain: 研究方法
created: 2026-11-08
updated: 2026-11-08
sources: ["[[2011-hamid-micro-health-insurance-poverty-bangladesh]]"]
status: draft
---

# 方案設置評估法（Program Placement Evaluation）

## 定義
在非實驗資料下評估社會方案的一種方法：比較「方案已設置的地區」和「方案未設置的地區」的結果，而不是比較「個人有沒有參與」。

## 為什麼需要
用「參與」來估計效果時，會遇到**內生性**問題：一些觀察不到的個人特質，可能同時影響參與決定和結果。

- 結構式：{ij} = X_{ij}\beta + A_{ij}\delta + \varepsilon_{ij}$，其中 $ 表示是否參與。
- 參與式：{ij} = X_{ij}\beta + Z_{ij}\phi + \mu_{ij}$
- 如果 $\varepsilon$ 和 $\mu$ 相關，$\delta$ 的估計就會有偏誤（[[2011-hamid-micro-health-insurance-poverty-bangladesh]]）。

## 設置模型
{ij} = X_{ij}\beta + P_{ij}\lambda + \varepsilon_{ij}$，其中 =1$ 代表方案地區，=0$ 代表對照地區。$\lambda$ 估計的是**平均處理效果（ATE）**。

**比 ATT 適合的情況**（[[2011-hamid-micro-health-insurance-poverty-bangladesh]]）：
- 方案有外溢效果，未參與者也會受益。
- 參與率很高，未參與者的觀察值太少。

## 主要風險：方案設置偏誤
方案通常不是隨機設置的，組織會選擇條件好（或差）的地區，這些地區特徵本身就會影響結果。

**緩解方法**（[[2011-hamid-micro-health-insurance-poverty-bangladesh]] 的做法）：
1. 方案區和對照區選在同一個小地理範圍。
2. 選擇方案「即將設置」的地區當對照（pipeline comparison；文獻見 Chase 2002；Galasso & Ravallion 2004）。
3. 調查對照區的參與意願，控制需求面偏誤。

## 文獻中的兩種對照組
- 方案在規劃中的地區（Chase 2002；Galasso & Ravallion 2004）
- 調查時方案尚未設置的地區（Amin, Li & Ahmed 1996；Hadi 2002）

## 限制
- 只能減輕設置偏誤，無法完全消除。只要方案區和對照區還有其他系統性差異，例如 [[2011-hamid-micro-health-insurance-poverty-bangladesh]] 中兩區加入微型貸款的時間不同，就會混入估計。
- 地區數很少時，等於只有一組對照（推論）。

## 相關概念
- [[micro-health-insurance]] · [[informal-risk-sharing]]（非正式保險在比較時也可能造成偏誤）
