def variance_swap_pricing(implied_volatility, realized_volatility, notional):
    """
    Variance Swap Pricing Strategy.
    
    :param implied_volatility: Implied volatility of the underlying asset.
    :param realized_volatility: Realized volatility of the underlying asset.
    :param notional: Notional value of the variance swap.
    :return: Payoff of the variance swap.
    """
    # Calculate variance from volatilities
    implied_variance = implied_volatility ** 2
    realized_variance = realized_volatility ** 2
    
    # Payoff calculation
    payoff = notional * (realized_variance - implied_variance)
    
    print(f"Variance Swap Payoff: {payoff:.2f}")
    return payoff
