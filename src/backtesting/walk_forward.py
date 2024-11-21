import pandas as pd
import numpy as np

class WalkForwardTester:
    def __init__(self, data, strategy_function, train_size=0.7, step_size=0.1):
        """
        Initialize the walk-forward tester.
        Args:
        - data (pd.DataFrame): Historical data with 'Close' prices and signals.
        - strategy_function (function): Function to execute the strategy on a dataset.
        - train_size (float): Proportion of data used for training in each window.
        - step_size (float): Proportion of data to move forward for the next window.
        """
        self.data = data
        self.strategy_function = strategy_function
        self.train_size = train_size
        self.step_size = step_size
        self.results = []

    def split_data(self, start_idx, train_length, test_length):
        """
        Split the data into training and testing sets.
        """
        train_data = self.data.iloc[start_idx : start_idx + train_length]
        test_data = self.data.iloc[start_idx + train_length : start_idx + train_length + test_length]
        return train_data, test_data

    def walk_forward(self, train_length, test_length):
        """
        Execute walk-forward testing.
        Args:
        - train_length (int): Number of data points in the training period.
        - test_length (int): Number of data points in the testing period.
        """
        start_idx = 0
        while start_idx + train_length + test_length <= len(self.data):
            train_data, test_data = self.split_data(start_idx, train_length, test_length)

            # Optimize parameters on training data
            optimized_params = self.strategy_function.optimize(train_data)

            # Test the strategy on testing data
            performance = self.strategy_function.run(test_data, optimized_params)

            # Store results
            self.results.append(performance)

            # Slide the window forward
            start_idx += int(test_length * self.step_size)

    def aggregate_results(self):
        """
        Aggregate results across all test periods.
        """
        metrics = pd.DataFrame(self.results)
        return {
            "Average Return": metrics["Total Return"].mean(),
            "Sharpe Ratio": metrics["Sharpe Ratio"].mean(),
            "Max Drawdown": metrics["Max Drawdown"].min(),
        }
def visualize_walk_forward(results):
    metrics = pd.DataFrame(results)
    metrics["Window"] = range(len(metrics))
    metrics.plot(x="Window", y=["Total Return", "Sharpe Ratio", "Max Drawdown"], subplots=True, figsize=(12, 8))
    plt.suptitle("Walk-Forward Testing Performance Metrics")
    plt.tight_layout()
    plt.show()
