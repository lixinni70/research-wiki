---
type: concept
title: 交互作用項與非線性
aliases: [Interaction Terms, 平方項, Quadratic Terms]
tags: [研究方法, 計量]
domain: 研究方法
created: 2026-11-18
updated: 2026-11-18
sources: ["[[2007-cull-financial-performance-outreach-microbanks]]"]
status: draft
---

# 交互作用項與非線性（Interaction and Nonlinear Terms）

## 交互作用項：效果會因群體而不同
把兩個變數相乘放進迴歸，例如 $Yield \times Type$，就能讓「利率對獲利的影響」在不同放款方式之間不一樣。

- [[2007-cull-financial-performance-outreach-microbanks]] 以個人放款機構為基準組；交互作用項的係數表示團體放款或村落銀行和基準組的**差距**（[[2007-cull-financial-performance-outreach-microbanks]]）。

## 平方項：效果先升後降
加入 $x^2$，可以描述「到某個程度後就不再增加」的關係。

$$y=\beta_1 x+\beta_2 x^2,\quad \beta_1>0,\ \beta_2<0 \Rightarrow \text{倒 U 型}$$

- 個人放款機構的獲利隨利率上升，但在年利率約 60% 附近趨平（[[2007-cull-financial-performance-outreach-microbanks]]）。
- 逾期比例與收益率呈倒 U 型，高點約在收益率 40%（[[2007-cull-financial-performance-outreach-microbanks]]）。
- 貸款金額與每元成本呈 U 型（[[2007-cull-financial-performance-outreach-microbanks]]）。

## 注意
作者提醒，線性項和平方項高度相關時，可能「假性地」產生這種彎曲形狀，所以要搭配理論解讀（[[2007-cull-financial-performance-outreach-microbanks]]）。

## 相關概念
[[regression-analysis]]
