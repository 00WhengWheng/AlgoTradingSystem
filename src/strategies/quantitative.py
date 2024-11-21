import numpy as np
import pandas as pd
from scipy.optimize import minimize

def mean_variance_optimization(returns):
    """
    Quantitative Trading Strategy using Mean-Variance Portfolio Optimization.
    
    :param returns: pd.DataFrame of historical returns for assets.
    :return: Optimal weights for the portfolio.
    """
    # Calculate expected returns and covariance matrix
    expected_returns = returns.mean()
    covariance_matrix = returns.cov()

    # Define objective function (minimize portfolio variance)
    def portfolio_volatility(weights):
        return np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

    # Constraints: weights sum to 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    
    # Bounds: weights between 0 and 1
    bounds = [(0, 1) for _ in range(len(expected_returns))]

    # Initial guess: equal allocation
    num_assets = len(expected_returns)
    initial_weights = np.array([1.0 / num_assets] * num_assets)

    # Optimize
    result = minimize(portfolio_volatility, initial_weights, constraints=constraints, bounds=bounds)

    # Optimal weights
    optimal_weights = result.x
    print("Optimal Weights:\n", optimal_weights)
    return optimal_weights

# visualization of results

def plot_portfolio_weights(weights, assets):
    """
    Visualize Portfolio Weights.
    
    :param weights: Optimal weights from optimization.
    :param assets: List of asset names.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(assets, weights, color='blue')
    plt.title("Portfolio Weights")
    plt.xlabel("Assets")
    plt.ylabel("Weight")
    plt.show()


