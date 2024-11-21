# src/backtesting/performance_metrics.py

import pandas as pd
import numpy as np

def calculate_drawdown(portfolio_values):
    """
    Calculates drawdown and maximum drawdown from portfolio values.
    
    Parameters:
    - portfolio_values (pd.Series): Series of portfolio values over time.
    
    Returns:
    - drawdown (pd.Series): Drawdown over time.
    - max_drawdown (float): Maximum drawdown observed.
    """
    peak = portfolio_values.cummax()
    drawdown = (portfolio_values - peak) / peak
    max_drawdown = drawdown.min()
    return drawdown, max_drawdown

def calculate_sortino_ratio(returns, target_return=0):
    """
    Calculates the Sortino Ratio, which adjusts for downside volatility only.
    
    Parameters:
    - returns (pd.Series): Series of returns.
    - target_return (float): Minimum acceptable return.
    
    Returns:
    - sortino_ratio (float): Sortino ratio value.
    """
    downside_returns = returns[returns < target_return]
    downside_std = downside_returns.std() * np.sqrt(252)
    expected_return = returns.mean() * 252
    sortino_ratio = (expected_return - target_return) / downside_std
    return sortino_ratio
