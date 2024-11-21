def trend_following_strategy(prices, short_window=20, long_window=50):
    """
    Algorithmic Trend Following Strategy using moving average crossovers.
    
    :param prices: pd.Series of price data.
    :param short_window: Lookback period for short-term moving average.
    :param long_window: Lookback period for long-term moving average.
    :return: Signal DataFrame with Buy/Sell signals.
    """
    df = pd.DataFrame(prices, columns=['Price'])
    df['Short_MA'] = df['Price'].rolling(window=short_window).mean()
    df['Long_MA'] = df['Price'].rolling(window=long_window).mean()
    
    # Generate signals
    df['Signal'] = np.where(df['Short_MA'] > df['Long_MA'], 'Buy',
                            np.where(df['Short_MA'] < df['Long_MA'], 'Sell', 'Hold'))
    
    # Plot for visualization
    plt.figure(figsize=(12, 6))
    plt.plot(df['Price'], label='Price')
    plt.plot(df['Short_MA'], label=f'Short MA ({short_window})', linestyle='--')
    plt.plot(df['Long_MA'], label=f'Long MA ({long_window})', linestyle='--')
    plt.title('Trend Following Strategy')
    plt.legend()
    plt.show()
    
    return df
