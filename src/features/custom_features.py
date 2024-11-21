# src/features/custom_features.py

import pandas as pd
import numpy as np
from .base_features import BaseFeature

class CustomFeatures(BaseFeature):
    def __init__(self, data):
        super().__init__(data)

    def add_volatility(self, window=20):
        """Adds rolling volatility feature."""
        self.data[f'Volatility_{window}'] = self.data['Close'].rolling(window=window).std()

    def add_momentum(self, window=10):
        """Adds momentum indicator as a custom feature."""
        self.data[f'Momentum_{window}'] = self.data['Close'].pct_change(periods=window)

    def add_bollinger_bands(self, window=20, num_std=2):
        """Adds Bollinger Bands (upper and lower) as custom features."""
        rolling_mean = self.data['Close'].rolling(window=window).mean()
        rolling_std = self.data['Close'].rolling(window=window).std()
        self.data['Bollinger_Upper'] = rolling_mean + (rolling_std * num_std)
        self.data['Bollinger_Lower'] = rolling_mean - (rolling_std * num_std)
