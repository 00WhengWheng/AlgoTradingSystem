def quarterly_effect_trading(prices):
    """
    Quarterly Effect Trading Strategy.
    
    :param prices: pd.DataFrame with columns ['Date', 'Price'].
    :return: Average returns at the turn of the quarter.
    """
    df = prices.copy()
    df['Quarter'] = df['Date'].dt.to_period('Q')
    df['Next Quarter'] = df['Quarter'].shift(-1)
    
    # Calculate returns at the turn of the quarter
    quarter_turns = df[df['Quarter'] != df['Next Quarter']]
    returns = quarter_turns['Price'].pct_change().mean()
    
    print(f"Average Quarterly Turn Return: {returns:.2%}")
    return returns
