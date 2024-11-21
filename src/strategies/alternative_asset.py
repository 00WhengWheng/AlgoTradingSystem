def alternative_asset_trading(asset_data, moving_avg_period=12):
    """
    Alternative Asset Trading Strategy.
    
    :param asset_data: pd.Series of historical asset prices (e.g., wine, art).
    :param moving_avg_period: Lookback period for moving average.
    :return: Trading signals based on price trend.
    """
    asset_data['Moving Average'] = asset_data['Price'].rolling(window=moving_avg_period).mean()
    asset_data['Signal'] = asset_data.apply(
        lambda row: "Buy" if row['Price'] > row['Moving Average'] else "Sell", axis=1
    )
    return asset_data
