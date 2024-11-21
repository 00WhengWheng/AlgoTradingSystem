def breakout_trading_strategy(prices, volume, window=20):
    """
    Breakout Trading Strategy.
    
    :param prices: pd.Series of price data.
    :param volume: pd.Series of volume data.
    :param window: Lookback period for high/low price.
    :return: Signal DataFrame with Buy/Sell signals.
    """
    df = pd.DataFrame({'Price': prices, 'Volume': volume})
    
    # Calculate rolling highs and lows
    df['Rolling High'] = df['Price'].rolling(window=window).max()
    df['Rolling Low'] = df['Price'].rolling(window=window).min()
    
    # Generate signals
    df['Signal'] = np.where((df['Price'] > df['Rolling High']) & (df['Volume'] > df['Volume'].mean()), 'Buy',
                            np.where((df['Price'] < df['Rolling Low']) & (df['Volume'] > df['Volume'].mean()), 'Sell', 'Hold'))
    
    # Plot for visualization
    plt.figure(figsize=(12, 6))
    plt.plot(df['Price'], label='Price')
    plt.plot(df['Rolling High'], label='Resistance', linestyle='--', color='red')
    plt.plot(df['Rolling Low'], label='Support', linestyle='--', color='green')
    plt.title('Breakout Trading Strategy')
    plt.legend()
    plt.show()
    
    return df
