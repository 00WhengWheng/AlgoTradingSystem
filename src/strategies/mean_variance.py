import numpy as np
from scipy.optimize import minimize

def mean_variance_optimization(returns, risk_free_rate=0.02):
    """
    Mean-Variance Portfolio Optimization.
    
    :param returns: pd.DataFrame of historical returns for assets.
    :param risk_free_rate: Annual risk-free rate for Sharpe ratio calculation.
    :return: Optimal portfolio weights.
    """
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    num_assets = len(mean_returns)
    
    # Objective function: Minimize portfolio volatility
    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    
    # Constraints: weights sum to 1
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = [(0, 1) for _ in range(num_assets)]
    
    # Initial guess: equal allocation
    initial_weights = np.array([1.0 / num_assets] * num_assets)
    
    # Optimize
    result = minimize(portfolio_volatility, initial_weights, constraints=constraints, bounds=bounds)
    optimal_weights = result.x
    
    print(f"Optimal Portfolio Weights: {optimal_weights}")
    return optimal_weights
