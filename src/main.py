from models.linear_regression import LinearRegressionModel
from models.lstm_model import LSTMModel
from models.model_ensemble import ModelEnsemble
from models.optimization import MarkowitzOptimizer
from data.collector import DataCollector
from features.feature_engineer import FeatureEngineer
from backtesting.backtester import Backtester

def main():
    # Step 1: Data Collection
    collector = DataCollector()
    data = collector.fetch_from_yfinance("AAPL", "2020-01-01", "2023-01-01")
    data = FeatureEngineer.add_feature(data)

    # Step 2: Prepare Data
    X_train, X_val, X_test, y_train, y_val, y_test = prepare_data(data)

    # Step 3: Train Models
    linear_model = LinearRegressionModel()
    linear_model.train(X_train, y_train)
    lstm_model = LSTMModel(input_shape=(X_train.shape[1], X_train.shape[2]))
    lstm_model.train(X_train, y_train)

    # Step 4: Evaluate Models
    print("Linear Model Performance:", linear_model.evaluate(X_val, y_val))
    print("LSTM Model Performance:", lstm_model.evaluate(X_val, y_val))

    # Step 5: Combine Predictions
    ensemble = ModelEnsemble({"Linear": linear_model, "LSTM": lstm_model})
    predictions = ensemble.predict(X_test)

    # Step 6: Backtesting
    data["Signal"] = predictions
    backtester = Backtester(data, "Ensemble Strategy")
    performance = backtester.run_strategy(signal_column="Signal", initial_capital=10000)
    print("Ensemble Strategy Performance:", performance)
