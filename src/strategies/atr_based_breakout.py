
import pandas as pd

def atr_based_breakout(prices, high, low, close, atr_window=14, breakout_multiplier=2):
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(window=atr_window).mean()
    upper_breakout = prices + breakout_multiplier * atr
    lower_breakout = prices - breakout_multiplier * atr
    signals = pd.Series("Hold", index=prices.index)
    signals[prices > upper_breakout] = "Buy"
    signals[prices < lower_breakout] = "Sell"
    return pd.DataFrame({
        "Price": prices,
        "ATR": atr,
        "Upper Breakout": upper_breakout,
        "Lower Breakout": lower_breakout,
        "Signal": signals
    })
