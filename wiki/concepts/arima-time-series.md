---
type: concept
title: ARIMA 時間序列模型
aliases: [ARIMA, Box-Jenkins, 自我迴歸整合移動平均]
tags: [研究方法, 時間序列, 預測]
domain: 研究方法
created: 2026-11-18
updated: 2026-11-18
sources: ["[[2014-mondal-arima-stock-forecasting]]"]
status: draft
---

# ARIMA 時間序列模型

## 定義
自我迴歸整合移動平均模型（AutoRegressive Integrated Moving Average），寫成 ARIMA($p,d,q$)，用一個變數**自己的過去**來預測它的未來。

| 參數 | 意思 |
|---|---|
| $p$ | 自我迴歸（AR）：用過去幾期的值 |
| $d$ | 差分次數：把有趨勢的序列變成平穩序列 |
| $q$ | 移動平均（MA）：用過去幾期的預測誤差 |

## 直覺解釋
預測明天的股價時，最好的線索常常是今天和最近幾天的股價。ARIMA 就是把「最近的值」和「最近猜錯多少」組合起來。

## 建模步驟（Box-Jenkins）
1. **辨識**：試幾組 $p,d,q$，用 [[model-selection-aic|AIC/AICc]] 挑最好的。
2. **估計**：算出係數。
3. **檢查**：殘差的 ACF、PACF 應該沒有顯著的落後項。
4. **預測**：用樣本外資料評估準確度。

## 實例
[[2014-mondal-arima-stock-forecasting]] 預測 56 檔印度股票未來 30 天的價格，7 個產業的平均準確度都在 85% 以上；不同訓練長度之間沒有顯著差異（[[2014-mondal-arima-stock-forecasting]]）。

## 限制
- 只看自己的過去，不考慮新聞、利率等外部因素。
- 評估預測模型時，應該和簡單基準（例如「明天＝今天」）比較；高準確度不等於有預測價值（見 [[2014-mondal-arima-stock-forecasting]] 的注意事項）。

## 相關概念
[[model-selection-aic]] · [[research-methods-comparison]]
