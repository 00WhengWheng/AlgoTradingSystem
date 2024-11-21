def fear_greed_trading(index_levels):
    """
    Fear and Greed Index Trading Strategy.
    
    :param index_levels: pd.Series of Fear and Greed Index levels (0–100).
    :return: Trading signals.
    """
    signals = index_levels.apply(
        lambda x: "Buy (Extreme Fear)" if x < 20 else "Sell (Extreme Greed)" if x > 80 else "Hold"
    )
    
    return pd.DataFrame({
        "Fear and Greed Index": index_levels,
        "Signal": signals
    })
