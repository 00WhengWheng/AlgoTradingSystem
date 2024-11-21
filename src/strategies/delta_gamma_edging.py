def delta_gamma_hedging(option_delta, option_gamma, spot_price_change):
    """
    Delta-Gamma Hedging Strategy.
    
    :param option_delta: Current delta of the option.
    :param option_gamma: Current gamma of the option.
    :param spot_price_change: Change in the underlying asset's price.
    :return: Adjusted delta after price change.
    """
    # Adjust delta for gamma effect
    new_delta = option_delta + option_gamma * spot_price_change
    print(f"Adjusted Delta: {new_delta:.2f}")
    return new_delta
