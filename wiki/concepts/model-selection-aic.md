---
type: concept
title: AIC 模型選擇
aliases: [AIC, AICc, BIC, 資訊準則]
tags: [研究方法, 統計]
domain: 研究方法
created: 2026-11-18
updated: 2026-11-18
sources: ["[[2014-mondal-arima-stock-forecasting]]"]
status: draft
---

# AIC 模型選擇（Model Selection with AIC）

## 定義
赤池資訊準則（Akaike Information Criterion）同時衡量「模型配適得多好」和「模型有多複雜」，數值越小越好。AICc 是針對小樣本的修正版。

## 直覺解釋
參數越多，模型越能貼合舊資料，但也越容易「背答案」、預測新資料時失準。AIC 對多出來的參數扣分，幫你在兩者之間取得平衡。

## 實例
[[2014-mondal-arima-stock-forecasting]] 對 Emami Limited 的股價試了 9 組 ARIMA 參數，ARIMA(1,0,2) 的 AICc 為 −2175.97，是最小值，所以選它（[[2014-mondal-arima-stock-forecasting]]）。

## AIC vs BIC
BIC 對複雜度扣分更重。作者引用 Burnham & Anderson、Yang（2005）的說法，認為真實模型通常不在候選名單內時，AIC 比較合適（[[2014-mondal-arima-stock-forecasting]]）。

## 相關概念
[[arima-time-series]]
