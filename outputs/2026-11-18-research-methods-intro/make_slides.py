#!/usr/bin/env python3
"""
產生「研究方法入門」教學簡報（CLAUDE.md 4.6 的 N4、N5 節點）。
同一份 SLIDES 資料同時輸出 slides-outline.md 與 slides.html，避免大綱和簡報不一致。
用法：python outputs/2026-11-18-research-methods-intro/make_slides.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TEMPLATE = ROOT / "templates" / "slides-template.html"
TITLE = "研究方法入門"
W = "../../wiki/"   # 網站上 slides.html 到 wiki 頁面的相對路徑

# 每張投影片：kind（cover/section/content/quiz/refs）、src（wiki 頁面）、outline（大綱重點）、html、notes
SLIDES = [
dict(kind="cover", src="none", title="研究方法入門", outline=["副標：用 5 篇論文看 5 種研究方法"], html="""
<h1>研究方法入門<br><span style="font-size:30px;font-weight:400;color:var(--ink-2)">用 5 篇論文看 5 種研究方法</span></h1>
<div class="meta">教學簡報 · 內容全部來自研究 Wiki 知識庫<br>2026-11-18</div>""",
notes="開場：今天不背公式，而是學會「看到一個問題，知道該用什麼方法」。"),

dict(kind="content", src="research-methods-comparison", title="同一個領域，5 種不同的問題",
outline=["5 個問題對應 5 種方法", "學完能判斷：該用什麼方法、能說明什麼、不能說明什麼"], html="""
<h2>同一個領域，5 種不同的問題</h2><p class="lead">研究方法不是先選好的工具，而是由「你想回答什麼」決定</p>
<table class="qmap">
<tr><th>你想問</th><th>適合的方法</th><th>本堂例子</th></tr>
<tr><td>❶ 這個方案<b>有沒有效果</b>？</td><td>準實驗設計</td><td>微型健康保險與貧窮</td></tr>
<tr><td>❷ <b>哪些因素</b>和結果有關？</td><td>迴歸分析</td><td>微型金融機構的獲利</td></tr>
<tr><td>❸ <b>換一種做法</b>會怎樣？</td><td>個案研究與模擬</td><td>企業避險工具</td></tr>
<tr><td>❹ <b>未來</b>會怎樣？</td><td>時間序列</td><td>股價預測</td></tr>
<tr><td>❺ 多個條件下<b>該怎麼選</b>？</td><td>多準則決策</td><td>小型住宅選擇</td></tr>
</table>
<div class="goal">🎯 學完你能做到：遇到一個研究問題，說出該用哪種方法，以及這種方法<b>能說明什麼、不能說明什麼</b></div>""",
notes="用這張表當地圖，後面每個單元都會回到這裡。"),

dict(kind="section", src="none", title="單元一：有沒有效果？", outline=["準實驗設計"], html="""
<div class="no">單元 1 / 5</div><h1>這個方案有沒有效果？</h1><p class="sub">方法：準實驗設計（方案設置評估）</p>""", notes=""),

dict(kind="content", src="program-placement-evaluation,2011-hamid-micro-health-insurance-poverty-bangladesh",
title="準實驗：找一個「幾乎一樣」的對照組",
outline=["問題：微型健康保險能減少貧窮嗎？", "比較已設置 ≥ 5 年和即將設置的鄰近地區，329 戶", "用「設置」而非「參與」，避開自我選擇", "結果：只有糧食充足度顯著（0.355，10%）"], html="""
<h2>準實驗：找一個「幾乎一樣」的對照組</h2><p class="lead">例子：孟加拉的微型健康保險能減少貧窮嗎？（Hamid et al. 2011）</p>
<div class="body"><div class="col">
<div class="flow2"><div class="grp a"><b>方案區</b><span>健康保險已設置 ≥ 5 年</span></div><div class="vs">vs</div><div class="grp b"><b>對照區</b><span>相鄰地區、即將設置</span></div></div>
<ul class="pts" style="margin-top:22px"><li>為什麼不直接比「有投保 vs 沒投保」的人？<br><span class="dim">因為會投保的人可能本來就不同（自我選擇）</span></li>
<li>所以改比較<b>地區</b>，共調查 329 戶</li></ul></div>
<div class="col"><table><tr><th>結果指標</th><th class="n">係數</th><th>顯著？</th></tr>
<tr><td>所得</td><td class="n">0.080</td><td>否</td></tr><tr><td>資產</td><td class="n">0.096</td><td>否</td></tr>
<tr class="hl"><td>糧食充足度</td><td class="n">0.355</td><td>是（10%）</td></tr><tr><td>在貧窮線以上</td><td class="n">0.202</td><td>否</td></tr></table>
<div class="key">💡 重點：準實驗比單純比較更接近因果，但仍可能有設置偏誤</div></div></div>""",
notes="強調「對照組要盡量相似」是因果推論的核心。"),

dict(kind="section", src="none", title="單元二：哪些因素有關？", outline=["迴歸分析"], html="""
<div class="no">單元 2 / 5</div><h1>哪些因素和結果有關？</h1><p class="sub">方法：迴歸分析</p>""", notes=""),

dict(kind="content", src="regression-analysis,2007-cull-financial-performance-outreach-microbanks",
title="迴歸：同時看很多因素",
outline=["方程式與係數的意思", "例子：49 國、124 家微型金融機構", "收益率係數 0.964、1% 顯著", "怎麼讀星號"], html="""
<h2>迴歸：同時看很多因素</h2><p class="lead">例子：微型金融機構為什麼有的賺錢、有的不賺？（Cull et al. 2007，49 國、124 家機構）</p>
<div class="math">$$\\underbrace{y_i}_{\\text{獲利}}=\\alpha+\\beta_1\\underbrace{x_{1i}}_{\\text{利率}}+\\beta_2\\underbrace{x_{2i}}_{\\text{成本}}+\\dots+\\varepsilon_i$$</div>
<div class="body"><div class="col"><ul class="pts">
<li><b>係數 $\\beta$</b>：其他條件不變時，$x$ 多 1 單位，$y$ 平均變多少</li>
<li><b>星號</b>：* 10%、** 5%、*** 1%，星號越多越不像巧合</li>
<li><b>控制變數</b>：放進年齡、規模、地區，才能「在其他條件相同時」比較</li></ul></div>
<div class="col"><div class="card1"><div class="v">0.964<sup>***</sup></div><div class="l">個人放款機構：利率越高，財務自足率越高</div></div></div></div>""",
notes="先讓學生看懂一個係數，再談限制。"),

dict(kind="content", src="group-lending,2007-cull-financial-performance-outreach-microbanks,interaction-and-nonlinear-terms",
title="迴歸發現的取捨",
outline=["三種放款方式的平均貸款與女性比例", "越服務窮人的方式越依賴補貼", "獲利在年利率約 60% 趨平（平方項）"], html="""
<h2>迴歸發現的取捨</h2><p class="lead">越服務窮人的放款方式，越難賺錢</p>
<div class="body"><div class="col"><p class="lab">平均貸款金額（美元，越小代表客戶越窮）</p>
<div class="bars">
<div class="bar"><span>個人放款</span><div class="t"><i style="width:100%"></i></div><span class="v">1,220</span></div>
<div class="bar" style="--c:var(--c3)"><span>團體連帶</span><div class="t"><i style="width:35.3%"></i></div><span class="v">431</span></div>
<div class="bar" style="--c:var(--c2)"><span>村落銀行</span><div class="t"><i style="width:12.2%"></i></div><span class="v">149</span></div></div>
<p class="lab" style="margin-top:22px">女性借款人比例</p>
<div class="bars">
<div class="bar"><span>個人放款</span><div class="t"><i style="width:46%"></i></div><span class="v">46%</span></div>
<div class="bar" style="--c:var(--c3)"><span>團體連帶</span><div class="t"><i style="width:75%"></i></div><span class="v">75%</span></div>
<div class="bar" style="--c:var(--c2)"><span>村落銀行</span><div class="t"><i style="width:88%"></i></div><span class="v">88%</span></div></div></div>
<div class="col"><div class="note">📈 <b>平方項</b>讓迴歸可以描述「先升後平」：個人放款機構的獲利隨利率上升，但在年利率約 60% 附近趨平</div>
<div class="key" style="margin-top:20px">💡 迴歸擅長描述「哪些因素一起變動」</div></div></div>""",
notes="這頁讓學生看到迴歸的產出長什麼樣子。"),

dict(kind="content", src="correlation-vs-causation,2007-cull-financial-performance-outreach-microbanks,2011-hamid-micro-health-insurance-poverty-bangladesh",
title="小心：相關不等於因果",
outline=["三個原因：遺漏變數、反向因果、自我選擇", "Cull 作者自己說只描述相關", "對照 Hamid 的準實驗"], html="""
<h2>小心：相關不等於因果</h2><p class="lead">兩件事一起變動，不代表其中一個造成另一個</p>
<div class="grid3">
<div class="card" style="--c:var(--primary)"><h3>遺漏變數</h3><p>有第三個因素同時影響兩者</p></div>
<div class="card" style="--c:var(--c3)"><h3>反向因果</h3><p>其實是結果影響了原因</p></div>
<div class="card" style="--c:var(--c2)"><h3>自我選擇</h3><p>參加的人本來就不一樣</p></div></div>
<table style="margin-top:26px"><tr><th></th><th>Cull et al.（迴歸）</th><th>Hamid et al.（準實驗）</th></tr>
<tr><td>怎麼處理因果</td><td>作者明說：只描述相關</td><td>找相似的對照區，試圖接近因果</td></tr>
<tr><td>作者承認的限制</td><td>可能是客戶特性或反向因果</td><td>仍可能有設置偏誤</td></tr></table>
<div class="key">💡 想更接近因果：用準實驗找相似的對照組，或用隨機實驗（wiki 尚無來源，見延伸閱讀）</div>""",
notes="這是整堂課最重要的觀念之一。"),

dict(kind="section", src="none", title="單元三：換一種做法會怎樣？", outline=["個案研究與模擬"], html="""
<div class="no">單元 3 / 5</div><h1>換一種做法會怎樣？</h1><p class="sub">方法：個案研究與反事實模擬</p>""", notes=""),

dict(kind="content", src="case-study-and-simulation,2015-popova-otc-vs-exchange-traded-derivatives",
title="個案模擬：用真實資料重算「如果」",
outline=["問題：企業若只能用交易所期貨避險會怎樣？", "3 家公司的模擬結果", "限制：案例少、委託單位"], html="""
<h2>個案模擬：用真實資料重算「如果」</h2><p class="lead">例子：如果企業不能用量身訂做的店頭（OTC）合約、只能用交易所期貨避險？（Popova & Simkins 2015）</p>
<table><tr><th>公司</th><th>原本的做法</th><th>模擬：改用交易所期貨</th></tr>
<tr><td>FMC</td><td>天然氣 OTC 年度合約</td><td>要多繳 649,854 至 2,166,180 美元保證金</td></tr>
<tr><td>Hilton</td><td>利率交換</td><td>要管理 7,532 口期貨</td></tr>
<tr><td>Worthington</td><td>利率交換</td><td>每股盈餘波動增加 3.39%</td></tr></table>
<p class="dim" style="margin-top:14px;font-size:18px">做法：從年報找出真實的避險部位 → 算出要幾口期貨才能複製 → 用每日市價算保證金與盈餘波動</p>
<div class="body" style="margin-top:16px"><div class="col"><div class="key">💡 適合：資料難取得（OTC 合約是私下簽訂）、需要細節的主題</div></div>
<div class="col"><div class="warn">⚠️ 限制：只有 3 家公司，難以推論到所有企業；研究由衍生品交易商協會（ISDA）委託</div></div></div>""",
notes="提醒學生看研究也要看是誰出資。"),

dict(kind="section", src="none", title="單元四：未來會怎樣？", outline=["時間序列"], html="""
<div class="no">單元 4 / 5</div><h1>未來會怎樣？</h1><p class="sub">方法：ARIMA 時間序列</p>""", notes=""),

dict(kind="content", src="arima-time-series,model-selection-aic,2014-mondal-arima-stock-forecasting",
title="ARIMA：用過去預測未來",
outline=["p、d、q 的意思", "Box-Jenkins 四步驟、AICc 選模型", "7 個產業準確度都在 85% 以上", "注意：沒和簡單基準比較"], html="""
<h2>ARIMA：用過去預測未來</h2><p class="lead">例子：預測 56 檔印度股票未來 30 天的價格（Mondal et al. 2014）</p>
<div class="body"><div class="col">
<div class="steps"><div><b>辨識</b><span>試幾組 $p,d,q$，選 AICc 最小</span></div><div><b>估計</b><span>算出係數</span></div><div><b>檢查</b><span>殘差沒有規律</span></div><div><b>預測</b><span>和實際值比較</span></div></div>
<p class="dim" style="margin-top:14px;font-size:17px">$p$：用過去幾期的值｜$d$：差分幾次去掉趨勢｜$q$：用過去幾期的誤差</p>
<div class="key" style="margin-top:16px">例：Emami 公司試了 9 組參數，ARIMA(1,0,2) 的 AICc 為 −2175.97 最小，所以選它</div></div>
<div class="col"><p class="lab">各產業預測準確度</p><div class="bars sm">
<div class="bar"><span>民生消費</span><div class="t"><i style="width:95.93%"></i></div><span class="v">95.93%</span></div>
<div class="bar" style="--c:var(--c2)"><span>電力</span><div class="t"><i style="width:92.28%"></i></div><span class="v">92.28%</span></div>
<div class="bar" style="--c:var(--c3)"><span>汽車</span><div class="t"><i style="width:87.89%"></i></div><span class="v">87.89%</span></div></div>
<div class="warn" style="margin-top:18px">⚠️ 沒有和「明天＝今天」這種簡單預測比較，高準確度不代表能賺錢</div></div></div>""",
notes="讓學生學會質疑「準確度」的比較基準。"),

dict(kind="section", src="none", title="單元五：該怎麼選？", outline=["多準則決策"], html="""
<div class="no">單元 5 / 5</div><h1>多個條件下該怎麼選？</h1><p class="sub">方法：AHP／ANP 多準則決策</p>""", notes=""),

dict(kind="content", src="ahp-anp,2022-li-light-steel-housing-anp",
title="AHP／ANP：一次只比兩個",
outline=["1–9 點尺度兩兩比較", "一致性檢定 CR ≤ 0.1", "民眾最看重建築維護 0.1267；專家最看重造價預算 0.1858", "只有 64% 問卷通過一致性檢定"], html="""
<h2>AHP／ANP：一次只比兩個</h2><p class="lead">例子：民眾選小型住宅最看重什麼？（李婉綾 2022）</p>
<div class="body"><div class="col">
<div class="pair">「維護」和「造價」哪個重要？重要多少？<div class="scale"><span>1<br>同等</span><span>3<br>稍微</span><span>5<br>頗為</span><span>7<br>極為</span><span>9<br>絕對</span></div></div>
<div class="math" style="font-size:20px;margin-top:18px">$$CR=\\frac{CI}{RI}\\le 0.1$$</div>
<p class="dim" style="font-size:16px">一致性檢定：答案前後矛盾（A&gt;B、B&gt;C 卻 C&gt;A）的問卷要排除</p></div>
<div class="col"><table><tr><th>誰</th><th>最看重</th><th class="n">權重</th></tr>
<tr><td>民眾</td><td>建築維護</td><td class="n">0.1267</td></tr><tr><td>專家（考慮相互影響）</td><td>造價預算</td><td class="n">0.1858</td></tr></table>
<div class="card1" style="margin-top:18px;--c:var(--c3)"><div class="v">64%</div><div class="l">283 份有效問卷中，只有 182 份通過一致性檢定</div></div></div></div>""",
notes="AHP 的結果是「偏好」，不是客觀事實。"),

dict(kind="content", src="research-methods-comparison", title="總結：5 種方法一張表",
outline=["對照表：能回答／不能回答"], html="""
<h2>總結：5 種方法一張表</h2>
<table class="sum"><tr><th>方法</th><th>用的資料</th><th>能回答</th><th>不能回答</th></tr>
<tr><td><b>準實驗</b></td><td>329 戶家戶調查</td><td>方案和結果的關係，比較接近因果</td><td>完全排除設置偏誤</td></tr>
<tr><td><b>迴歸</b></td><td>49 國 124 家機構</td><td>多個因素同時的相關、取捨</td><td>因果</td></tr>
<tr><td><b>個案模擬</b></td><td>3 家公司年報</td><td>具體影響有多大、細節</td><td>推論到所有公司</td></tr>
<tr><td><b>時間序列</b></td><td>56 檔股票股價</td><td>短期預測</td><td>為什麼會變動</td></tr>
<tr><td><b>AHP／ANP</b></td><td>民眾 182 份、專家 8 份問卷</td><td>準則的相對重要性</td><td>客觀上哪個方案最好</td></tr></table>
<p class="dim" style="margin-top:16px;font-size:18px">每種方法的限制，都是原作者自己在論文中承認的</p>""",
notes="請學生遮住右欄，自己說說看每種方法的限制。"),

dict(kind="content", src="research-methods-comparison", title="怎麼選方法？",
outline=["想知道因果→準實驗", "哪些因素一起變動→迴歸", "少數案例要細節→個案", "預測→時間序列並比基準", "做決策→AHP 並檢查一致性"], html="""
<h2>怎麼選方法？</h2><p class="lead">先問問題，再看手上有什麼資料</p>
<div class="choose">
<div><span class="q">想知道「是不是它造成的」</span><span class="a">準實驗／實驗</span></div>
<div><span class="q">想知道「哪些因素一起變動」</span><span class="a">迴歸（別說成因果）</span></div>
<div><span class="q">只有少數案例，但需要細節</span><span class="a">個案研究＋模擬</span></div>
<div><span class="q">要預測未來的數字</span><span class="a">時間序列（要和簡單基準比）</span></div>
<div><span class="q">要做決策，沒有客觀資料</span><span class="a">AHP／ANP（要檢查一致性）</span></div></div>""",
notes="這張是帶走用的速查卡。"),

dict(kind="quiz", src="none", title="小測驗",
outline=["Q1 想知道新政策是否「造成」改變→準實驗", "Q2 迴歸係數顯著代表？→相關", "Q3 預測準確度 90% 先問什麼？→和簡單基準比"], html="""
<h2>小測驗：點選答案</h2>
<div class="quiz">
<div class="qz" data-ans="b"><p>Q1　想知道新的補助政策是不是「造成」農民所得增加，最適合？</p>
<button data-k="a">迴歸分析</button><button data-k="b">準實驗（找相似的對照組）</button><button data-k="c">AHP</button><span class="fb"></span></div>
<div class="qz" data-ans="a"><p>Q2　迴歸中「利率」的係數顯著為正，代表什麼？</p>
<button data-k="a">利率和獲利一起變動（相關）</button><button data-k="b">提高利率一定會增加獲利</button><button data-k="c">利率是獲利唯一的原因</button><span class="fb"></span></div>
<div class="qz" data-ans="c"><p>Q3　有人說他的模型預測股價「準確度 90%」，你應該先問？</p>
<button data-k="a">用了什麼軟體</button><button data-k="b">資料有多少筆</button><button data-k="c">和「明天＝今天」的簡單預測相比如何</button><span class="fb"></span></div></div>""",
notes="可以讓學生舉手投票再點答案。"),

dict(kind="refs", src="none", title="延伸閱讀", outline=["wiki 頁面連結"], html=f"""
<h2>延伸閱讀：研究 Wiki 頁面</h2><p class="lead">每頁的內容都來自這些 wiki 頁面，點了可以看完整說明與原文出處</p>
<div class="refgrid">
<a href="{W}research-methods-comparison.html">5 種研究方法比較</a>
<a href="{W}program-placement-evaluation.html">方案設置評估（準實驗）</a>
<a href="{W}regression-analysis.html">迴歸分析</a>
<a href="{W}correlation-vs-causation.html">相關不等於因果</a>
<a href="{W}case-study-and-simulation.html">個案研究與模擬</a>
<a href="{W}arima-time-series.html">ARIMA 時間序列</a>
<a href="{W}model-selection-aic.html">AIC 模型選擇</a>
<a href="{W}ahp-anp.html">AHP 與 ANP</a></div>
<p class="dim" style="margin-top:22px">wiki 還沒有隨機實驗（RCT）的來源，已列入開放問題，之後匯入</p>""", notes=""),
]

EXTRA_CSS = """<style>
.lead{margin-bottom:22px}
.sub{font-size:22px;opacity:.8;margin-top:10px}
.dim{color:var(--ink-3)}
.lab{font-size:15px;color:var(--ink-2);margin-bottom:10px}
table.qmap td,table.qmap th{padding:9px 14px}
.goal{margin-top:22px;background:var(--tint);padding:14px 20px;font-size:18px;color:var(--ink-2)}
.key{background:var(--tint);border-left:3px solid var(--primary);padding:12px 18px;font-size:17px;color:var(--ink);margin-top:18px}
.warn{background:#F3ECE6;border-left:3px solid #A0705A;padding:12px 18px;font-size:16px;color:var(--ink-2)}
.flow2{display:flex;align-items:stretch;gap:14px}
.grp{flex:1;background:var(--surface);border-top:3px solid var(--c);padding:16px 18px}
.grp b{display:block;font-size:20px}.grp span{font-size:15px;color:var(--ink-2)}
.grp.a{--c:var(--primary)}.grp.b{--c:var(--c2)}
.vs{align-self:center;color:var(--ink-3);font-size:18px}
.card1{background:var(--surface);border-top:3px solid var(--c,var(--primary));padding:22px 24px}
.card1 .v{font-size:46px;font-weight:600}.card1 .l{font-size:16px;color:var(--ink-2);margin-top:4px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:var(--surface);border-top:3px solid var(--c);padding:18px 22px}
.card h3{font-size:20px;margin-bottom:6px}.card p{font-size:16px;color:var(--ink-2)}
.steps{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.steps div{background:var(--surface);border-left:3px solid var(--c2);padding:12px 16px}
.steps b{display:block;font-size:18px}.steps span{font-size:15px;color:var(--ink-2)}
.bars.sm .bar{grid-template-columns:90px 1fr 80px}
.pair{background:var(--surface);padding:18px 20px;font-size:18px}
.scale{display:flex;justify-content:space-between;margin-top:12px;font-size:14px;color:var(--ink-2);text-align:center}
.scale span{flex:1;border-top:3px solid var(--c4);padding-top:6px}
table.sum td{padding:12px 14px;font-size:18px}
.choose{display:flex;flex-direction:column;gap:12px}
.choose div{display:grid;grid-template-columns:1fr auto 300px;align-items:center;background:var(--surface);padding:14px 20px;font-size:19px}
.choose div::after{content:"→";grid-column:2;grid-row:1;color:var(--ink-3);padding:0 18px}
.choose .q{grid-column:1}.choose .a{grid-column:3;font-weight:600;color:var(--primary)}
.quiz{display:flex;flex-direction:column;gap:18px}
.qz p{font-size:19px;margin-bottom:8px}
.qz button{font:inherit;font-size:16px;background:var(--surface);border:1px solid var(--line);padding:7px 14px;margin:0 8px 6px 0;cursor:pointer;color:var(--ink)}
.qz button:hover{border-color:var(--primary)}
.qz button.ok{background:#E3EAE1;border-color:#6B7F6A}.qz button.no{background:#F3E4DE;border-color:#A0705A}
.qz .fb{font-size:15px;color:var(--ink-2);margin-left:6px}
.refgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.refgrid a{display:block;background:var(--surface);border-left:3px solid var(--primary);padding:12px 18px;font-size:18px;color:var(--ink);text-decoration:none}
.refgrid a:hover{background:var(--tint)}
/* 第 3 輪修正（G4 W1）：教學投影用，放大字級與間距 */
.lead{font-size:21px;margin-bottom:26px}
table{font-size:21px}th,td{padding:13px 16px}
table.qmap td,table.qmap th{padding:13px 16px}table.sum td{padding:16px 16px;font-size:21px}
ul.pts{font-size:23px;line-height:1.75}
.goal,.key{font-size:20px;padding:16px 22px}.warn{font-size:19px;padding:16px 22px}
.bars{gap:22px}.bar{font-size:19px;grid-template-columns:120px 1fr 86px}.bar .t{height:36px}
.bars.sm .bar{grid-template-columns:100px 1fr 90px}
.grp{padding:20px 22px}.grp b{font-size:23px}.grp span{font-size:17px}
.card{padding:24px 26px}.card h3{font-size:23px}.card p{font-size:18px}
.card1{padding:28px}.card1 .v{font-size:56px}.card1 .l{font-size:18px}
.steps{gap:16px}.steps div{padding:18px 20px}.steps b{font-size:21px}.steps span{font-size:17px}
.pair{font-size:21px;padding:22px 24px}.scale{font-size:16px}
.choose{gap:16px}.choose div{font-size:22px;padding:18px 24px;grid-template-columns:1fr auto 340px}
.qz p{font-size:22px;margin-bottom:12px}.qz button{font-size:18px;padding:10px 18px}.quiz{gap:30px}
.refgrid{gap:16px}.refgrid a{font-size:20px;padding:16px 22px}
.math{padding:28px 32px}
</style>
<script>
document.addEventListener('click',e=>{const b=e.target.closest('.qz button');if(!b)return;e.stopPropagation();
const q=b.closest('.qz');const ok=b.dataset.k===q.dataset.ans;
q.querySelectorAll('button').forEach(x=>x.classList.remove('ok','no'));b.classList.add(ok?'ok':'no');
q.querySelector('.fb').textContent=ok?'答對了！':'再想想看';},true);
</script>"""


def section_html(s):
    cls = {"cover": "cover", "section": "section"}.get(s["kind"], "")
    foot = f'<div class="foot"><span>{TITLE}</span><span></span></div>'
    notes = f'<div class="notes">{s["notes"]}</div>' if s["notes"] else ""
    return f'<section class="slide {cls}" data-src="{s["src"]}">{s["html"]}{foot}{notes}</section>\n'


def outline_md():
    out = [f"---\ntype: slides-outline\nbased_on: notes.md\nstyle: C（暖灰褐）\nslides: {len(SLIDES)}\n---\n",
           f"# 簡報逐頁內容：{TITLE}\n",
           "> 由 make_slides.py 產生（與 slides.html 同一份資料）。每頁的「出處」是 G3 對應閘的檢查依據。\n"]
    for i, s in enumerate(SLIDES, 1):
        out.append(f"## {i}｜{s['title']}")
        out += [f"- {o}" for o in s["outline"]]
        src = "無（" + {"cover": "封面", "section": "章節頁", "quiz": "測驗頁", "refs": "延伸閱讀"}.get(s["kind"], "") + "）" \
            if s["src"] == "none" else "、".join(f"[[{p}]]" for p in s["src"].split(","))
        out.append(f"- **出處**：{src}")
        if s["notes"]:
            out.append(f"- **講者備註**：{s['notes']}")
        out.append("")
    return "\n".join(out)


def main():
    tpl = TEMPLATE.read_text(encoding="utf-8")
    head = tpl[:tpl.index('<div class="deck" id="deck">')]
    tail = tpl[tpl.index('</div>\n<div id="notesPane">'):]
    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head)
    head = head.replace("</head>", EXTRA_CSS + "</head>")
    deck = '<div class="deck" id="deck">\n' + "".join(section_html(s) for s in SLIDES)
    (HERE / "slides.html").write_text(head + deck + tail, encoding="utf-8")
    (HERE / "slides-outline.md").write_text(outline_md(), encoding="utf-8")
    print(f"產生 {len(SLIDES)} 頁：slides.html、slides-outline.md")


if __name__ == "__main__":
    main()
