def calendar_spread(long_option_price, short_option_price):
    """
    Calendar Spread Strategy.
    
    :param long_option_price: Price of the long-dated option.
    :param short_option_price: Price of the short-dated option.
    :return: Net debit and potential profit range.
    """
    # Net cost of the calendar spread
    net_debit = long_option_price - short_option_price
    
    print(f"Calendar Spread: Net Debit = {net_debit:.2f}")
    return {"Net Debit": net_debit}

def calendar_spread_with_theta(long_theta, short_theta, net_debit):
    """
    Calendar Spread with Theta Adjustment.
    
    :param long_theta: Theta of the long-dated option.
    :param short_theta: Theta of the short-dated option.
    :param net_debit: Net cost of the calendar spread.
    :return: Adjusted profit/loss over time.
    """
    daily_theta = short_theta - long_theta  # Net daily time decay
    time_to_profit = net_debit / abs(daily_theta) if daily_theta < 0 else float('inf')
    
    print(f"Time to Profit: {time_to_profit:.2f} days (if achievable)")
    return {"Time to Profit": time_to_profit}
