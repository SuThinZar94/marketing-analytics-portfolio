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

Under-performing dips below [threshold]% occurred on [list 2–3 dates]; consider pausing weak adsets/creatives or reallocating budget.

> Replace these with your real insights after running the notebook.

## Recommendations (examples)
- Reallocate 10–15% budget from low-ROAS adsets to top-performing channels.
- Run A/B tests on creatives in low-CTR segments (country-device pairs).
- Introduce country-specific CPA targets with weekly reviews.

## Artifacts
- Notebook: `notebooks/01_campaign_performance.ipynb`
- Visuals: add PNG exports to `/visuals` and embed below.


[Open full-size chart](../visuals/daily_ctr.png)
