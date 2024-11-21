def bull_call_spread(long_call_price, short_call_price, long_strike, short_strike):
    """
    Bull Call Spread Strategy.
    
    :param long_call_price: Price of the long call option.
    :param short_call_price: Price of the short call option.
    :param long_strike: Strike price of the long call.
    :param short_strike: Strike price of the short call.
    :return: Maximum profit and loss.
    """
    # Net cost of the spread
    net_cost = long_call_price - short_call_price
    
    # Maximum profit occurs when the underlying closes above the short strike
    max_profit = short_strike - long_strike - net_cost
    
    # Maximum loss is the initial cost of the spread
    max_loss = net_cost
    
    print(f"Bull Call Spread: Max Profit = {max_profit:.2f}, Max Loss = {max_loss:.2f}")
    return {"Max Profit": max_profit, "Max Loss": max_loss}
