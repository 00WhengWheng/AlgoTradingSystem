import pandas as pd

def keltner_channel(prices, high, low, atr_window=14, multiplier=2):
    """
    Keltner Channel Strategy.

    :param prices: pd.Series of closing prices.
    :param high: pd.Series of high prices.
    :param low: pd.Series of low prices.
    :param atr_window: Lookback period for ATR calculation.
    :param multiplier: Multiplier for channel width based on ATR.
    :return: pd.DataFrame with Keltner Channel and signals.
    """
    # Calculate Average True Range (ATR)
    tr = pd.concat([high - low, (high - prices.shift(1)).abs(), (low - prices.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(window=atr_window).mean()

    # Calculate Keltner Channel
    middle_band = prices.rolling(window=atr_window).mean()
    upper_band = middle_band + (multiplier * atr)
    lower_band = middle_band - (multiplier * atr)

    # Generate signals
    signals = pd.Series("Hold", index=prices.index)
    signals[prices > upper_band] = "Sell"
    signals[prices < lower_band] = "Buy"

    return pd.DataFrame({
        "Price": prices,
        "Middle Band": middle_band,
        "Upper Band": upper_band,
        "Lower Band": lower_band,
        "Signal": signals
    })
