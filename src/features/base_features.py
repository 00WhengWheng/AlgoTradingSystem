# src/features/base_features.py

class BaseFeature:
    def __init__(self, data):
        """
        Base class for feature engineering.
        
        Parameters:
        - data (pd.DataFrame): DataFrame containing historical price data.
        """
        self.data = data

    def add_feature(self):
        """
        Abstract method to add features. Each feature class will implement its own logic.
        """
        raise NotImplementedError("Each feature must implement the add_feature method.")
