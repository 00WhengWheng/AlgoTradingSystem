
import pandas as pd

def multi_timeframe_analysis(prices, short_window=5, long_window=20):
    short_ma = prices.rolling(window=short_window).mean()
    long_ma = prices.rolling(window=long_window).mean()
    signals = pd.Series(index=prices.index, data="Neutral")
    signals[(short_ma > long_ma) & (short_ma.shift(1) <= long_ma.shift(1))] = "Buy"
    signals[(short_ma < long_ma) & (short_ma.shift(1) >= long_ma.shift(1))] = "Sell"
    return pd.DataFrame({
        "Price": prices,
        "Short MA": short_ma,
        "Long MA": long_ma,
        "Signal": signals
    })
