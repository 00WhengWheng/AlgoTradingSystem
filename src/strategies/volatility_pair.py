def volatility_pair_trading(asset1_volatility, asset2_volatility, threshold=0.1):
    """
    Volatility-Based Pair Trading Strategy.
    
    :param asset1_volatility: Series of historical volatilities for Asset 1.
    :param asset2_volatility: Series of historical volatilities for Asset 2.
    :param threshold: Volatility ratio threshold for generating signals.
    :return: Trading signals.
    """
    ratio = asset1_volatility / asset2_volatility
    mean_ratio = ratio.mean()
    
    signals = []
    for r in ratio:
        if r > mean_ratio * (1 + threshold):
            signals.append("Sell Asset 1, Buy Asset 2")
        elif r < mean_ratio * (1 - threshold):
            signals.append("Buy Asset 1, Sell Asset 2")
        else:
            signals.append("Hold")
    
    return pd.DataFrame({
        "Volatility Ratio": ratio,
        "Signal": signals
    })
