def january_effect_analysis(prices, start_date='01-01', end_date='01-31'):
    """
    January Effect Analysis.
    
    :param prices: pd.DataFrame with columns ['Date', 'Price'].
    :param start_date: Start date for analysis (default: '01-01').
    :param end_date: End date for analysis (default: '01-31').
    :return: Average returns in January.
    """
    df = prices.copy()
    df['Month-Day'] = df['Date'].dt.strftime('%m-%d')
    january_data = df[(df['Month-Day'] >= start_date) & (df['Month-Day'] <= end_date)]
    
    avg_return = january_data['Price'].pct_change().mean()
    print(f"Average January Return: {avg_return:.2%}")
    return avg_return
