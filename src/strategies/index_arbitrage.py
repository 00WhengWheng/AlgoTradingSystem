def index_arbitrage(index_price, constituent_prices, weights, transaction_cost=0.001):
    """
    Index Arbitrage Strategy.
    
    :param index_price: Current price of the index.
    :param constituent_prices: List of prices for index constituents.
    :param weights: List of weights for each constituent in the index.
    :param transaction_cost: Cost per transaction as a fraction.
    :return: Arbitrage opportunity details.
    """
    portfolio_value = sum(np.array(constituent_prices) * np.array(weights))
    
    if portfolio_value > index_price + transaction_cost:
        print(f"Arbitrage Opportunity: Sell Portfolio, Buy Index at {index_price}")
        return "Sell Portfolio, Buy Index"
    elif portfolio_value < index_price - transaction_cost:
        print(f"Arbitrage Opportunity: Buy Portfolio, Sell Index at {index_price}")
        return "Buy Portfolio, Sell Index"
    else:
        print("No arbitrage opportunity found.")
        return "Hold"
