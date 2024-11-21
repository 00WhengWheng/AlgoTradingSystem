import talib

def momentum_trading_strategy(prices):
    """
    Momentum Trading Strategy using RSI and MACD.
    
    :param prices: pd.Series of price data.
    :return: Signal DataFrame with Buy/Sell signals.
    """
    df = pd.DataFrame(prices, columns=['Price'])
    
    # Calculate RSI and MACD
    df['RSI'] = talib.RSI(prices, timeperiod=14)
    macd, macd_signal, _ = talib.MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['Signal Line'] = macd_signal
    
    # Generate signals
    df['Signal'] = np.where((df['RSI'] < 30) & (df['MACD'] > df['Signal Line']), 'Buy',
                            np.where((df['RSI'] > 70) & (df['MACD'] < df['Signal Line']), 'Sell', 'Hold'))
    
    # Plot for visualization
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(df['Price'], label='Price')
    plt.title('Momentum Trading Strategy')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(df['RSI'], label='RSI', color='orange')
    plt.axhline(30, linestyle='--', color='green', label='Oversold')
    plt.axhline(70, linestyle='--', color='red', label='Overbought')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    return df
