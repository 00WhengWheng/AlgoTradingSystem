def synthetic_long(spot_price, call_price, put_price, strike_price, risk_free_rate, time_to_maturity):
    """
    Synthetic Long Position using options.
    
    :param spot_price: Current price of the underlying asset.
    :param call_price: Price of the call option.
    :param put_price: Price of the put option.
    :param strike_price: Strike price of the options.
    :param risk_free_rate: Risk-free interest rate.
    :param time_to_maturity: Time to maturity in years.
    :return: Synthetic long position price.
    """
    # Synthetic price = Call - Put + Strike discounted at risk-free rate
    discounted_strike = strike_price * np.exp(-risk_free_rate * time_to_maturity)
    synthetic_price = call_price - put_price + discounted_strike
    
    print(f"Synthetic Long Position Price: {synthetic_price:.2f}")
    return synthetic_price


def synthetic_short(spot_price, call_price, put_price, strike_price, risk_free_rate, time_to_maturity):
    """
    Synthetic Short Position using options.
    
    :param spot_price: Current price of the underlying asset.
    :param call_price: Price of the call option.
    :param put_price: Price of the put option.
    :param strike_price: Strike price of the options.
    :param risk_free_rate: Risk-free interest rate.
    :param time_to_maturity: Time to maturity in years.
    :return: Synthetic short position price.
    """
    # Synthetic short = Put - Call - Strike discounted at risk-free rate
    discounted_strike = strike_price * np.exp(-risk_free_rate * time_to_maturity)
    synthetic_price = put_price - call_price - discounted_strike
    
    print(f"Synthetic Short Position Price: {synthetic_price:.2f}")
    return synthetic_price
