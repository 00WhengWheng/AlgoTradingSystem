from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def ml_trading_strategy(data, features, target):
    """
    Machine Learning-Based Trading Strategy using Random Forest.
    
    :param data: pd.DataFrame containing features and target.
    :param features: List of feature column names.
    :param target: Target column name.
    :return: Trained model and test accuracy.
    """
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Test model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Model Accuracy: {accuracy:.2f}")
    return model
