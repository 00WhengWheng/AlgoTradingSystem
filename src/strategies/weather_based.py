def weather_based_trading(weather_data, commodity_prices):
    """
    Weather-Based Trading Strategy.
    
    :param weather_data: pd.DataFrame with columns ['Date', 'Temperature', 'Rainfall'].
    :param commodity_prices: pd.Series of commodity prices (e.g., Natural Gas).
    :return: DataFrame with trading signals based on weather anomalies.
    """
    df = pd.DataFrame(weather_data)
    df['Commodity_Price'] = commodity_prices
    
    # Identify extreme weather anomalies
    df['Temp_Anomaly'] = df['Temperature'] - df['Temperature'].mean()
    df['Rain_Anomaly'] = df['Rainfall'] - df['Rainfall'].mean()
    
    # Generate signals based on anomalies
    df['Signal'] = np.where(df['Temp_Anomaly'] > 5, 'Buy (Extreme Cold)',
                            np.where(df['Rain_Anomaly'] > 50, 'Sell (Flood Risk)', 'Hold'))
    
    return df
