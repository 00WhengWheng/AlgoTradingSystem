from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def supervised_price_prediction(data, features, target):
    """
    Supervised Learning for Price Prediction.
    
    :param data: pd.DataFrame containing features and target.
    :param features: List of feature column names.
    :param target: Target column name (e.g., future price).
    :return: Trained model and prediction error.
    """
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train Gradient Boosting Regressor
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
    model.fit(X_train, y_train)
    
    # Test the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    
    print(f"Model Mean Squared Error: {mse:.2f}")
    return model, mse
