import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class WalkForwardPipeline:
    """
    A pipeline for managing and executing different Walk-Forward Testing techniques.
    """
    def __init__(self):
        self.techniques = {}
        self.strategies = {}

    def register_technique(self, name, technique_function):
        """
        Register a Walk-Forward Testing technique.
        :param name: Name of the technique (e.g., 'rolling', 'expanding').
        :param technique_function: Function implementing the technique.
        """
        self.techniques[name] = technique_function

    def register_strategy(self, name, strategy_instance, params=None, technique="rolling"):
        """
        Register a strategy with a specific Walk-Forward Testing technique.
        :param name: Name of the strategy.
        :param strategy_instance: Instance of the strategy.
        :param params: Parameters for the strategy.
        :param technique: Walk-Forward Testing technique to use.
        """
        if technique not in self.techniques:
            raise ValueError(f"Technique {technique} is not registered.")
        self.strategies[name] = {
            "strategy": strategy_instance,
            "params": params,
            "technique": technique
        }

    def execute(self, data, train_size, test_size):
        """
        Execute all registered strategies with their respective techniques.
        :param data: Historical data (pd.DataFrame).
        :param train_size: Size of the training window.
        :param test_size: Size of the testing window.
        :return: Consolidated results.
        """
        results = {}
        for name, config in self.strategies.items():
            strategy = config["strategy"]
            params = config["params"]
            technique = config["technique"]
            
            print(f"Executing strategy: {name} using {technique} technique")
            technique_function = self.techniques[technique]
            results[name] = technique_function(strategy, data, params, train_size, test_size)
        
        return results


# Techniques implementations
def rolling_walk_forward(strategy, data, params, train_size, test_size):
    results = []
    total_size = len(data)

    for start in range(0, total_size - train_size - test_size, test_size):
        train_data = data.iloc[start:start + train_size]
        test_data = data.iloc[start + train_size:start + train_size + test_size]

        strategy.train(train_data)
        test_results = strategy.execute(test_data)

        results.append({
            "Train Period": (train_data.index[0], train_data.index[-1]),
            "Test Period": (test_data.index[0], test_data.index[-1]),
            "Metrics": calculate_metrics(test_results["Equity Curve"])
        })

    return results

# Metric calculations
def calculate_metrics(equity_curve):
    """
    Calculate performance metrics for a single equity curve.
    :param equity_curve: pd.Series of equity values over time.
    :return: Dictionary of metrics.
    """
    returns = equity_curve.pct_change().dropna()
    cumulative_return = equity_curve.iloc[-1] / equity_curve.iloc[0] - 1
    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252)
    sortino_ratio = returns.mean() / returns[returns < 0].std() * np.sqrt(252)
    max_drawdown = (equity_curve / equity_curve.cummax() - 1).min()
    
    return {
        "Cumulative Return": cumulative_return,
        "Sharpe Ratio": sharpe_ratio,
        "Sortino Ratio": sortino_ratio,
        "Max Drawdown": max_drawdown
    }

def consolidate_walk_forward_metrics(walk_forward_results):
    """
    Consolidate metrics across all walk-forward iterations.
    :param walk_forward_results: List of dictionaries with metrics for each iteration.
    :return: pd.DataFrame of metrics for all iterations.
    """
    metrics = []
    for iteration, result in enumerate(walk_forward_results):
        metrics.append({
            "Iteration": iteration + 1,
            "Cumulative Return": result["Metrics"]["Cumulative Return"],
            "Sharpe Ratio": result["Metrics"]["Sharpe Ratio"],
            "Sortino Ratio": result["Metrics"]["Sortino Ratio"],
            "Max Drawdown": result["Metrics"]["Max Drawdown"]
        })
    return pd.DataFrame(metrics)

# Visualizations
def plot_equity_curves(walk_forward_results, title="Aggregated Equity Curve"):
    """
    Plot equity curves from all walk-forward iterations.
    :param walk_forward_results: List of dictionaries with equity curves for each iteration.
    :param title: Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    for result in walk_forward_results:
        equity_curve = result["Metrics"]["Equity Curve"]
        plt.plot(equity_curve.index, equity_curve.values, alpha=0.5)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Equity")
    plt.grid()
    plt.show()

def plot_metrics_bar(metrics_df, metric_name, title=None):
    """
    Plot a bar chart for a specific metric across iterations.
    :param metrics_df: DataFrame of consolidated metrics.
    :param metric_name: Metric to plot.
    :param title: Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(metrics_df["Iteration"], metrics_df[metric_name], color="skyblue")
    plt.title(title or f"{metric_name} Across Walk-Forward Iterations")
    plt.xlabel("Iteration")
    plt.ylabel(metric_name)
    plt.grid()
    plt.show()

def plot_metrics_heatmap(metrics_df, title="Metrics Heatmap"):
    """
    Plot a heatmap of metrics across iterations.
    :param metrics_df: DataFrame of consolidated metrics.
    :param title: Title of the heatmap.
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(metrics_df.set_index("Iteration").T, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(title)
    plt.show()
