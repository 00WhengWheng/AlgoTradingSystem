import matplotlib.pyplot as plt
import plotly.graph_objects as go

class VisualizationManager:
    """
    Manages graphical visualization of trading strategy results.
    """
    def __init__(self):
        pass

    def plot_equity_curve(self, equity, title="Equity Curve"):
        """
        Plot the equity curve.
        :param equity: pd.Series of equity values over time.
        :param title: Title of the plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(equity.index, equity.values, label="Equity", linewidth=2, color="blue")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Equity")
        plt.legend()
        plt.grid()
        plt.show()

    def plot_trading_signals(self, prices, signals, title="Trading Signals"):
        """
        Plot trading signals on a price chart.
        :param prices: pd.Series of prices.
        :param signals: pd.DataFrame with 'Buy' and 'Sell' signals.
        :param title: Title of the plot.
        """
        plt.figure(figsize=(12, 8))
        plt.plot(prices.index, prices.values, label="Price", color="blue", linewidth=1.5)
        plt.scatter(signals[signals["Signal"] == "Buy"].index, 
                    prices[signals["Signal"] == "Buy"], label="Buy Signal", marker="^", color="green", s=100)
        plt.scatter(signals[signals["Signal"] == "Sell"].index, 
                    prices[signals["Signal"] == "Sell"], label="Sell Signal", marker="v", color="red", s=100)
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

    def plot_candlestick(self, data, title="Candlestick Chart"):
        """
        Plot a candlestick chart.
        :param data: pd.DataFrame with columns ['Date', 'Open', 'High', 'Low', 'Close'].
        :param title: Title of the chart.
        """
        fig = go.Figure(data=[go.Candlestick(
            x=data['Date'],
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            increasing_line_color='green',
            decreasing_line_color='red'
        )])
        fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Price")
        fig.show()

    def plot_cumulative_returns(self, returns, title="Cumulative Returns"):
        """
        Plot cumulative returns over time.
        :param returns: pd.Series of cumulative returns.
        :param title: Title of the plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(returns.index, returns.values, label="Cumulative Returns", linewidth=2, color="green")
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Cumulative Returns")
        plt.legend()
        plt.grid()
        plt.show()
