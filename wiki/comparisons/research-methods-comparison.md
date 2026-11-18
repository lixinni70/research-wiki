---
type: comparison
title: 5 種研究方法比較
aliases: [研究方法比較, Research Methods Comparison]
tags: [研究方法, 比較]
domain: 研究方法
created: 2026-11-18
updated: 2026-11-18
sources: ["[[2011-hamid-micro-health-insurance-poverty-bangladesh]]", "[[2007-cull-financial-performance-outreach-microbanks]]", "[[2015-popova-otc-vs-exchange-traded-derivatives]]", "[[2014-mondal-arima-stock-forecasting]]", "[[2022-li-light-steel-housing-anp]]"]
status: solid
---

# 5 種研究方法比較

## 比較目的
用 wiki 中的 5 篇研究，說明不同研究問題適合不同方法。這頁是「研究方法入門」教學簡報的主要依據。

## 對照表

| 研究問題 | 方法 | 例子 | 資料 | 能回答 | 不能回答 |
|---|---|---|---|---|---|
| 有沒有效果？ | 準實驗：方案設置評估（[[program-placement-evaluation]]） | Hamid et al. 2011 | 329 戶家戶調查，比較有、無方案的鄰近地區 | 方案和結果的關係，比較接近因果 | 完全排除設置偏誤 |
| 哪些因素有關？ | 迴歸分析（[[regression-analysis]]） | Cull et al. 2007 | 49 國 124 家機構的橫斷面資料 | 多個因素同時的相關、取捨 | 因果（見 [[correlation-vs-causation]]） |
| 換一種做法會怎樣？ | 個案研究與模擬（[[case-study-and-simulation]]） | Popova & Simkins 2015 | 3 家公司年報中的避險部位 | 具體影響有多大、細節 | 推論到所有公司 |
| 未來會怎樣？ | ARIMA 時間序列（[[arima-time-series]]） | Mondal et al. 2014 | 56 檔股票的歷史股價 | 短期預測 | 為什麼會變動 |
| 該怎麼選？ | AHP／ANP（[[ahp-anp]]） | 李婉綾 2022 | 問卷：民眾 182 份、專家 8 份 | 準則的相對重要性 | 客觀上哪個方案最好 |

來源：[[2011-hamid-micro-health-insurance-poverty-bangladesh]]、[[2007-cull-financial-performance-outreach-microbanks]]、[[2015-popova-otc-vs-exchange-traded-derivatives]]、[[2014-mondal-arima-stock-forecasting]]、[[2022-li-light-steel-housing-anp]]

## 分析
1. **先問問題，再選方法**：同樣是金融主題，問「有沒有效」和問「未來多少」，需要完全不同的方法。
2. **資料決定可行性**：OTC 合約資料難取得，所以 [[2015-popova-otc-vs-exchange-traded-derivatives]] 只能用個案；[[2007-cull-financial-performance-outreach-microbanks]] 有統一的跨國資料庫，才能做迴歸。
3. **每種方法都有作者自己承認的限制**：[[2007-cull-financial-performance-outreach-microbanks]] 說只描述相關；[[2011-hamid-micro-health-insurance-poverty-bangladesh]] 承認可能有設置偏誤；[[2022-li-light-steel-housing-anp]] 有 36% 的有效問卷沒通過一致性檢定（[[2022-li-light-steel-housing-anp]]）。
4. **評估標準要合理**：[[2014-mondal-arima-stock-forecasting]] 的高準確度沒有和簡單基準比較，讀者要自己判斷（[[2014-mondal-arima-stock-forecasting]]）。

## 結論：怎麼選方法
- 想知道**因果** → 盡量找準實驗或實驗設計。
- 想知道**哪些因素一起變動** → 迴歸，但不要說成因果。
- 只有**少數案例**但需要細節 → 個案研究加模擬。
- 要**預測數字** → 時間序列，並和簡單基準比較。
- 要**做決策**、沒有客觀資料 → AHP／ANP，並檢查一致性。
