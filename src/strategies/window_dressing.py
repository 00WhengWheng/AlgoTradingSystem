def window_dressing_analysis(prices, volumes, quarter_end_dates, window=5):
    """
    Window Dressing Analysis.
    
    :param prices: pd.Series of stock prices.
    :param volumes: pd.Series of stock volumes.
    :param quarter_end_dates: List of quarter-end dates.
    :param window: Number of days before quarter-end to analyze.
    :return: Price and volume anomalies around quarter-end.
    """
    anomalies = []
    for date in quarter_end_dates:
        pre_end_prices = prices.loc[:date].iloc[-window:]
        pre_end_volumes = volumes.loc[:date].iloc[-window:]
        
        price_anomaly = pre_end_prices.pct_change().mean()
        volume_anomaly = pre_end_volumes.mean() / volumes.mean()
        
        anomalies.append({
            "Quarter-End Date": date,
            "Avg Price Change": price_anomaly,
            "Volume Anomaly": volume_anomaly
        })
    
    return pd.DataFrame(anomalies)
