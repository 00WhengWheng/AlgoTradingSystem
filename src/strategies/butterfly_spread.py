def butterfly_spread(long_call_price, short_call_price, strike_lower, strike_middle, strike_upper):
    """
    Butterfly Spread Strategy.
    
    :param long_call_price: Price of the long calls (at lower and upper strikes).
    :param short_call_price: Price of the short calls (at the middle strike).
    :param strike_lower: Lower strike price.
    :param strike_middle: Middle strike price.
    :param strike_upper: Upper strike price.
    :return: Max profit, max loss, and break-even points.
    """
    # Net cost of the butterfly spread
    net_cost = 2 * long_call_price - short_call_price
    
    # Max profit occurs if the underlying closes at the middle strike
    max_profit = strike_middle - strike_lower - net_cost
    
    # Max loss is the initial cost of the spread
    max_loss = net_cost
    
    # Break-even points
    lower_break_even = strike_lower + net_cost
    upper_break_even = strike_upper - net_cost
    
    print(f"Butterfly Spread: Max Profit = {max_profit:.2f}, Max Loss = {max_loss:.2f}")
    print(f"Break-Even Points: {lower_break_even:.2f} to {upper_break_even:.2f}")
    return {
        "Max Profit": max_profit,
        "Max Loss": max_loss,
        "Break-Even Range": (lower_break_even, upper_break_even)
    }
