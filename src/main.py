# src/main.py

import pandas as pd
from utils.config_loader import load_yaml_config
from utils.logger import setup_logger
from data.scripts.fetch_data import DataFetcher
from data.scripts.preprocess_data import DataPreprocessor
from features.feature_engineer import FeatureEngineer
from models.random_forest import RandomForestModel  # or any model you choose
from backtesting.backtester import Backtester
from backtesting.performance_metrics import calculate_drawdown, calculate_sortino_ratio
from backtesting.plot_results import plot_portfolio_value, plot_drawdown

def main():
    # Load configuration
    config = load_yaml_config('../config/app_config.yaml')
    
    # Set up logger
    logger = setup_logger('TradingSystemLogger')
    logger.info("Starting the trading algorithm system")

    # Step 1: Fetch Data
    logger.info("Fetching data...")
    data_fetcher = DataFetcher(
        tickers=config['data']['tickers'],
        start_date=config['data']['start_date'],
        end_date=config['data']['end_date'],
        interval=config['data']['interval']
    )
    data_fetcher.fetch_and_save()
    logger.info("Data fetching complete")

    # Step 2: Preprocess Data
    logger.info("Preprocessing data...")
    preprocessor = DataPreprocessor()
    preprocessor.preprocess()
    logger.info("Data preprocessing complete")

    # Step 3: Feature Engineering
    logger.info("Generating features...")
    # Load processed data
    data = pd.read_csv('../data/processed/AAPL.csv', index_col='Date', parse_dates=True)
    feature_engineer = FeatureEngineer(data)
    data_with_features = feature_engineer.generate_features()
    logger.info("Feature engineering complete")

    # Step 4: Train or Load Model
    logger.info("Training model...")
    X = data_with_features.drop(columns=['target'])  # Assuming target column is predefined
    y = data_with_features['target']  # Define target based on your objective

    # Train and save model
    model = RandomForestModel(data_with_features)
    model.train(X, y)
    logger.info("Model training complete")

    # Step 5: Backtesting
    logger.info("Running backtest...")
    # Generate trading signals based on the model's predictions
    predictions = model.predict(X)
    data_with_features['signal'] = predictions.apply(lambda x: 1 if x > 0 else -1)  # Example signal generation

    # Initialize and run backtest
    backtester = Backtester(data_with_features, signals=data_with_features['signal'])
    backtest_results = backtester.run_backtest()
    logger.info("Backtest complete")

    # Step 6: Calculate Performance Metrics
    logger.info("Calculating performance metrics...")
    metrics = backtester.get_performance_metrics()
    drawdown, max_drawdown = calculate_drawdown(backtest_results['portfolio_value'])
    sortino_ratio = calculate_sortino_ratio(backtest_results['net_return'])

    # Log performance metrics
    logger.info("Performance Metrics:")
    logger.info(metrics)
    logger.info(f"Maximum Drawdown: {max_drawdown:.2%}")
    logger.info(f"Sortino Ratio: {sortino_ratio:.2f}")

    # Step 7: Plot Results
    plot_portfolio_value(backtest_results)
    plot_drawdown(backtest_results['portfolio_value'])

    logger.info("Trading algorithm system run completed successfully")

if __name__ == "__main__":
    main()
