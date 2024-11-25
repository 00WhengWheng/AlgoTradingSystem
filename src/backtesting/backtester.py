# File: src/backtesting/backtester.py
from backtesting.walk_forward import WalkForwardPipeline
from backtesting.performance_analyzer import PerformanceAnalyzer
from data.indicators import calculate_rsi
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, data, strategy_name="Strategy"):
        self.data = data
        self.strategy_name = strategy_name
        self.results = None

    def run_strategy(self, signal_column, initial_capital=10000, transaction_cost=0.001):
        data = self.data.copy()
        data["Position"] = data[signal_column].shift()
        data["Market Return"] = data["Close"].pct_change()
        data["Strategy Return"] = data["Market Return"] * data["Position"]
        data["Transaction Costs"] = transaction_cost * data["Position"].diff().abs()
        data["Net Strategy Return"] = data["Strategy Return"] - data["Transaction Costs"]

        data["Cumulative Strategy"] = (1 + data["Net Strategy Return"]).cumprod()
        self.results = data
        return PerformanceAnalyzer.calculate(data, initial_capital)

    def plot_results(self):
        plt.plot(self.results["Cumulative Strategy"], label="Strategy")
        plt.legend()
        plt.show()
