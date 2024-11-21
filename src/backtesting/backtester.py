import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, data, strategy_name="Strategy"):
        """
        Initialize the backtester with historical data and a strategy name.
        Args:
        - data (pd.DataFrame): Historical data with 'Open', 'High', 'Low', 'Close' prices.
        - strategy_name (str): Name of the strategy.
        """
        self.data = data
        self.strategy_name = strategy_name
        self.results = None

    def run_strategy(self, signal_column, initial_capital=10000, transaction_cost=0.001):
        """
        Run the backtesting strategy.
        Args:
        - signal_column (str): Column in the data that contains buy/sell signals.
        - initial_capital (float): Starting capital for the backtest.
        - transaction_cost (float): Proportional transaction cost per trade.
        """
        data = self.data.copy()
        data["Position"] = data[signal_column].shift()  # Use signal to determine positions
        data["Market Return"] = data["Close"].pct_change()
        data["Strategy Return"] = data["Market Return"] * data["Position"]
        data["Transaction Costs"] = transaction_cost * np.abs(data["Position"].diff())
        data["Net Strategy Return"] = data["Strategy Return"] - data["Transaction Costs"]

        # Calculate cumulative performance
        data["Cumulative Market"] = (1 + data["Market Return"]).cumprod()
        data["Cumulative Strategy"] = (1 + data["Net Strategy Return"]).cumprod()

        # Store results
        self.results = data
        self.results["Portfolio Value"] = initial_capital * self.results["Cumulative Strategy"]
        self.results["Drawdown"] = self.calculate_drawdown(self.results["Portfolio Value"])

        # Performance metrics
        performance = self.calculate_performance(initial_capital)
        return performance

    def calculate_drawdown(self, portfolio_value):
        """
        Calculate the drawdowns of the portfolio.
        """
        rolling_max = portfolio_value.cummax()
        drawdown = (portfolio_value - rolling_max) / rolling_max
        return drawdown

    def calculate_performance(self, initial_capital):
        """
        Calculate key performance metrics.
        """
        total_return = (self.results["Portfolio Value"].iloc[-1] / initial_capital) - 1
        sharpe_ratio = self.calculate_sharpe_ratio(self.results["Net Strategy Return"])
        max_drawdown = self.results["Drawdown"].min()

        return {
            "Total Return": total_return,
            "Sharpe Ratio": sharpe_ratio,
            "Max Drawdown": max_drawdown,
        }

    def calculate_sharpe_ratio(self, strategy_returns, risk_free_rate=0.01):
        """
        Calculate Sharpe ratio for the strategy.
        """
        excess_returns = strategy_returns - (risk_free_rate / 252)
        sharpe_ratio = np.sqrt(252) * excess_returns.mean() / excess_returns.std()
        return sharpe_ratio

    def plot_results(self):
        """
        Plot the equity curve and drawdown.
        """
        if self.results is None:
            print("No results to plot. Run a strategy first.")
            return

        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.plot(self.results["Portfolio Value"], label="Strategy Portfolio Value")
        plt.plot(self.results["Cumulative Market"] * self.results["Portfolio Value"].iloc[0], label="Market Portfolio Value")
        plt.title(f"{self.strategy_name} - Portfolio Value")
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(self.results["Drawdown"], label="Drawdown")
        plt.title(f"{self.strategy_name} - Drawdown")
        plt.legend()

        plt.tight_layout()
        plt.show()
