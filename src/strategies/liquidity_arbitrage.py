def liquidity_arbitrage(liquid_market_price, illiquid_market_price, transaction_cost=0.002):
    """
    Liquidity Arbitrage Strategy.
    
    :param liquid_market_price: Price in the liquid market.
    :param illiquid_market_price: Price in the illiquid market.
    :param transaction_cost: Cost per transaction as a fraction.
    :return: Arbitrage action.
    """
    if liquid_market_price > illiquid_market_price + transaction_cost:
        print(f"Arbitrage Opportunity: Buy in Illiquid Market at {illiquid_market_price}, Sell in Liquid Market at {liquid_market_price}")
        return "Buy in Illiquid Market, Sell in Liquid Market"
    elif liquid_market_price < illiquid_market_price - transaction_cost:
        print(f"Arbitrage Opportunity: Buy in Liquid Market at {liquid_market_price}, Sell in Illiquid Market at {illiquid_market_price}")
        return "Buy in Liquid Market, Sell in Illiquid Market"
    else:
        print("No arbitrage opportunity found.")
        return "Hold"
