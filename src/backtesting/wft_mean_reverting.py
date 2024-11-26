def wft_mean_reverting_scalping(data, price_col, z_score_window, train_size, test_size):
    """
    Walk-Forward Test for Mean-Reverting Scalping on High-Frequency Data.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing high-frequency price data.
        price_col (str): Column representing asset prices.
        z_score_window (int): Window size for calculating Z-score.
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
        
        # Calculate mean and standard deviation for Z-score
        rolling_mean = train_data[price_col].rolling(z_score_window).mean()
        rolling_std = train_data[price_col].rolling(z_score_window).std()
        
        # Generate signals
        test_data['z_score'] = (test_data[price_col] - rolling_mean.iloc[-1]) / rolling_std.iloc[-1]
        test_data['long_signal'] = test_data['z_score'] < -2
        test_data['short_signal'] = test_data['z_score'] > 2
        
        # Calculate PnL
        test_data['pnl'] = np.where(test_data['long_signal'], 
                                    test_data[price_col].pct_change(), 
                                    np.where(test_data['short_signal'], 
                                             -test_data[price_col].pct_change(), 
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
