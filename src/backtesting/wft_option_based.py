import numpy as np
import pandas as pd

def wft_options_volatility_arbitrage(data, iv_col, rv_col, train_size, test_size, hedge_ratio=1):
    """
    Walk-Forward Test for Options-Based Volatility Arbitrage with Dynamic Hedging.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing implied and realized volatility data.
        iv_col (str): Column representing implied volatility (IV).
        rv_col (str): Column representing realized volatility (RV).
        train_size (int): Number of rows in the in-sample (training) data.
        test_size (int): Number of rows in the out-of-sample (testing) data.
        hedge_ratio (float): The delta-neutral hedge ratio.
    
    Returns:
        pd.DataFrame: Out-of-sample performance metrics for each iteration.
    """
    results = []
    start = 0
    
    while start + train_size + test_size <= len(data):
        # Define training and testing data
        train_data = data.iloc[start:start + train_size]
        test_data = data.iloc[start + train_size:start + train_size + test_size]
        
        # Calculate average IV-RV spread in training
        train_data['spread'] = train_data[iv_col] - train_data[rv_col]
        spread_mean = train_data['spread'].mean()
        spread_std = train_data['spread'].std()
        
        # Dynamic thresholds (e.g., 1 standard deviation)
        long_threshold = spread_mean - spread_std
        short_threshold = spread_mean + spread_std
        
        # Generate signals in out-of-sample
        test_data['spread'] = test_data[iv_col] - test_data[rv_col]
        test_data['long_signal'] = test_data['spread'] < long_threshold
        test_data['short_signal'] = test_data['spread'] > short_threshold
        
        # Simulate PnL with delta-neutral hedging
        test_data['pnl'] = 0
        for i in range(len(test_data)):
            if test_data['long_signal'].iloc[i]:
                # Buy option, expect realized volatility to exceed implied
                test_data['pnl'].iloc[i] = hedge_ratio * (test_data[rv_col].iloc[i] - test_data[iv_col].iloc[i])
            elif test_data['short_signal'].iloc[i]:
                # Sell option, expect implied volatility to exceed realized
                test_data['pnl'].iloc[i] = hedge_ratio * (test_data[iv_col].iloc[i] - test_data[rv_col].iloc[i])
        
        # Calculate performance metrics
        total_pnl = test_data['pnl'].sum()
        sharpe_ratio = test_data['pnl'].mean() / test_data['pnl'].std() if test_data['pnl'].std() != 0 else 0
        win_rate = (test_data['pnl'] > 0).mean()
        max_drawdown = (test_data['pnl'].cumsum() - test_data['pnl'].cumsum().cummax()).min()
        
        # Log results
        results.append({
            'start_date': test_data.index[0],
            'end_date': test_data.index[-1],
            'total_pnl': total_pnl,
            'sharpe_ratio': sharpe_ratio,
            'win_rate': win_rate,
            'max_drawdown': max_drawdown
        })
        
        # Move window forward
        start += test_size
    
    return pd.DataFrame(results)
