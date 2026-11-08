---
type: source
title: "Can Micro Health Insurance Reduce Poverty? Evidence From Bangladesh"
aliases: [Hamid et al. 2011, 微型健康保險能減少貧窮嗎]
authors: ["[[syed-abdul-hamid]]", "[[jennifer-roberts]]", "[[paul-mosley]]"]
year: 2011
venue: The Journal of Risk and Insurance, 78(1), 57–82
url: https://doi.org/10.1111/j.1539-6975.2010.01402.x
raw: raw/papers/2011-hamid-micro-health-insurance-poverty-bangladesh.pdf
tags: [微型保險, 健康保險, 貧窮, 孟加拉, 影響評估, 發展經濟學]
domain: 發展經濟學
created: 2026-11-08
updated: 2026-11-08
ingested: 2026-11-08
status: solid
---

# Can Micro Health Insurance Reduce Poverty? Evidence From Bangladesh

| 項目 | 內容 |
|---|---|
| 作者 | [[syed-abdul-hamid]]（達卡大學）、[[jennifer-roberts]]（里茲大學）、[[paul-mosley]]（雪菲爾大學） |
| 研究對象 | [[grameen-bank]] 透過 [[grameen-kalyan]] 經營的 MHI 方案 |
| 發表 | 2011 · *The Journal of Risk and Insurance* 78(1): 57–82 |
| DOI | 10.1111/j.1539-6975.2010.01402.x |
| 原文 | `raw/papers/2011-hamid-micro-health-insurance-poverty-bangladesh.pdf` |
| 備註 | 曾發表於第 5 屆國際微型保險研討會（塞內加爾，2009）；此研究沒有外部經費 |

## 一句話摘要
作者比較孟加拉鄉村中「已有 MHI 至少 5 年」和「沒有 MHI」的 Grameen 微型貸款地區。結果是：在微型貸款之外再加上 [[micro-health-insurance|微型健康保險（MHI）]]，和四項貧窮指標都呈正向關聯，但只有**糧食充足度**達到統計顯著（10% 水準）。

## 核心貢獻
- 第一篇直接檢驗「在 [[microcredit|微型貸款]] 上加 MHI」是否減少貧窮的實證研究。之前的 MHI 研究多半只看就醫利用、自付費用等過程指標。
- 提出一個概念架構（原文 Figure 1），說明 MHI 怎麼透過「健康改善」和「降低醫療支出的不確定性」兩條路徑影響家戶貧窮。
- 用「方案設置（placement）」而不是「個人參與（participation）」來估計效果，把外溢效果算進去（見 [[program-placement-evaluation]]）。

## 概念架構：MHI 如何影響貧窮
1. MHI 帶來健康意識提升、正式醫療利用增加，進而**改善健康狀態**。
2. 健康改善產生兩種效果：
   - **增益效果（augmenting）**：生產力提高、勞動供給增加，收入因此提高。
   - **穩定效果（stabilization）**：因病損失的工作天數減少、醫療支出降低，收入因此穩定，家戶不必借錢或變賣生產性資產。
3. **醫療支出的不確定性降低**後，家戶不需要為了預防而持有現金或高流動性資產，可以投資在報酬較高的資產上。
4. 收入超過溫飽水準後，可以投資營養、人力資本、實物資本；群組團結增強，退出微型貸款的機率降低；長期下來脫離貧窮線。

## 方法
- **資料**：2006 年的橫斷面家戶調查，共 329 戶：GB1 136 戶、GB2 85 戶、GB3 108 戶。整體回應率 73%。
- **分層**：
  - GB1：有 MHI ≥ 5 年（Madhabpur 分行，Singair 次區，1996 年起有 MHI）
  - GB2：有 MHI 1–2 年（Pakutia 分行，Nagarpur 次區，2004 年起）
  - GB3：沒有 MHI（Joy Mantap 分行，與 GB1 同在 Singair 次區、彼此相鄰，Grameen 已計畫在此設 MHI）
- **抽樣**：多階段抽樣，每區隨機抽 2 村，每村抽 2 個女性貸款中心。約 96% 的 GB 會員是女性，所以只抽女性中心。
- **估計**：設置模型 $y_{ij} = X_{ij}\beta + P_{ij}\lambda + \varepsilon_{ij}$，比較 GB1（P=1）和 GB3（P=0）。$\lambda$ 是**平均處理效果（ATE）**，不是對受處理者的效果（ATT）。GB2 只用在描述統計。
- **為什麼不用參與模型**：一是 MHI 有外溢效果（健康推廣服務涵蓋整個服務範圍內的居民，未投保者也可以付較高費用就醫，還有非正式風險分擔）；二是 GB1 的參保率高達 96%，未參保的觀察值太少。
- **控制設置偏誤的做法**：實驗區和對照區選在同一個小地理範圍；對照區是即將設置 MHI 的地區；再調查對照區居民的投保意願，GB3 有 98% 願意投保，和 GB1 實際的 96% 很接近。
- **結果變數**：
  1. 年齡與性別調整後的人均所得（取 log，OLS）
  2. 人均非土地資產（取 log，OLS）
  3. 糧食充足度（3 級 ordered probit）
  4. 是否在貧窮線以上（probit）。貧窮線用 [[cost-of-basic-needs|基本需求成本法]] 計算。
