import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MarketScenarioSimulator:
    def __init__(self, data):
        """
        Initialize the simulator with historical data.
        Args:
        - data (pd.DataFrame): Historical data with 'Close' prices.
        """
        self.data = data

    def simulate_trending_market(self, trend_strength=0.001):
        """
        Simulate a trending market by applying a linear trend to the data.
        Args:
        - trend_strength (float): Slope of the trend.
        """
        trend = np.linspace(1, 1 + trend_strength * len(self.data), len(self.data))
        self.data["Trending_Close"] = self.data["Close"] * trend
        return self.data["Trending_Close"]

    def simulate_range_bound_market(self, range_amplitude=0.02):
        """
        Simulate a range-bound market by adding sinusoidal noise to the data.
        Args:
        - range_amplitude (float): Amplitude of the oscillations.
        """
        oscillation = np.sin(np.linspace(0, 2 * np.pi, len(self.data))) * range_amplitude * self.data["Close"].mean()
        self.data["Range_Bound_Close"] = self.data["Close"] + oscillation
        return self.data["Range_Bound_Close"]

    def simulate_high_volatility_market(self, volatility_factor=2.0):
        """
        Simulate a high-volatility market by amplifying price changes.
        Args:
        - volatility_factor (float): Factor to amplify volatility.
        """
        returns = self.data["Close"].pct_change()
        amplified_returns = returns * volatility_factor
        self.data["High_Volatility_Close"] = self.data["Close"].iloc[0] * (1 + amplified_returns).cumprod()
        return self.data["High_Volatility_Close"]

    def simulate_black_swan_event(self, drop_percent=30):
        """
        Simulate a black swan event by introducing a sudden price drop.
        Args:
        - drop_percent (float): Percentage drop in price.
        """
        shock_index = int(len(self.data) * 0.8)  # Drop near the end
        self.data["Black_Swan_Close"] = self.data["Close"].copy()
        self.data.loc[shock_index:, "Black_Swan_Close"] *= (1 - drop_percent / 100)
        return self.data["Black_Swan_Close"]

    def visualize_scenarios(self):
        """
        Plot all simulated market scenarios.
        """
        plt.figure(figsize=(12, 8))
        for column in self.data.columns:
            if "Close" in column and column != "Close":
                plt.plot(self.data.index, self.data[column], label=column)
        plt.plot(self.data.index, self.data["Close"], label="Original Close", linestyle="--")
        plt.title("Simulated Market Scenarios")
        plt.legend()
        plt.grid()
        plt.show()


def visualize_strategy_performance(results):
    scenarios = list(results.keys())
    metrics = ["Total Return", "Sharpe Ratio", "Max Drawdown"]

    for metric in metrics:
        values = [results[scenario][metric] for scenario in scenarios]
        plt.figure(figsize=(10, 6))
        plt.bar(scenarios, values)
        plt.title(f"Strategy Performance - {metric}")
        plt.ylabel(metric)
        plt.xticks(rotation=45)
        plt.grid(axis="y")
        plt.show()
