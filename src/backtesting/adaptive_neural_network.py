from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.metrics import mean_squared_error

def wft_adaptive_neural_network(data, feature_cols, target_col, seq_length, train_size, test_size):
    """
    Walk-Forward Test for Adaptive Neural Network Strategy.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing features and target data.
        feature_cols (list): Columns representing features for the neural network.
        target_col (str): Column representing the target variable.
        seq_length (int): Length of sequences for LSTM input.
        train_size (int): Number of rows in the in-sample (training) data.
        test_size (int): Number of rows in the out-of-sample (testing) data.
    
    Returns:
        pd.DataFrame: Out-of-sample performance metrics for each iteration.
    """
    results = []
    start = 0
    
    while start + train_size + test_size <= len(data):
        # Define training and testing data
        train_data = data.iloc[start:start + train_size]
        test_data = data.iloc[start + train_size:start + train_size + test_size]
        
        # Prepare sequential data
        X_train, y_train = create_sequences(train_data[feature_cols + [target_col]].values, seq_length)
        X_test, y_test = create_sequences(test_data[feature_cols + [target_col]].values, seq_length)
        
        # Reshape for LSTM
        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], len(feature_cols)))
        X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], len(feature_cols)))
        
        # Build LSTM model
        model = Sequential([
            LSTM(50, activation='relu', return_sequences=True, input_shape=(seq_length, len(feature_cols))),
            Dropout(0.2),
            LSTM(50, activation='relu'),
            Dropout(0.2),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        
        # Train model
        early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stop], verbose=0)
        
        # Test model
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        
        # Calculate directional accuracy
        actual_direction = np.sign(y_test)
        predicted_direction = np.sign(predictions.flatten())
        directional_accuracy = (actual_direction == predicted_direction).mean()
        
        # Log results
        results.append({
            'start_date': test_data.index[0],
            'end_date': test_data.index[-1],
            'mse': mse,
            'directional_accuracy': directional_accuracy
        })
        
        # Move window forward
        start += test_size
    
    return pd.DataFrame(results)
