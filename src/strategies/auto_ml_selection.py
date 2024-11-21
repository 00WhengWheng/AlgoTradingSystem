from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

def auto_ml_strategy_selection(data, features, target):
    """
    Auto-ML for Strategy Selection.
    
    :param data: pd.DataFrame containing features and target.
    :param features: List of feature column names.
    :param target: Target column name (e.g., future price).
    :return: Best performing model pipeline.
    """
    X = data[features]
    y = data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # TPOT AutoML
    tpot = TPOTRegressor(generations=5, population_size=50, verbosity=2, random_state=42)
    tpot.fit(X_train, y_train)
    
    # Evaluate model
    score = tpot.score(X_test, y_test)
    print(f"AutoML Best Model Score: {score:.2f}")
    
    return tpot
