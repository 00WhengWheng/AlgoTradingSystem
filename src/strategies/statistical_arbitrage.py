
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint

def statistical_arbitrage(pair_prices, window=30, zscore_threshold=2):
    if pair_prices.shape[1] != 2:
        raise ValueError("Input DataFrame must contain exactly two columns for the pair.")
    _, p_value, _ = coint(pair_prices.iloc[:, 0], pair_prices.iloc[:, 1])
    if p_value > 0.05:
        raise ValueError("The pair is not cointegrated.")
    hedge_ratio = np.polyfit(pair_prices.iloc[:, 0], pair_prices.iloc[:, 1], 1)[0]
    spread = pair_prices.iloc[:, 1] - hedge_ratio * pair_prices.iloc[:, 0]
    rolling_mean = spread.rolling(window=window).mean()
    rolling_std = spread.rolling(window=window).std()
    zscore = (spread - rolling_mean) / rolling_std
    signals = np.where(zscore > zscore_threshold, "Short", 
                       np.where(zscore < -zscore_threshold, "Long", "Neutral"))
    return pd.DataFrame({
        "Asset1": pair_prices.iloc[:, 0],
        "Asset2": pair_prices.iloc[:, 1],
        "Spread": spread,
        "Z-Score": zscore,
        "Signal": signals
    })
