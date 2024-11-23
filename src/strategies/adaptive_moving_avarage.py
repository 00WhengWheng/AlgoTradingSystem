import pandas as pd

def adaptive_moving_average(prices, window=10, factor=2):
    """
    Adaptive Moving Average (AMA).
    Adapts to changes in volatility and trend.

    :param prices: pd.Series of price data.
    :param window: Lookback period for volatility calculation.
    :param factor: Smoothing factor for adjusting responsiveness.
    :return: pd.Series of adaptive moving average values.
    """
    # Calculate price changes and volatility (absolute changes)
    price_change = prices.diff()
    volatility = prices.diff().rolling(window=window).std()

    # Calculate the efficiency ratio (ER)
    direction = price_change.abs().rolling(window=window).sum()
    er = direction / volatility

    # Calculate smoothing constants based on ER
    fast = 2 / (2 + 1)
    slow = 2 / (30 + 1)
    sc = (er * (fast - slow) + slow) ** 2

    # Calculate Adaptive Moving Average
    ama = pd.Series(index=prices.index, data=0)
    ama.iloc[0] = prices.iloc[0]  # Initialize AMA with the first price
    for i in range(1, len(prices)):
        ama.iloc[i] = ama.iloc[i - 1] + sc.iloc[i] * (prices.iloc[i] - ama.iloc[i - 1])

    return ama
