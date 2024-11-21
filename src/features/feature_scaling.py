# src/features/feature_scaling.py

from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaler:
    def __init__(self, data):
        self.data = data

    def min_max_scale(self, columns):
        """Applies Min-Max scaling to specified columns."""
        scaler = MinMaxScaler()
        self.data[columns] = scaler.fit_transform(self.data[columns])
    
    def standard_scale(self, columns):
        """Applies Standard scaling to specified columns."""
        scaler = StandardScaler()
        self.data[columns] = scaler.fit_transform(self.data[columns])
