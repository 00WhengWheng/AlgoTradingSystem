# File: src/backtesting/parameter_optimizer.py
from itertools import product

class ParameterOptimizer:
    def __init__(self, data, strategy_class):
        self.data = data
        self.strategy_class = strategy_class

    def grid_search(self, param_grid):
        param_combinations = list(product(*param_grid.values()))
        best_params, best_performance = None, float("-inf")
        for params in param_combinations:
            param_dict = dict(zip(param_grid.keys(), params))
            performance = self.strategy_class(**param_dict).run(self.data)
            if performance["Total Return"] > best_performance:
                best_params, best_performance = param_dict, performance["Total Return"]
        return best_params, best_performance
