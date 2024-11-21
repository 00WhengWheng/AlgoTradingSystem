# models/xgboost_model.py

import xgboost as xgb
from .base_model import BaseModel

class XGBoostModel(BaseModel):
    def __init__(self, data, params=None):
        super().__init__(data, params)
        self.model = xgb.XGBRegressor(**params)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X):
        return self.model.predict(X)
