import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_squared_error

class LSTMModel(BaseModel):
    def __init__(self, input_shape):
        self.model = self._build_model(input_shape)

    def _build_model(self, input_shape):
        model = tf.keras.Sequential([
            tf.keras.layers.LSTM(50, return_sequences=True, input_shape=input_shape),
            tf.keras.layers.LSTM(50),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)

    def predict(self, X):
        return self.model.predict(X)

    def evaluate(self, X_val, y_val):
        predictions = self.predict(X_val)
        return {"RMSE": mean_squared_error(y_val, predictions, squared=False)}
