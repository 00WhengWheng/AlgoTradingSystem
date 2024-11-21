# src/features/feature_engineer.py

import pandas as pd
import yaml
from .technical_indicators import TechnicalIndicators
from .custom_features import CustomFeatures
from .feature_scaling import FeatureScaler

class FeatureEngineer:
    def __init__(self, data, config_path="feature_config.yaml"):
        self.data = data
        self.config = self.load_config(config_path)

    def load_config(self, config_path):
        """Loads feature configuration from YAML file."""
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        return config

    def generate_features(self):
        """Generates features as specified in the configuration."""
        # Technical indicators
        ti = TechnicalIndicators(self.data)
        if 'SMA' in self.config['technical_indicators']:
            ti.add_sma(window=self.config['technical_indicators']['SMA'])
        if 'EMA' in self.config['technical_indicators']:
            ti.add_ema(window=self.config['technical_indicators']['EMA'])
        if 'RSI' in self.config['technical_indicators']:
            ti.add_rsi(period=self.config['technical_indicators']['RSI'])

        # Custom features
        cf = CustomFeatures(self.data)
        if 'Volatility' in self.config['custom_features']:
            cf.add_volatility(window=self.config['custom_features']['Volatility'])
        if 'Momentum' in self.config['custom_features']:
            cf.add_momentum(window=self.config['custom_features']['Momentum'])
        if 'Bollinger_Bands' in self.config['custom_features']:
            cf.add_bollinger_bands(
                window=self.config['custom_features']['Bollinger_Bands']['window'],
                num_std=self.config['custom_features']['Bollinger_Bands']['num_std']
            )

        # Scaling
        if 'scaling' in self.config:
            scaler = FeatureScaler(self.data)
            if 'min_max' in self.config['scaling']:
                scaler.min_max_scale(columns=self.config['scaling']['min_max'])
            if 'standard' in self.config['scaling']:
                scaler.standard_scale(columns=self.config['scaling']['standard'])

        return self.data
