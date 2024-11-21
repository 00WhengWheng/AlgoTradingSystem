def adjusted_vwap(prices, volumes, slippage=0.0005):
    """
    Adjust VWAP for execution slippage.
    
    :param prices: pd.Series of intraday prices.
    :param volumes: pd.Series of intraday volumes.
    :param slippage: Execution slippage as a fraction of price.
    :return: Adjusted VWAP.
    """
    raw_vwap = (prices * volumes).sum() / volumes.sum()
    adjusted_vwap = raw_vwap * (1 + slippage)
    print(f"Adjusted VWAP: {adjusted_vwap:.2f}")
    return adjusted_vwap
