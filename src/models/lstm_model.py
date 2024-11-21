# models/lstm_model.py

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from .base_model import BaseModel

class LSTMModel(BaseModel):
    def __init__(self, data, input_shape, units=50, params=None):
        super().__init__(data, params)
        self.model = Sequential([
            LSTM(units, input_shape=input_shape, return_sequences=True),
            LSTM(units),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)

    def predict(self, X):
        return self.model.predict(X)
