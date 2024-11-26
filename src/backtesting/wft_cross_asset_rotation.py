_def wft_cross_asset_rotation(data, macro_cols, asset_cols, train_size, test_size):
    """
    Walk-Forward Test for Cross-Asset Rotation with Macro Indicators.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing macro indicators and asset returns.
        macro_cols (list): Columns representing macro indicators (e.g., GDP, inflation).
        asset_cols (list): Columns representing asset class returns (e.g., equities, bonds).
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
        
        # Optimize asset allocation using macro indicators
        optimal_weights = {}
        for asset in asset_cols:
            corr = train_data[macro_cols].corrwith(train_data[asset])
            optimal_weights[asset] = corr.mean()  # Averaging correlations with macro indicators
        
        # Normalize weights
        weight_sum = sum(abs(w) for w in optimal_weights.values())
        normalized_weights = {k: v / weight_sum for k, v in optimal_weights.items()}
        
        # Test out-of-sample returns
        test_data['portfolio_return'] = sum(
            normalized_weights[asset] * test_data[asset] for asset in asset_cols
        )
        
        # Log results
        results.append({
            'start_date': test_data.index[0],
            'end_date': test_data.index[-1],
            'portfolio_return': test_data['portfolio_return'].sum()
        })
        
        # Move window forward
        start += test_size
    
    return pd.DataFrame(results)
