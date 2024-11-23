
import pandas as pd
import numpy as np

def mean_reversion_strategy(prices, window=20, threshold=2):
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    z_scores = (prices - rolling_mean) / rolling_std
    signals = np.where(z_scores > threshold, 'Sell', np.where(z_scores < -threshold, 'Buy', 'Hold'))
    return pd.DataFrame({"Price": prices, "Rolling Mean": rolling_mean, "Z-Score": z_scores, "Signal": signals})
