def weather_derivative_trading(weather_data, derivative_prices, threshold=5):
    """
    Weather Derivative Trading Strategy.
    
    :param weather_data: DataFrame with temperature and forecast data.
    :param derivative_prices: Series of weather derivative prices.
    :param threshold: Degree threshold for significant weather anomalies.
    :return: Trading signals based on weather anomalies.
    """
    weather_data['Anomaly'] = weather_data['Temperature'] - weather_data['Historical Average']
    signals = []
    
    for anomaly, price in zip(weather_data['Anomaly'], derivative_prices):
        if anomaly > threshold:
            signals.append("Buy Heating Derivative")
        elif anomaly < -threshold:
            signals.append("Buy Cooling Derivative")
        else:
            signals.append("Hold")
    
    return pd.DataFrame({
        "Anomaly": weather_data['Anomaly'],
        "Derivative Price": derivative_prices,
        "Signal": signals
    })
