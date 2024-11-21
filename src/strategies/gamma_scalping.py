from math import exp, sqrt, log
from scipy.stats import norm

def black_scholes_greeks(spot_price, strike_price, time_to_maturity, risk_free_rate, volatility, option_type='call'):
    """
    Calculate Delta and Gamma using Black-Scholes.
    
    :param spot_price: Current price of the underlying asset.
    :param strike_price: Strike price of the option.
    :param time_to_maturity: Time to maturity in years.
    :param risk_free_rate: Annual risk-free interest rate.
    :param volatility: Annualized volatility of the underlying.
    :param option_type: 'call' or 'put'.
    :return: Delta and Gamma.
    """
    d1 = (log(spot_price / strike_price) + (risk_free_rate + (volatility ** 2) / 2) * time_to_maturity) / (volatility * sqrt(time_to_maturity))
    d2 = d1 - volatility * sqrt(time_to_maturity)
    
    # Calculate Delta
    if option_type == 'call':
        delta = norm.cdf(d1)
    elif option_type == 'put':
        delta = norm.cdf(d1) - 1
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")
    
    # Calculate Gamma
    gamma = norm.pdf(d1) / (spot_price * volatility * sqrt(time_to_maturity))
    
    return delta, gamma
