---
type: research-note
question: 研究方法入門：用 5 篇論文看 5 種方法
created: 2026-11-18
wiki_pages: ["[[research-methods-comparison]]", "[[program-placement-evaluation]]", "[[regression-analysis]]", "[[interaction-and-nonlinear-terms]]", "[[correlation-vs-causation]]", "[[group-lending]]", "[[case-study-and-simulation]]", "[[arima-time-series]]", "[[model-selection-aic]]", "[[ahp-anp]]", "[[2011-hamid-micro-health-insurance-poverty-bangladesh]]", "[[2007-cull-financial-performance-outreach-microbanks]]", "[[2015-popova-otc-vs-exchange-traded-derivatives]]", "[[2014-mondal-arima-stock-forecasting]]", "[[2022-li-light-steel-housing-anp]]"]
wiki_source_count: 5
---

# 研究方法入門：用 5 篇論文看 5 種方法

> 4.6 流程的 N3 節點產出：只列 wiki 中查得到的事實，每條附出處頁。簡報（N4、N5）只能使用這份清單裡的內容。

## 教學目標
讓沒學過研究方法的人，看完能回答：「遇到一個研究問題，該用哪種方法？這種方法能說明什麼、不能說明什麼？」

## 可用事實清單

### 總覽
- 5 個研究問題對應 5 種方法：有沒有效果→準實驗；哪些因素有關→迴歸；換做法會怎樣→個案模擬；未來會怎樣→時間序列；該怎麼選→AHP／ANP（[[research-methods-comparison]]）
- 先問問題再選方法；資料決定可行性；每種方法都有作者承認的限制（[[research-methods-comparison]]）

### 單元一：準實驗（Hamid 2011）
- 比較 MHI 已設置 ≥ 5 年的地區和即將設置的鄰近地區；329 戶（[[2011-hamid-micro-health-insurance-poverty-bangladesh]]）
- 用「設置」而不是「參與」估計，是為了避開自我選擇；估計的是 ATE（[[program-placement-evaluation]]）
- 結果：糧食充足度係數 0.355，10% 水準顯著；所得、資產、貧窮線都不顯著（[[2011-hamid-micro-health-insurance-poverty-bangladesh]]）

### 單元二：迴歸（Cull 2007）
- 方程式 $y_i=\alpha+\beta_1 x_{1i}+\dots+\varepsilon_i$；係數代表其他條件不變時的平均差異（[[regression-analysis]]）
- 49 國、124 家機構；個人放款機構收益率係數 0.964、1% 顯著（[[regression-analysis]]、[[2007-cull-financial-performance-outreach-microbanks]]）
- 獲利在年利率約 60% 趨平（平方項）（[[interaction-and-nonlinear-terms]]）
- 三種放款方式平均貸款：個人 1,220、團體 431、村落銀行 149 美元；女性比例 46%、75%、88%（[[2007-cull-financial-performance-outreach-microbanks]]、[[group-lending]]）
- 作者說只描述相關；相關不等於因果的三個原因：遺漏變數、反向因果、自我選擇（[[correlation-vs-causation]]）

### 單元三：個案研究與模擬（Popova 2015）
- 3 家公司：FMC、Hilton、Worthington（[[case-study-and-simulation]]）
- Hilton 要 7,532 口期貨；FMC 要多繳 649,854 至 2,166,180 美元保證金；Worthington 每股盈餘波動增加 3.39%（[[2015-popova-otc-vs-exchange-traded-derivatives]]）
- 限制：案例少、ISDA 委託（[[case-study-and-simulation]]、[[2015-popova-otc-vs-exchange-traded-derivatives]]）

### 單元四：時間序列（Mondal 2014）
- ARIMA($p,d,q$)：用自己的過去預測未來；Box-Jenkins 四步驟：辨識、估計、檢查、預測（[[arima-time-series]]）
- AICc 越小越好；Emami 選 ARIMA(1,0,2)（[[model-selection-aic]]）
- 56 檔印度股票，7 個產業準確度都在 85% 以上；FMCG 95.93% 最高，汽車 87.89% 最低（[[2014-mondal-arima-stock-forecasting]]）
- 注意：沒和簡單基準比較，高準確度不等於能獲利（[[2014-mondal-arima-stock-forecasting]]）

### 單元五：AHP／ANP（李婉綾 2022）
- 1–9 點尺度兩兩比較；$AW=\lambda W$；$CR=CI/RI\le 0.1$（[[ahp-anp]]）
- 民眾第一名：建築維護 0.1267；專家（考慮相依性）第一名：造價預算 0.1858（[[ahp-anp]]、[[2022-li-light-steel-housing-anp]]）
- 283 份有效問卷中只有 182 份（64%）通過一致性檢定（[[ahp-anp]]）

## wiki 沒有、簡報不能講的內容
- 隨機實驗（RCT）的實例 → 列入延伸閱讀，建議日後匯入（[[questions]]）
- 機器學習預測方法 → wiki 無來源，不提
