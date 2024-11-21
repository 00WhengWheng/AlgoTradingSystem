import statsmodels.api as sm

def pairs_trading_strategy(asset1, asset2):
    """
    Pairs Trading Strategy based on cointegration.
    
    :param asset1: pd.Series of price data for asset 1.
    :param asset2: pd.Series of price data for asset 2.
    :return: Signal DataFrame with Buy/Sell signals.
    """
    df = pd.DataFrame({'Asset1': asset1, 'Asset2': asset2})
    
    # Perform cointegration test
    _, pvalue, _ = sm.tsa.coint(asset1, asset2)
    if pvalue > 0.05:
        raise ValueError("The assets are not cointegrated; pairs trading may not be effective.")
    
    # Calculate price spread and z-score
    hedge_ratio = sm.OLS(asset1, sm.add_constant(asset2)).fit().params[1]
    df['Spread'] = df['Asset1'] - hedge_ratio * df['Asset2']
    df['Z-Score'] = (df['Spread'] - df['Spread'].mean()) / df['Spread'].std()
    
    # Generate signals
    df['Signal'] = np.where(df['Z-Score'] > 2, 'Sell Asset1, Buy Asset2',
                            np.where(df['Z-Score'] < -2, 'Buy Asset1, Sell Asset2', 'Hold'))
    
    # Plot for visualization
    plt.figure(figsize=(12, 6))
    plt.plot(df['Spread'], label='Spread')
    plt.axhline(df['Spread'].mean(), linestyle='--', color='blue', label='Mean')
    plt.axhline(df['Spread'].mean() + 2 * df['Spread'].std(), linestyle='--', color='red', label='Upper Threshold')
    plt.axhline(df['Spread'].mean() - 2 * df['Spread'].std(), linestyle='--', color='green', label='Lower Threshold')
    plt.title('Pairs Trading Strategy')
    plt.legend()
    plt.show()
    
    return df
