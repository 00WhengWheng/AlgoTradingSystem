# File: backtesting/performance_analyzer.py
import matplotlib.pyplot as plt

class PerformanceAnalyzer:
    @staticmethod
    def plot_equity_curve(trades):
        equity = [trade['equity'] for trade in trades]
        plt.plot(equity)
        plt.title("Equity Curve")
        plt.xlabel("Trades")
        plt.ylabel("Equity")
        plt.show()
