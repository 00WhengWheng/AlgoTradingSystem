# src/backtesting/plot_results.py

import matplotlib.pyplot as plt

def plot_portfolio_value(results):
    """
    Plots the portfolio value over time.
    
    Parameters:
    - results (pd.DataFrame): DataFrame with portfolio value over time.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(results['portfolio_value'], label="Portfolio Value")
    plt.title("Portfolio Value Over Time")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.show()

def plot_drawdown(portfolio_values):
    """
    Plots the drawdown over time.
    
    Parameters:
    - portfolio_values (pd.Series): Series of portfolio values over time.
    """
    peak = portfolio_values.cummax()
    drawdown = (portfolio_values - peak) / peak
    plt.figure(figsize=(12, 6))
    plt.plot(drawdown, label="Drawdown", color='red')
    plt.title("Drawdown Over Time")
    plt.xlabel("Date")
    plt.ylabel("Drawdown (%)")
    plt.legend()
    plt.show()
