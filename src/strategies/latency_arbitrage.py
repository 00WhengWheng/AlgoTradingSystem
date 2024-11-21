def latency_arbitrage(price_feed1, price_feed2, transaction_cost=0.001):
    """
    Latency Arbitrage Strategy.
    
    :param price_feed1: Series of prices from Feed 1 (faster feed).
    :param price_feed2: Series of prices from Feed 2 (slower feed).
    :param transaction_cost: Cost per trade as a fraction.
    :return: Arbitrage opportunities.
    """
    opportunities = []
    for p1, p2 in zip(price_feed1, price_feed2):
        if p1 > p2 + transaction_cost:
            opportunities.append("Buy Feed 2, Sell Feed 1")
        elif p1 < p2 - transaction_cost:
            opportunities.append("Sell Feed 2, Buy Feed 1")
        else:
            opportunities.append("Hold")
    
    return pd.DataFrame({
        "Price Feed 1": price_feed1,
        "Price Feed 2": price_feed2,
        "Signal": opportunities
    })
