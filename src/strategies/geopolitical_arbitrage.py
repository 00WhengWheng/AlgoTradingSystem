def geopolitical_arbitrage(news_data, asset_prices):
    """
    Geopolitical Arbitrage Strategy.
    
    :param news_data: pd.DataFrame with columns ['Date', 'Event', 'Impact'].
    :param asset_prices: pd.Series of asset prices (e.g., USD/EUR).
    :return: DataFrame with trading signals.
    """
    df = pd.DataFrame(news_data)
    df['Asset_Price'] = asset_prices
    
    # Identify events with high impact
    df['Signal'] = np.where(df['Impact'] > 7, 'Trade on Volatility', 'Hold')
    
    print("Geopolitical Arbitrage Signals:")
    print(df[['Date', 'Event', 'Signal']])
    return df
