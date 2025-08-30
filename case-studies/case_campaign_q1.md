# Case Study: Q1 Campaign Performance (Dummy Data)

**Objective:** Evaluate paid media efficiency across channels (Facebook, Google, TikTok) using key metrics (CTR, CPC, CPA, ROAS).

## Dataset
- Source: `/data/campaign/campaign_q1_2025.csv` (synthetic)
- Granularity: Daily, per campaign/adset/ad, with country, device, and placement

## Method
1. Data prep (null handling, derived metrics)
2. Aggregation by channel and time
3. Trend & distribution charts
4. Insights + recommendations

## Key Findings
- Overall CTR averaged ~[5.01]% in Q1 (range [min2.07]%–[max17.77]%), with a [upward/downward/flat] trend across the quarter.
- March outperformed January by ~[Δ0.12%] (avg CTR [Mar5.11]% vs [Jan5.23]%), suggesting positive impact from [new creative/bid changes/targeting tweak].
- Top spike(s) on [2025-03-02, 2025-01-02] reached [peak0.177689]% CTR; investigate what changed on those days to replicate.
- Volatility is [low/medium/high] (stdev [s2.31]%; coeff. of variation [cv46.2]%). Plan A/B tests to stabilize performance.

- **Under-performing dips** (bottom-quartile, ~≤ mid-3% CTR) occurred on **2025-01-18 (2.07%)**, **2025-03-05 (2.12%)**, and **2025-03-10 (2.37%)**. Pause/rotate weak adsets/creatives on these segments and rebalance bids.

## Recommendations
1. **Budget reallocation (quick win).** Shift **10–15%** from segments with **CTR < ~3.5%** and **below-median ROAS** toward proven winners; keep a small learn budget on paused sets to avoid full resets.
2. **Creative & copy A/B tests.** In the dip segments, launch **3–5 variants** (headline, visual, hook). Success criteria: **+10% CTR** or **−15% CPC** within 7–10 days; kill underperformers early.
3. **Placement & device tuning.** With **high volatility (CV = 46.2%)**, split by **device** and **placement**. Scale where CTR ≥ **avg + 1σ (~7.3%)**; cap or pause where CTR ≤ **~3.5%** for **3 consecutive days**.
4. **Bid/pacing guardrails.** Add rules: *pause* when **CTR < 3%** **or** **CPC > target**; *scale +20% daily* when **ROAS ≥ target** and spend ≥ minimum learning budget.
5. **Schedule & audience hygiene.** Review day-level patterns around **2025-01-18 / 03-05 / 03-10**; lower bids or frequency where fatigue appears (high impressions, falling CTR). Refresh audiences/negatives weekly.
6. **Insight loop.** For peak days (**2025-03-02 = 17.77% CTR**, **2025-01-02**, **2025-03-12**), document **creative, audience, placement, and bid** settings; replicate the winning combos in new adsets.

## Artifacts
- Notebook: `notebooks/01_campaign_performance.ipynb`
- **Visuals (embedded):**


[Open full-size chart](../visuals/daily_ctr.png)

![ROAS by Channel](../visuals/roas_by_channel.png)

## Metrics Dictionary
- **Impressions** — number of times ads were served.
- **Clicks** — number of ad clicks.

- **CTR (Click-Through Rate)**  
  `CTR = Clicks / Impressions`

- **CPC (Cost per Click)**  
  `CPC = Spend / Clicks`

- **CPA (Cost per Acquisition/Conversion)**  
  `CPA = Spend / Conversions`  
  > Treated as acquisition cost when “conversion” = acquisition.

- **CVR (Conversion Rate)** *(not always shown, useful for diagnostics)*  
  `CVR = Conversions / Clicks`

- **ROAS (Return on Ad Spend)**  
  `ROAS = Revenue / Spend`

- **CPM (Cost per 1,000 Impressions)** *(optional)*  
  `CPM = (Spend / Impressions) * 1000`

**Aggregation note:** Metrics are computed at daily level and/or aggregated by channel; division-by-zero is handled (NaN when denominator = 0).

## Data Caveats & Assumptions

- **Synthetic dataset.** All data are dummy/synthetic for portfolio use; patterns are realistic but not from a live account.
- **Attribution simplification.** Conversions and revenue are treated as same-day (no lag window). Multi-touch attribution, view-through, and cross-device effects are not modeled.
- **Revenue treatment.** `revenue_usd` is gross; returns, refunds, taxes, and subscription churn are not deducted—ROAS may be optimistic.
- **Currency & FX.** All values are in USD; FX effects are ignored.
- **Outliers possible.** High CTR spikes (e.g., **17.77% on 2025-03-02**) may reflect synthetic variance; in production, investigate creative/placement quality or tracking artifacts.
- **Segmentation fields.** Country (`TH, SG, MY, VN, PH, MM`), device (`iOS/Android/Desktop`), placement vary by channel; ensure apples-to-apples comparisons when benchmarking.
- **Operational guardrails.** No brand-safety filters, frequency caps, or pacing rules are encoded; apply platform best practices in real campaigns.
- **Reproducibility.** Metrics are calculated in the notebook `notebooks/01_campaign_performance.ipynb` (and helper `scripts/utils.py`). If metrics differ after edits, re-run all cells and re-export visuals.

