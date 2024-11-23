import numpy as np
import pandas as pd
from scipy.optimize import minimize

def mean_variance_optimization(returns, risk_free_rate=0.01):
    """
    Mean-Variance Optimization for Portfolio Allocation.

    :param returns: pd.DataFrame of historical returns for assets.
    :param risk_free_rate: Risk-free rate for Sharpe ratio calculation.
    :return: Optimal weights for the portfolio.
    """
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_assets = len(mean_returns)

    # Objective function: Minimize portfolio variance
    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Constraints: Weights must sum to 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})

    # Bounds: No short selling (weights between 0 and 1)
    bounds = tuple((0, 1) for _ in range(num_assets))

    # Initial guess: Equal allocation
    initial_weights = np.array([1 / num_assets] * num_assets)

    # Perform optimization
    result = minimize(portfolio_volatility, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

    # Calculate Sharpe ratio of the optimized portfolio
    optimized_weights = result.x
    portfolio_return = np.dot(optimized_weights, mean_returns)
    portfolio_std_dev = portfolio_volatility(optimized_weights)
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std_dev

    return {
        "Optimal Weights": optimized_weights,
        "Portfolio Return": portfolio_return,
        "Portfolio Volatility": portfolio_std_dev,
        "Sharpe Ratio": sharpe_ratio
    }
