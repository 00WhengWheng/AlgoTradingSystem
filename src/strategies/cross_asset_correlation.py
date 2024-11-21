def cross_asset_correlation(asset1, asset2, window=30):
    """
    Cross-Asset Correlation Trading Strategy.
    
    :param asset1: pd.Series of returns or prices for Asset 1.
    :param asset2: pd.Series of returns or prices for Asset 2.
    :param window: Rolling window for calculating correlation.
    :return: Correlation and trading signals.
    """
    correlation = asset1.rolling(window).corr(asset2)
    
    signals = correlation.apply(
        lambda x: "Trade Long" if x < 0.2 else "Trade Short" if x > 0.8 else "Hold"
    )
    
    return pd.DataFrame({
        "Correlation": correlation,
        "Signal": signals
    })
