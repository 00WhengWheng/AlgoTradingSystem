import holidays

def holiday_effect_trading(prices, country='US'):
    """
    Holiday Effect Trading Strategy.
    
    :param prices: pd.DataFrame with columns ['Date', 'Price'].
    :param country: Country code for holiday calendar (default: US).
    :return: Average pre/post-holiday returns.
    """
    df = prices.copy()
    holiday_list = holidays.country_holidays(country)
    
    # Identify holiday dates in the dataset
    df['Holiday'] = df['Date'].apply(lambda x: x in holiday_list)
    df['Pre-Holiday'] = df['Holiday'].shift(-1)  # Day before the holiday
    df['Post-Holiday'] = df['Holiday'].shift(1)  # Day after the holiday
    
    # Calculate returns
    df['Return'] = df['Price'].pct_change()
    pre_holiday_returns = df.loc[df['Pre-Holiday'] == True, 'Return']
    post_holiday_returns = df.loc[df['Post-Holiday'] == True, 'Return']
    
    # Average returns
    avg_pre = pre_holiday_returns.mean()
    avg_post = post_holiday_returns.mean()
    
    print(f"Average Pre-Holiday Return: {avg_pre:.2%}")
    print(f"Average Post-Holiday Return: {avg_post:.2%}")
    
    return {"Pre-Holiday Return": avg_pre, "Post-Holiday Return": avg_post}
