def wft_event_driven(data, event_dates, price_col, event_window, train_size, test_size):
    """
    Walk-Forward Test for Event-Driven Strategy.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing price data with timestamps.
        event_dates (list): List of dates corresponding to events (e.g., earnings).
        price_col (str): Column representing asset prices.
        event_window (int): Number of days before and after an event to consider.
        train_size (int): Number of events in the in-sample (training) data.
        test_size (int): Number of events in the out-of-sample (testing) data.
    
    Returns:
        pd.DataFrame: Out-of-sample performance metrics for each iteration.
    """
    results = []
    start = 0
    
    while start + train_size + test_size <= len(event_dates):
        # Define training and testing events
        train_events = event_dates[start:start + train_size]
        test_events = event_dates[start + train_size:start + train_size + test_size]
        
        # Calculate average return around events in training
        train_returns = []
        for event in train_events:
            event_data = data.loc[event - event_window:event + event_window]
            train_returns.append(event_data[price_col].pct_change().sum())
        avg_return = np.mean(train_returns)
        
        # Test on out-of-sample events
        test_returns = []
        for event in test_events:
            event_data = data.loc[event - event_window:event + event_window]
            test_returns.append(event_data[price_col].pct_change().sum())
        
        # Log results
        results.append({
            'start_date': test_events[0],
            'end_date': test_events[-1],
            'expected_return': avg_return,
            'actual_return': np.mean(test_returns)
        })
        
        # Move window forward
        start += test_size
    
    return pd.DataFrame(results)
