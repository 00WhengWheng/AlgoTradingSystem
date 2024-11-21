def herding_behavior_analysis(volumes, rolling_window=10):
    """
    Analyze herding behavior based on trading volume spikes.
    
    :param volumes: pd.Series of trading volumes for an asset.
    :param rolling_window: Lookback period for average volume.
    :return: Trading signals.
    """
    avg_volume = volumes.rolling(rolling_window).mean()
    volume_spike = volumes > (avg_volume * 1.5)
    
    signals = ["Buy (Overbought)" if spike else "Sell (Underbought)" for spike in volume_spike]
    
    return pd.DataFrame({
        "Volume": volumes,
        "Avg Volume": avg_volume,
        "Signal": signals
    })
