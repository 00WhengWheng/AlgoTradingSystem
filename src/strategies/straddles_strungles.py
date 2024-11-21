def straddle_pricing_with_iv(call_price, put_price, strike_price, implied_volatility, time_to_maturity):
    """
    Straddle Pricing with Implied Volatility Adjustments.
    
    :param call_price: Price of the call option.
    :param put_price: Price of the put option.
    :param strike_price: Strike price of the options.
    :param implied_volatility: Implied volatility of the options.
    :param time_to_maturity: Time to expiration in years.
    :return: Adjusted break-even points.
    """
    # Adjust cost for volatility
    cost = call_price + put_price + (implied_volatility * sqrt(time_to_maturity))
    upper_break_even = strike_price + cost
    lower_break_even = strike_price - cost
    
    print(f"Adjusted Break-Even: {lower_break_even:.2f} to {upper_break_even:.2f}")
    return {"Lower Break-Even": lower_break_even, "Upper Break-Even": upper_break_even}
