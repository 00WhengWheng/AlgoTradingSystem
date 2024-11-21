def dark_pool_arbitrage(dark_pool_price, public_price, transaction_cost=0.001):
    """
    Dark Pool Arbitrage Strategy.
    
    :param dark_pool_price: Price from the dark pool.
    :param public_price: Price from the public exchange.
    :param transaction_cost: Cost per transaction as a fraction.
    :return: Arbitrage opportunity details.
    """
    if dark_pool_price < public_price - transaction_cost:
        print(f"Arbitrage Opportunity: Buy in Dark Pool at {dark_pool_price}, Sell on Public Exchange at {public_price}")
        return "Buy in Dark Pool, Sell on Public Exchange"
    elif dark_pool_price > public_price + transaction_cost:
        print(f"Arbitrage Opportunity: Buy on Public Exchange at {public_price}, Sell in Dark Pool at {dark_pool_price}")
        return "Buy on Public Exchange, Sell in Dark Pool"
    else:
        print("No arbitrage opportunity found.")
        return "Hold"
