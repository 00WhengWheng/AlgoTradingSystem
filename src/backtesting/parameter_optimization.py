import pandas as pd
import numpy as np
from itertools import product

class ParameterOptimizer:
    def __init__(self, data, strategy_class):
        """
        Initialize the parameter optimizer.
        Args:
        - data (pd.DataFrame): Historical data with 'Close' prices.
        - strategy_class (class): Trading strategy class to optimize.
        """
        self.data = data
        self.strategy_class = strategy_class
        self.results = []

    def grid_search(self, param_grid):
        """
        Perform grid search over the parameter grid.
        Args:
        - param_grid (dict): Dictionary of parameter ranges. Example:
            {
                "short_ma": [5, 10, 15],
                "long_ma": [20, 30, 40]
            }
        """
        param_combinations = list(product(*param_grid.values()))
        param_names = list(param_grid.keys())
        best_params = None
        best_performance = float('-inf')

        for params in param_combinations:
            param_dict = dict(zip(param_names, params))
            performance = self.evaluate_params(param_dict)

            self.results.append({"params": param_dict, **performance})

            if performance["Total Return"] > best_performance:
                best_performance = performance["Total Return"]
                best_params = param_dict

        return best_params, best_performance

    def evaluate_params(self, params):
        """
        Evaluate the strategy with the given parameters.
        Args:
        - params (dict): Dictionary of parameters.
        Returns:
        - dict: Performance metrics.
        """
        strategy = self.strategy_class(**params)
        test_data = self.data.copy()
        performance = strategy.run(test_data, params)
        return performance

import random

class RandomSearchOptimizer(ParameterOptimizer):
    def random_search(self, param_ranges, n_iter=10):
        """
        Perform random search over the parameter ranges.
        Args:
        - param_ranges (dict): Parameter ranges. Example:
            {
                "short_ma": (5, 15),  # Min and max range
                "long_ma": (20, 40)
            }
        - n_iter (int): Number of random combinations to test.
        """
        best_params = None
        best_performance = float('-inf')

        for _ in range(n_iter):
            params = {key: random.randint(*value) for key, value in param_ranges.items()}
            performance = self.evaluate_params(params)

            self.results.append({"params": params, **performance})

            if performance["Total Return"] > best_performance:
                best_performance = performance["Total Return"]
                best_params = params

        return best_params, best_performance


from skopt import gp_minimize
from skopt.space import Integer

class BayesianOptimizer(ParameterOptimizer):
    def bayesian_optimize(self, param_ranges, n_calls=20):
        """
        Perform Bayesian optimization over the parameter ranges.
        Args:
        - param_ranges (dict): Parameter ranges. Example:
            {
                "short_ma": (5, 15),  # Min and max range
                "long_ma": (20, 40)
            }
        - n_calls (int): Number of iterations for optimization.
        """
        dimensions = [Integer(*param_ranges[key], name=key) for key in param_ranges.keys()]

        def objective(params):
            param_dict = {name: value for name, value in zip(param_ranges.keys(), params)}
            performance = self.evaluate_params(param_dict)
            return -performance["Total Return"]  # Minimize negative return

        result = gp_minimize(objective, dimensions, n_calls=n_calls)
        best_params = {name: value for name, value in zip(param_ranges.keys(), result.x)}
        return best_params, -result.fun


def plot_optimization_results(results):
    df = pd.DataFrame(results)
    for param in df["params"].iloc[0].keys():
        df[param] = df["params"].apply(lambda x: x[param])

    # Scatter plot for each parameter vs. Total Return
    for param in df["params"].iloc[0].keys():
        plt.figure(figsize=(8, 4))
        plt.scatter(df[param], df["Total Return"], alpha=0.6)
        plt.title(f"Optimization Results: {param} vs. Total Return")
        plt.xlabel(param)
        plt.ylabel("Total Return")
        plt.grid()
        plt.show()