- **控制變數**：戶長教育、戶長職業等級、在海外工作的家人數、擁有的耕地、加入微型貸款的月數、家戶人數、村落主要收入來源。

## 主要結果

**描述統計（原文 Table 3，單位：美元）**

| 指標 | GB1 | GB2 | GB3 | GB1−GB3 |
|---|---|---|---|---|
| 人均所得 | 342.7 | 260.1 | 240.3 | 102.3*** |
| 人均非土地資產 | 223.5 | 142.0 | 158.2 | 65.3*** |
| 在貧窮線以上的家戶 % | 80.88 | 70.37 | 69.44 | 11.44* |
| 糧食有剩餘的家戶 % | 26.5 | 12.9 | 8.3 | 18.2（不顯著） |

**迴歸（原文 Table 4，n = 244）：MHI 設置變數的係數**

| 結果 | 係數（穩健標準誤） | 顯著性 |
|---|---|---|
| log 人均所得 | 0.080 (0.069) | 不顯著 |
| log 人均非土地資產 | 0.096 (0.162) | 不顯著 |
| 糧食充足度（ordered probit） | 0.355 (0.205) | 10% 水準顯著 |
| 在貧窮線以上（probit） | 0.202 (0.246) | 不顯著 |

- 邊際效果（原文 Table A1）：位在 MHI 已設置 5 年以上的地區，「糧食有剩餘」的機率增加 0.078，「糧食不足」的機率減少 0.117（兩者都是 10% 水準）。作者說這個效果的大小和「多一位家人在海外工作」差不多，只略小於「戶長從事高等級職業」（+0.167）。
- 戶長教育、高等級職業、海外家人、耕地面積四個變數對四項結果都一致呈正向貢獻。
- 加入微型貸款的時間對其中三項結果有正向效果。作者據此認為微型貸款減貧的效果很明確，MHI 的效果則還太新，無法下定論。

> [!question] 待確認
> 原文寫「增加 0.078 percentage points」，但 probit 邊際效果 0.078 通常解讀為機率增加 0.078（約 7.8 個百分點）。原文用詞可能有誤。

## 限制與批評
作者自己指出：
- **時間太短**：GB1 平均設置 MHI 只有約 6 年，所得和資產累積這類動態效果，用一次的橫斷面資料不容易看出來。
- **方案設計的缺陷**：只提供初級醫療，沒有二、三級醫療；轉診機制實際上沒有運作。名義上每年最多 2,000 塔卡（約 29 美元）的住院給付原本由 ILO 出資，但資金已經用完，實務上不再提供。
- **因果路徑沒有被觀察到**：GB1 和 GB3 的醫療支出、因病損失工作天數都沒有顯著差異，而這兩項正是架構中的「穩定效果」。
- **自付額太高**：自付額雖然不多，對極貧家戶仍是阻礙，他們會轉向提供賒帳的非正式醫療者，即使總花費更高（見 [[moral-hazard]]）。
- **樣本限制**：只抽微型貸款會員，無法回答 MHI 能不能觸及「最窮的窮人」。

另外（推論）：
- GB1 會員加入微型貸款的時間顯著較長（9.62 年對 6.84 年），描述統計中的所得差距有一部分可能來自微型貸款，而不是 MHI。迴歸雖然有控制這個變數，但非隨機設置的疑慮仍在。
- 只比較一個實驗分行和一個對照分行，等於地區層級只有一組對照，外部效度有限。

## 與既有知識的關係
- **延伸**：[[microcredit]] 文獻已指出健康衝擊是借款人無法脫貧的主因（Todd 1996；Wright 2000）。本文檢驗把 MHI 當成補充服務的效果。
- **延伸**：Mosley（2003）研究過 [[brac]] 的 MHI，但沒有直接檢驗貧窮，而且樣本小、時間早。
- **相關**：[[informal-risk-sharing]]。樣本中 96% 的家戶主要用當期收入或儲蓄支付醫療費，很少依賴借貸或變賣資產，所以非正式保險造成的估計偏誤可能有限。
- **理論背景**：[[insurance-demand-theory|期望效用下的保險需求]]、[[moral-hazard]]、[[adverse-selection]]。
- **方案特性**：Grameen 的 MHI 是「兩方制」，保險人本身就是醫療提供者，性質上比較接近醫療預付，而不是承保重大醫療支出的保險（見 [[micro-health-insurance]]）。

## 值得記住的引文
> "the purpose of any insurance policy is to convert an uncertain, but potentially large, loss into a certain, small loss" — Newhouse (1978)，本文引用

> "Our analyses clearly demonstrate the positive effect of microcredit in reducing poverty, while the effect of adding micro health insurance is still too new to be able to offer definitive results."

## 影響到的頁面
- 新建：[[micro-health-insurance]]、[[microinsurance]]、[[microcredit]]、[[program-placement-evaluation]]、[[informal-risk-sharing]]、[[insurance-demand-theory]]、[[moral-hazard]]、[[adverse-selection]]、[[cost-of-basic-needs]]、[[grameen-bank]]、[[grameen-kalyan]]、[[brac]]、[[syed-abdul-hamid]]、[[jennifer-roberts]]、[[paul-mosley]]、[[muhammad-yunus]]
