# File: data_pipeline/indicators.py
import pandas as pd

class IndicatorCalculator:
    @staticmethod
    def calculate_rsi(data, period=14):
        """Calcola l'RSI (Relative Strength Index)."""
        delta = data['Close'].diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
        """Calcola l'MACD (Moving Average Convergence Divergence)."""
        fast_ema = data['Close'].ewm(span=fast_period, adjust=False).mean()
        slow_ema = data['Close'].ewm(span=slow_period, adjust=False).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
        return macd_line, signal_line
