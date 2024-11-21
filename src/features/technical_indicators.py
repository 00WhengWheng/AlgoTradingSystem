# src/features/technical_indicators.py

import pandas as pd
from .base_features import BaseFeature

class TechnicalIndicators(BaseFeature):
    def __init__(self, data):
        super().__init__(data)

    def add_sma(self, window=50):
        """Adds Simple Moving Average (SMA) feature."""
        self.data[f'SMA_{window}'] = self.data['Close'].rolling(window=window).mean()

    def add_ema(self, window=50):
        """Adds Exponential Moving Average (EMA) feature."""
        self.data[f'EMA_{window}'] = self.data['Close'].ewm(span=window, adjust=False).mean()

    def add_rsi(self, period=14):
        """Adds Relative Strength Index (RSI) feature."""
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
