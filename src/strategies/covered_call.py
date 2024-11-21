def covered_call(stock_price, call_price, strike_price):
    """
    Covered Call Strategy.
    
    :param stock_price: Current price of the stock.
    :param call_price: Price of the sold call option.
    :param strike_price: Strike price of the sold call option.
    :return: Max profit and max loss.
    """
    # Maximum profit occurs if the stock closes at or above the strike price
    max_profit = (strike_price - stock_price) + call_price
    
    # Maximum loss occurs if the stock price drops to zero
    max_loss = stock_price - call_price
    
    print(f"Covered Call: Max Profit = {max_profit:.2f}, Max Loss = {max_loss:.2f}")
    return {"Max Profit": max_profit, "Max Loss": max_loss}
