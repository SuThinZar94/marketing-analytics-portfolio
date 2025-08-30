"""Utility functions for marketing analytics (dummy data)."""
import pandas as pd
import numpy as np

def add_basic_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['ctr'] = (df['clicks'] / df['impressions']).replace([np.inf, -np.inf], np.nan)
    df['cpc'] = (df['spend_usd'] / df['clicks']).replace([np.inf, -np.inf], np.nan)
    df['cpa'] = (df['spend_usd'] / df['conversions']).replace([np.inf, -np.inf], np.nan)
    df['roas'] = (df['revenue_usd'] / df['spend_usd']).replace([np.inf, -np.inf], np.nan)
    return df
