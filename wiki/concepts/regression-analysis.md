---
type: concept
title: 迴歸分析
aliases: [Regression Analysis, OLS, 最小平方法]
tags: [研究方法, 計量]
domain: 研究方法
created: 2026-11-18
updated: 2026-11-18
sources: ["[[2007-cull-financial-performance-outreach-microbanks]]"]
status: draft
---

# 迴歸分析（Regression Analysis）

## 定義
用一條方程式描述「結果變數 $y$」如何隨著幾個「解釋變數 $x$」變動，並估計每個 $x$ 的影響方向和大小。最常用的是普通最小平方法（Ordinary Least Squares, OLS）。

$$y_i=\alpha+\beta_1 x_{1i}+\beta_2 x_{2i}+\dots+\varepsilon_i$$

## 直覺解釋
把很多機構的資料畫在圖上，找一條最貼近所有點的線。係數 $\beta$ 告訴你：其他條件不變時，$x$ 多 1 單位，$y$ 平均多多少。

## 怎麼讀迴歸表
- **係數**：正負代表方向，大小代表幅度。
- **t 值或標準誤**：判斷係數是否可能只是巧合；星號代表顯著水準（* 10%、** 5%、*** 1%）。
- **控制變數**：放進年齡、規模、地區等變數，是為了「在其他條件相同時」比較。
- **$R^2$**：模型解釋了多少變異。

## 實例
[[2007-cull-financial-performance-outreach-microbanks]] 用 104 家微型金融機構，以財務自足率為 $y$，以放款收益率、成本、放款方式、規模、年齡、地區為 $x$。個人放款機構的收益率係數 0.964、在 1% 水準顯著（[[2007-cull-financial-performance-outreach-microbanks]]）。

## 優點與限制
- 優點：可以同時考慮很多因素，資料容易取得。
- 限制：只能說明**相關**；如果有沒觀察到的因素同時影響 $x$ 和 $y$，或 $y$ 反過來影響 $x$，係數就不代表因果（見 [[correlation-vs-causation]]）。

## 相關概念
[[interaction-and-nonlinear-terms]] · [[correlation-vs-causation]] · [[program-placement-evaluation]] · [[research-methods-comparison]]
