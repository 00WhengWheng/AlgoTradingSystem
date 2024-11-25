import numpy as np

class MarkowitzOptimizer:
    def __init__(self, returns, cov_matrix):
        self.returns = returns
        self.cov_matrix = cov_matrix

    def optimize(self, risk_tolerance=0.1):
        weights = np.linalg.solve(self.cov_matrix, self.returns)
        weights /= np.sum(weights)
        return weights
