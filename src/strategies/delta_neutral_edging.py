import QuantLib as ql

def delta_neutral_hedging(spot_price, option_delta, portfolio_position):
    """
    Delta-Neutral Hedging Strategy.
    
    :param spot_price: Current price of the underlying asset.
    :param option_delta: Delta of the option (sensitivity to underlying price changes).
    :param portfolio_position: Number of options in the portfolio.
    :return: Number of shares needed to hedge the portfolio.
    """
    # Calculate the total delta of the portfolio
    total_delta = option_delta * portfolio_position
    
    # Shares needed to hedge the portfolio
    shares_needed = -total_delta / spot_price
    
    print(f"To achieve delta-neutrality, hedge with {shares_needed:.2f} shares.")
    return shares_needed
