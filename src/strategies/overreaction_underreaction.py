def overreaction_underreaction_strategy(prices, threshold=0.05):
    """
    Overreaction and Underreaction Strategy.
    
    :param prices: pd.Series of price data.
    :param threshold: Percentage threshold for detecting large moves.
    :return: Trading signals.
    """
    daily_return = prices.pct_change()
    overreaction = daily_return.abs() > threshold
    
    signals = ["Buy (Rebound Expected)" if ret < 0 else "Sell (Pullback Expected)" if ret > 0 else "Hold"
               for ret, react in zip(daily_return, overreaction) if react]
    
    return pd.DataFrame({
        "Price": prices,
        "Daily Return": daily_return,
        "Signal": signals
    })
