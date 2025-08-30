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

## Key Findings (example placeholders)
- TikTok showed the **highest ROAS** in early March driven by lower CPC.
- Google had the **most stable CTR**, suitable for always-on acquisition.
- Facebook performed better on **mobile placements**; desktop had higher CPC.

> Replace these with your real insights after running the notebook.

## Recommendations (examples)
- Reallocate 10–15% budget from low-ROAS adsets to top-performing channels.
- Run A/B tests on creatives in low-CTR segments (country-device pairs).
- Introduce country-specific CPA targets with weekly reviews.

## Artifacts
- Notebook: `notebooks/01_campaign_performance.ipynb`
- Visuals: add PNG exports to `/visuals` and embed below.
