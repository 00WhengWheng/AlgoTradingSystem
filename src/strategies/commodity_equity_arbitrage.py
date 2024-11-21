def commodity_equity_arbitrage(commodity_prices, equity_prices, window=30):
    """
    Commodity-Equity Arbitrage Strategy.
    
    :param commodity_prices: pd.Series of commodity prices.
    :param equity_prices: pd.Series of related equity prices.
    :param window: Rolling window for price ratio mean.
    :return: Trading signals based on price ratio deviations.
    """
    price_ratio = equity_prices / commodity_prices
    rolling_mean = price_ratio.rolling(window).mean()
    rolling_std = price_ratio.rolling(window).std()

    z_scores = (price_ratio - rolling_mean) / rolling_std

    signals = z_scores.apply(
        lambda x: "Buy Equity, Sell Commodity" if x < -2 else "Sell Equity, Buy Commodity" if x > 2 else "Hold"
    )

    return pd.DataFrame({
        "Price Ratio": price_ratio,
        "Z-Score": z_scores,
        "Signal": signals
    })
