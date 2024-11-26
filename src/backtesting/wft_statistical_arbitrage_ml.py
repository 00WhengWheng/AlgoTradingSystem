_import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def wft_statistical_arbitrage(data, feature_cols, target_col, train_size, test_size):
    """
    Walk-Forward Test for Statistical Arbitrage using Machine Learning.
    
    Parameters:
        data (pd.DataFrame): DataFrame containing features and target.
        feature_cols (list): Columns to use as features for the model.
        target_col (str): Column representing the target spread to predict.
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
        
        # Prepare features and target
        X_train = train_data[feature_cols]
        y_train = train_data[target_col]
        X_test = test_data[feature_cols]
        y_test = test_data[target_col]
        
        # Train model
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        
        # Predict and evaluate
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        
        # Log results
        results.append({
            'start_date': test_data.index[0],
            'end_date': test_data.index[-1],
            'mse': mse
        })
        
        # Move window forward
        start += test_size
    
    return pd.DataFrame(results)
