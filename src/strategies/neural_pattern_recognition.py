from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

def pattern_recognition_nn(prices):
    """
    Pattern Recognition with Neural Networks.
    
    :param prices: pd.Series of historical price data.
    :return: Trained model for pattern recognition.
    """
    # Preprocess data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(prices.values.reshape(-1, 1))
    
    # Prepare dataset
    X, y = [], []
    for i in range(len(scaled_prices) - 5):
        X.append(scaled_prices[i:i+5])
        y.append(scaled_prices[i+5])
    X, y = np.array(X), np.array(y)
    
    # Build LSTM model
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)),
        LSTM(50, return_sequences=False),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    # Train the model
    model.fit(X, y, batch_size=32, epochs=10, verbose=1)
    
    print("Pattern Recognition Model Trained")
    return model
