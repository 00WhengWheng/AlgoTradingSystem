def carbon_credit_arbitrage(market1_prices, market2_prices, transaction_cost=0.1):
    """
    Carbon Credit Arbitrage Strategy.
    
    :param market1_prices: Series of carbon credit prices in Market 1.
    :param market2_prices: Series of carbon credit prices in Market 2.
    :param transaction_cost: Cost per trade as a fraction.
    :return: Arbitrage opportunities.
    """
    spreads = market1_prices - market2_prices
    opportunities = []
    
    for spread in spreads:
        if spread > transaction_cost:
            opportunities.append("Sell Market 1, Buy Market 2")
        elif spread < -transaction_cost:
            opportunities.append("Buy Market 1, Sell Market 2")
        else:
            opportunities.append("Hold")
    
    return pd.DataFrame({
        "Price Spread": spreads,
        "Opportunity": opportunities
    })
