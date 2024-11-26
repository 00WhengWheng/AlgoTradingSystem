import numpy as np

def wft_volatility_breakout(data, atr_col, high_col, low_col, close_col, train_size, test_size):
    """
    Walk-Forward Test for Volatility Breakout with Regime Detection.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing price and ATR data.
        atr_col (str): Column name for the Average True Range (ATR).
        high_col (str): Column name for the high price.
        low_col (str): Column name for the low price.
        close_col (str): Column name for the close price.
        train_size (int): Number of rows in the in-sample (training) data.
        test_size (int): Number of rows in the out-of-sample (testing) data.
    
    Returns:
        pd.DataFrame: Out-of-sample performance metrics for each iteration.
    """
    results = []
    start = 0
    
    while start + train_size + test_size <= len(data):
        # Define training and testing data
        train_data = data.iloc[start:start + train_size]
        test_data = data.iloc[start + train_size:start + train_size + test_size]
        
        # Calculate breakout levels
        atr_mean = train_data[atr_col].mean()
        upper_breakout = train_data[close_col].iloc[-1] + 1.5 * atr_mean
        lower_breakout = train_data[close_col].iloc[-1] - 1.5 * atr_mean
        
        # Test breakout levels
        test_data['long_entry'] = test_data[high_col] > upper_breakout
        test_data['short_entry'] = test_data[low_col] < lower_breakout
        test_data['pnl'] = np.where(test_data['long_entry'], 
                                    test_data[close_col] - upper_breakout,
                                    np.where(test_data['short_entry'], 
                                             lower_breakout - test_data[close_col], 
                                             0))
        
        # Log results
        results.append({
            'start_date': test_data.index[0],
            'end_date': test_data.index[-1],
            'pnl': test_data['pnl'].sum()
        })
        
        # Move window forward
        start += test_size
    
    return pd.DataFrame(results)
