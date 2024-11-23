import pandas as pd

def volume_weighted_momentum(prices, volumes, momentum_window=14):
    """
    Volume-Weighted Momentum Strategy.

    :param prices: pd.Series of price data.
    :param volumes: pd.Series of volume data.
    :param momentum_window: Lookback period for momentum calculation.
    :return: pd.DataFrame with volume-weighted momentum and signals.
    """
    # Calculate price momentum
    momentum = prices.diff(momentum_window)

    # Volume weighting
    volume_weighted_momentum = momentum * volumes.rolling(window=momentum_window).mean()

    # Generate signals
    signals = pd.Series("Hold", index=prices.index)
    signals[volume_weighted_momentum > 0] = "Buy"
    signals[volume_weighted_momentum < 0] = "Sell"

    return pd.DataFrame({
        "Price": prices,
        "Volume": volumes,
        "Momentum": momentum,
        "Volume-Weighted Momentum": volume_weighted_momentum,
        "Signal": signals
    })
