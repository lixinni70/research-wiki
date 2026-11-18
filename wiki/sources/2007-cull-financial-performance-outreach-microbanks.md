---
type: source
title: "Financial Performance and Outreach: A Global Analysis of Leading Microbanks"
aliases: [Cull et al. 2007, 微型銀行的財務績效與觸及]
authors: ["Robert Cull", "Asli Demirgüç-Kunt", "Jonathan Morduch"]
year: 2007
venue: The Economic Journal, 117 (February), F107–F133
raw: raw/papers/2007-cull-financial-performance-outreach-microbanks.pdf
tags: [微型金融, 迴歸分析, 跨國資料]
domain: 發展經濟學
method: 橫斷面 OLS 迴歸（含交互作用項、平方項）
created: 2026-11-18
updated: 2026-11-18
ingested: 2026-11-18
status: solid
---

# Financial Performance and Outreach: A Global Analysis of Leading Microbanks

| 項目 | 內容 |
|---|---|
| 作者 | Robert Cull、Asli Demirgüç-Kunt（世界銀行）、Jonathan Morduch |
| 發表 | 2007 · *The Economic Journal* 117: F107–F133 |
| 資料 | MIX（Microfinance Information Exchange）調整後的財務資料；49 國、124 家微型金融機構，1999–2002 年每家一筆，70% 是 2002 年 |
| 方法 | 橫斷面 OLS 迴歸（[[regression-analysis]]），含交互作用項與平方項（[[interaction-and-nonlinear-terms]]） |

## 一句話摘要
微型金融機構有可能同時賺錢又服務窮人，但依放款方式拆開來看會出現取捨：個人放款機構獲利最高，觸及窮人的程度最低；村落銀行最窮、最依賴補貼。

## 研究問題
1. 提高利率會不會因為逆選擇和道德風險，反而讓還款率和獲利下降？
2. 「觸及最窮的人」和「追求獲利」之間有沒有取捨？
3. 機構有沒有發生[[mission-drift|使命漂移]]，也就是為了商業化而離開較窮的客戶？

作者明確說明：關鍵變數沒有足夠的外生變異，所以**只描述相關，不估計因果**（見 [[correlation-vs-causation]]）。

## 三種放款方式（原文 Table 4）

| 指標 | 個人放款（56 家） | 團體連帶（48 家） | 村落銀行（20 家） |
|---|---|---|---|
| 財務自足率 FSS 平均 | 1.11 | 0.98 | 0.95 |
| 調整後 ROA 平均 | 0.01 | −0.05 | −0.08 |
| 平均貸款金額（美元） | 1,220 | 431 | 149 |
| 女性借款人比例 | 46% | 75% | 88% |
| 補貼占資金比例（Table 5） | 11.0% | 27.7% | 35.5% |

說明見 [[group-lending]]。財務自足率（FSS）＝調整後營業收入 ÷ 調整後（財務費用＋放款損失準備＋營業費用），小於 1 表示收入不夠支應成本。

## 迴歸模型
$$FSS_i=\alpha+\beta_1 Yield_i+\beta_2 Yield_i\times Type_i+\beta_3 Labour_i+\dots+\beta_{10}Region_i+\varepsilon_i$$

- 依變數：FSS、OSS、ROA 三種獲利指標（n = 104）。
- 交互作用項讓「利率對獲利的影響」可以依放款方式不同而不同；省略類別是個人放款機構。

## 主要結果
- **利率與獲利**：個人放款機構的實質放款收益率（Real Yield）係數為正且在 1% 水準顯著（FSS 欄 0.964）；但加入平方項後，獲利在年利率約 60% 附近趨平（Table 8、Figure 2）。團體放款機構則是 U 型關係。
- **成本**：資本成本對三種機構的獲利都是負向；控制成本後，放款方式虛擬變數本身不再顯著。
- **逾期風險**：個人放款機構的逾期比例（portfolio at risk）與收益率呈倒 U 型，在收益率約 40% 達到高點（Table 9、Figure 3）。
- **貸款規模與成本**：平均貸款金額越大，每一元的成本越低，但只到某個程度，呈 U 型（Table 10）。
- **使命漂移**（Table 11–12）：個人放款機構規模越大，平均貸款越大、借給女性的比例越低，表示觸及深度下降；但財務自足率越高的個人放款機構反而貸款越小、女性比例越高。村落銀行和團體放款機構看不到使命漂移的明顯證據。

## 限制
- 樣本是資料品質好的領先機構，不代表所有微型金融機構。
- 橫斷面資料，可能有遺漏變數或反向因果；作者自己指出利率結果也可能由「客戶特性」或「反向因果」造成。
- 用平均貸款金額代表客戶有多窮，只是代理變數。

## 與既有知識的關係
- **延伸** [[microcredit]]：從家戶層級（[[2011-hamid-micro-health-insurance-poverty-bangladesh]]）轉到機構層級。
- **方法對照**：Hamid 用[[program-placement-evaluation|方案設置評估]]試圖接近因果；Cull 用跨國迴歸描述相關。兩者的比較見 [[research-methods-comparison]]。
- **理論**：利率過高引起[[adverse-selection|逆選擇]]和[[moral-hazard|道德風險]]（Stiglitz & Weiss 1981，引自本文）。

## 影響到的頁面
[[regression-analysis]]、[[interaction-and-nonlinear-terms]]、[[correlation-vs-causation]]、[[mission-drift]]、[[group-lending]]、[[microcredit]]、[[research-methods-comparison]]
