def protective_put(stock_price, put_price, strike_price):
    """
    Protective Put Strategy.
    
    :param stock_price: Current price of the stock.
    :param put_price: Price of the purchased put option.
    :param strike_price: Strike price of the put option.
    :return: Max profit and max loss.
    """
    # Maximum profit occurs if the stock price rises significantly
    max_profit = float('inf')  # Unlimited upside
    
    # Maximum loss occurs if the stock price falls to the strike price
    max_loss = stock_price - strike_price + put_price
    
    print(f"Protective Put: Max Profit = Unlimited, Max Loss = {max_loss:.2f}")
    return {"Max Profit": max_profit, "Max Loss": max_loss}
