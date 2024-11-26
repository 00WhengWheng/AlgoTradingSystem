def wft_alternative_data(data, alt_data_col, price_col, threshold, train_size, test_size):
    """
    Walk-Forward Test for Alternative Data-Driven Strategy.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing alternative data and price data.
        alt_data_col (str): Column representing alternative data (e.g., foot traffic, sentiment).
        price_col (str): Column representing asset prices.
        threshold (float): Threshold for generating signals based on alternative data.
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
        
        # Optimize signal thresholds based on alternative data
        alt_mean = train_data[alt_data_col].mean()
        
        # Generate signals
        test_data['long_signal'] = test_data[alt_data_col] > alt_mean + threshold
        test_data['short_signal'] = test_data[alt_data_col] < alt_mean - threshold
        
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
