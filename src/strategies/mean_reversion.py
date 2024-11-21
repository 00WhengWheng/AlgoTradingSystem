import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

def mean_reversion_strategy(prices, window=20, num_std_dev=2):
    """
    Mean Reversion Strategy based on Bollinger Bands.
    
    :param prices: pd.Series of price data.
    :param window: Lookback period for moving average.
    :param num_std_dev: Number of standard deviations for Bollinger Bands.
    :return: Signal DataFrame with Buy/Sell signals.
    """
    df = pd.DataFrame(prices, columns=['Price'])
    df['MA'] = df['Price'].rolling(window=window).mean()
    df['STD'] = df['Price'].rolling(window=window).std()
    df['Upper Band'] = df['MA'] + num_std_dev * df['STD']
    df['Lower Band'] = df['MA'] - num_std_dev * df['STD']
    
    # Generate signals
    df['Signal'] = np.where(df['Price'] > df['Upper Band'], 'Sell', 
                            np.where(df['Price'] < df['Lower Band'], 'Buy', 'Hold'))
    
    # Plot for visualization
    plt.figure(figsize=(12, 6))
    plt.plot(df['Price'], label='Price')
    plt.plot(df['MA'], label='Moving Average', linestyle='--')
    plt.plot(df['Upper Band'], label='Upper Band', linestyle='--', color='red')
    plt.plot(df['Lower Band'], label='Lower Band', linestyle='--', color='green')
    plt.legend()
    plt.title('Mean Reversion Strategy')
    plt.show()
    
    return df
