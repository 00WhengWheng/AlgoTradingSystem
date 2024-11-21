def commodity_spread_trading(commodity1_prices, commodity2_prices, window=20):
    """
    Commodity Spread Trading Strategy.
    
    :param commodity1_prices: pd.Series of prices for Commodity 1 (e.g., Brent crude).
    :param commodity2_prices: pd.Series of prices for Commodity 2 (e.g., WTI crude).
    :param window: Lookback period for spread mean calculation.
    :return: DataFrame with spread and trading signals.
    """
    df = pd.DataFrame({
        'Commodity1': commodity1_prices,
        'Commodity2': commodity2_prices
    })
    
    # Calculate spread and rolling statistics
    df['Spread'] = df['Commodity1'] - df['Commodity2']
    df['Spread_Mean'] = df['Spread'].rolling(window).mean()
    df['Spread_Std'] = df['Spread'].rolling(window).std()
    
    # Generate signals
    df['Signal'] = np.where(df['Spread'] > df['Spread_Mean'] + df['Spread_Std'], 'Sell Commodity1, Buy Commodity2',
                            np.where(df['Spread'] < df['Spread_Mean'] - df['Spread_Std'], 'Buy Commodity1, Sell Commodity2', 'Hold'))
    
    return df
