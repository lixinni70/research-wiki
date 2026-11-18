---
type: source
title: "Study of Effectiveness of Time Series Modeling (ARIMA) in Forecasting Stock Prices"
aliases: [Mondal et al. 2014, ARIMA 股價預測]
authors: ["Prapanna Mondal", "Labani Shit", "Saptarsi Goswami"]
year: 2014
venue: International Journal of Computer Science, Engineering and Applications (IJCSEA), 4(2), 13–29
url: https://doi.org/10.5121/ijcsea.2014.4202
raw: raw/papers/2014-mondal-arima-stock-forecasting.pdf
tags: [時間序列, ARIMA, 預測, 股價]
domain: 計量與預測
method: ARIMA 時間序列預測＋配對 t 檢定
created: 2026-11-18
updated: 2026-11-18
ingested: 2026-11-18
status: solid
---

# Study of Effectiveness of Time Series Modeling (ARIMA) in Forecasting Stock Prices

| 項目 | 內容 |
|---|---|
| 作者 | Prapanna Mondal、Labani Shit、Saptarsi Goswami（Institute of Engineering and Management） |
| 發表 | 2014 · IJCSEA 4(2): 13–29 · DOI 10.5121/ijcsea.2014.4202 |
| 資料 | 印度國家證券交易所（NSE）7 個產業、每產業 8 家，共 56 家公司；訓練資料 2012 年 4 月到 2014 年 2 月（23 個月），預測接下來 30 天 |
| 方法 | ARIMA（[[arima-time-series]]），以 AICc（[[model-selection-aic]]） 選模型，ACF/PACF 檢查殘差，配對 t 檢定比較不同訓練長度 |

## 一句話摘要
用 ARIMA 預測 56 檔印度股票未來 30 天的價格，7 個產業的平均準確度都在 85% 以上，民生消費（FMCG）最準、汽車和銀行最差；訓練資料用 6、12、18 或 23 個月，準確度沒有顯著差異。

## 方法步驟
1. **模型辨識**：p、q 只試 2 以下（Box-Jenkins 建議），選 AICc 最小的模型。以 Emami Limited 為例，ARIMA(1,0,2) 的 AICc 為 −2175.97，是所有候選中最小。
2. **參數估計**：ARIMA(1,0,2) 的 ar1 = 0.9863（標準誤 0.0073）。
3. **模型檢查**：殘差的 ACF、PACF 沒有顯著落後項，表示模型合適。
4. **衡量準確度**：準確度 ＝ 1 − |實際值 − 預測值| ÷ 實際值，再取平均並乘以 100%。
5. **配對 t 檢定**：比較 4 種訓練長度的準確度，p 值都在 0.19 以上，無法拒絕「沒有差異」的虛無假設。

## 主要結果（原文 Table 4，23 個月訓練資料）

| 產業 | 準確度 |
|---|---|
| 民生消費 FMCG | 95.93% |
| 電力 | 92.28% |
| 基礎建設 | 91.29% |
| 資訊科技 | 91.06% |
| 銀行 | 90.51% |
| 鋼鐵 | 90.46% |
| 汽車 | 87.89% |

- 個股差異很大：汽車業的 TVS 只有 69.78%（用 18 個月資料時更低到 44.31%）。
- 汽車、銀行、鋼鐵的準確度標準差較大。

> [!warning] 方法上需要注意
> - 文中稱用 MAE（平均絕對誤差）計算準確度，但公式實際上是 1 − 絕對百分比誤差，也就是 1 − MAPE。
> - 沒有和簡單基準（例如「明天＝今天」的隨機漫步預測）比較；股價每日變動通常很小，所以 85% 以上的「準確度」不代表模型有預測能力，也不代表能獲利。**（推論）**

## 影響到的頁面
[[arima-time-series]]、[[model-selection-aic]]、[[research-methods-comparison]]
