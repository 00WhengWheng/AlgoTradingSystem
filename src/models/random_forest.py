# models/random_forest.py

from sklearn.ensemble import RandomForestRegressor
from .base_model import BaseModel

class RandomForestModel(BaseModel):
    def __init__(self, data, n_estimators=100, max_depth=None, params=None):
        super().__init__(data, params)
        self.model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
