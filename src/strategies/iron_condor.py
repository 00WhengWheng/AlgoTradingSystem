def iron_condor(short_call_price, long_call_price, short_put_price, long_put_price,
                short_call_strike, long_call_strike, short_put_strike, long_put_strike):
    """
    Iron Condor Strategy.
    
    :param short_call_price: Price of the short call.
    :param long_call_price: Price of the long call.
    :param short_put_price: Price of the short put.
    :param long_put_price: Price of the long put.
    :param short_call_strike: Strike price of the short call.
    :param long_call_strike: Strike price of the long call.
    :param short_put_strike: Strike price of the short put.
    :param long_put_strike: Strike price of the long put.
    :return: Max profit, max loss, and break-even points.
    """
    # Net premium received
    net_credit = (short_call_price - long_call_price) + (short_put_price - long_put_price)
    
    # Max profit occurs if the underlying stays between short strikes
    max_profit = net_credit
    
    # Max loss occurs if the underlying moves beyond either long strike
    max_loss = max(long_call_strike - short_call_strike, short_put_strike - long_put_strike) - net_credit
    
    # Break-even points
    lower_break_even = short_put_strike - net_credit
    upper_break_even = short_call_strike + net_credit
    
    print(f"Iron Condor: Max Profit = {max_profit:.2f}, Max Loss = {max_loss:.2f}")
    print(f"Break-Even Points: {lower_break_even:.2f} to {upper_break_even:.2f}")
    return {
        "Max Profit": max_profit,
        "Max Loss": max_loss,
        "Break-Even Range": (lower_break_even, upper_break_even)
    }

def iron_condor_probability_of_success(short_put_strike, long_put_strike, short_call_strike, long_call_strike, implied_volatility, time_to_maturity):
    """
    Calculate Iron Condor Probability of Success.
    
    :param short_put_strike: Strike price of the short put.
    :param long_put_strike: Strike price of the long put.
    :param short_call_strike: Strike price of the short call.
    :param long_call_strike: Strike price of the long call.
    :param implied_volatility: Implied volatility of the underlying.
    :param time_to_maturity: Time to maturity in years.
    :return: Probability of staying within range.
    """
    lower_bound = norm.cdf((short_put_strike - implied_volatility) / (implied_volatility * sqrt(time_to_maturity)))
    upper_bound = norm.cdf((short_call_strike + implied_volatility) / (implied_volatility * sqrt(time_to_maturity)))
    
    probability = upper_bound - lower_bound
    print(f"Probability of Staying Within Range: {probability * 100:.2f}%")
    return probability
