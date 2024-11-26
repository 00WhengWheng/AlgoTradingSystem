def wft_sentiment_momentum(data, sentiment_col, price_col, threshold, train_size, test_size):
    """
    Walk-Forward Test for Sentiment-Driven Momentum Strategy.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing sentiment and price data.
        sentiment_col (str): Column name for sentiment scores.
        price_col (str): Column name for asset prices.
        threshold (float): Sentiment score threshold for generating signals.
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
        
        # Calculate sentiment thresholds
        sentiment_mean = train_data[sentiment_col].mean()
        
        # Generate signals
        test_data['long_signal'] = test_data[sentiment_col] > sentiment_mean + threshold
        test_data['short_signal'] = test_data[sentiment_col] < sentiment_mean - threshold
        
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
