"""
# File: data_pipeline/indicators.py
import pandas as pd

class IndicatorCalculator:
    @staticmethod
    def calculate_rsi(data, period=14):
        #Calcola l'RSI (Relative Strength Index).
        delta = data['Close'].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
        #Calcola l'MACD (Moving Average Convergence Divergence).
        fast_ema = data['Close'].ewm(span=fast_period, adjust=False).mean()
        slow_ema = data['Close'].ewm(span=slow_period, adjust=False).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
        return macd_line, signal_line
"""

import yfinance as yf
import pandas as pd
import numpy as np
from py_vollib.black_scholes.greeks.analytical import delta, gamma, theta, vega
from yahoo_fin import options
from alpha_vantage.fundamentaldata import FundamentalData
import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Alpha Vantage API key (replace with your actual key)
ALPHA_VANTAGE_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
FRED_API_KEY = "YOUR_FRED_API_KEY"

def fetch_risk_free_rate():
    """
    Fetch the 10-year Treasury Yield as the risk-free rate using FRED API.
    """
    try:
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&api_key={FRED_API_KEY}&file_type=json"
        response = requests.get(url).json()
        observations = response['observations']
        latest_yield = float(observations[-1]['value']) / 100  # Convert to decimal
        return latest_yield
    except Exception as e:
        print(f"Error fetching risk-free rate: {e}")
        return 0.01  # Default to 1% if error

def fetch_implied_volatility(ticker):
    """
    Fetch the implied volatility from Yahoo Finance options data.
    """
    try:
        expiration_dates = options.get_expiration_dates(ticker)
        if not expiration_dates:
            raise ValueError("No expiration dates found for the ticker.")
        
        # Get the first expiration date's options chain
        options_chain = options.get_options_chain(ticker, expiration_dates[0])
        calls_iv = options_chain['calls']['Implied Volatility']
        puts_iv = options_chain['puts']['Implied Volatility']
        
        # Calculate average implied volatility
        avg_iv = (calls_iv.mean() + puts_iv.mean()) / 2
        return avg_iv
    except Exception as e:
        print(f"Error fetching implied volatility: {e}")
        return 0.25  # Default to 25% if error

def calculate_greeks(S, K, T, r, sigma, option_type='c'):
    """
    Calculate Greeks for an option using py_vollib.
    """
    try:
        greeks = {
            "Delta": delta(option_type, S, K, T, r, sigma),
            "Gamma": gamma(option_type, S, K, T, r, sigma),
            "Theta": theta(option_type, S, K, T, r, sigma),
            "Vega": vega(option_type, S, K, T, r, sigma),
        }
        return greeks
    except Exception as e:
        print(f"Error calculating Greeks: {e}")
        return {"Delta": None, "Gamma": None, "Theta": None, "Vega": None}

def fetch_and_calculate_indicators(ticker, start_date, end_date):
    """
    Fetch historical data and calculate indicators, including Greeks.
    """
    # Fetch stock data
    data = yf.download(ticker, start=start_date, end=end_date, interval="1d")
    
    # Moving Averages
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
    
    # RSI
    def calculate_rsi(series, period=14):
        delta = series.diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    data['RSI_14'] = calculate_rsi(data['Close'])
    
    # Bollinger Bands
    data['BB_Middle'] = data['Close'].rolling(window=20).mean()
    data['BB_Upper'] = data['BB_Middle'] + 2 * data['Close'].rolling(window=20).std()
    data['BB_Lower'] = data['BB_Middle'] - 2 * data['Close'].rolling(window=20).std()
    
    # Historical Volatility
    data['Daily_Return'] = data['Close'].pct_change()
    data['HV_20'] = data['Daily_Return'].rolling(window=20).std() * np.sqrt(252)
    
    # Fetch risk-free rate and implied volatility
    r = fetch_risk_free_rate()
    sigma = fetch_implied_volatility(ticker)

    # Option Greeks (Example: Last close as underlying price)
    S = data['Close'].iloc[-1]  # Last closing price
    K = round(S)  # Example: Use the closest strike price
    T = 30 / 365  # Example: 30 days to expiration
    greeks = calculate_greeks(S, K, T, r, sigma)
    
    # Add Greeks to DataFrame
    data['Delta'] = greeks['Delta']
    data['Gamma'] = greeks['Gamma']
    data['Theta'] = greeks['Theta']
    data['Vega'] = greeks['Vega']
    
    # Save to CSV
    filename = f"{ticker}_indicators.csv"
    data.to_csv(filename)
    print(f"Indicators saved to {filename}")
    
    return data

# Example Usage
ticker = "AAPL"
start_date = "2023-01-01"
end_date = "2023-11-24"

data = fetch_and_calculate_indicators(ticker, start_date, end_date)

# Visualization Example
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close', color='blue')
plt.plot(data['SMA_50'], label='SMA 50', color='orange')
plt.plot(data['BB_Upper'], label='Bollinger Upper', color='red', linestyle='--')
plt.plot(data['BB_Lower'], label='Bollinger Lower', color='green', linestyle='--')
plt.legend()
plt.title(f'Indicators for {ticker}')
plt.show()
