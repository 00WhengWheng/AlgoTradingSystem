import os
import pandas as pd
import numpy as np

class DataProcessor:
    """
    A modular system for processing and cleaning financial data.
    """
    def __init__(self, raw_data_dir="data/raw_data", processed_data_dir="data/processed_data"):
        """
        Initialize the DataProcessor.
        :param raw_data_dir: Directory containing raw data.
        :param processed_data_dir: Directory where processed data will be stored.
        """
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir
        os.makedirs(self.processed_data_dir, exist_ok=True)

    def load_data(self, ticker, interval="1d"):
        """
        Load raw data for a given ticker.
        :param ticker: Ticker symbol.
        :param interval: Data interval (e.g., '1d', '1h').
        :return: DataFrame with raw data.
        """
        file_path = os.path.join(self.raw_data_dir, f"{ticker}_{interval}.csv")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No raw data found for {ticker} at interval {interval}.")
        data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
        return data

    def clean_data(self, data):
        """
        Clean the data by filling missing values and removing duplicates.
        :param data: DataFrame with raw data.
        :return: Cleaned DataFrame.
        """
        print("Cleaning data...")
        data = data.drop_duplicates()
        data = data.fillna(method="ffill").fillna(method="bfill")  # Fill missing values
        if data.isnull().any().any():
            raise ValueError("Data still contains missing values after cleaning.")
        return data

    def add_indicators(self, data):
        """
        Add basic technical indicators to the data.
        :param data: Cleaned DataFrame.
        :return: DataFrame with added indicators.
        """
        print("Adding technical indicators...")
        data["SMA_20"] = data["Close"].rolling(window=20).mean()  # 20-period SMA
        data["EMA_20"] = data["Close"].ewm(span=20).mean()        # 20-period EMA
        data["Volatility"] = data["Close"].rolling(window=20).std()  # Rolling volatility
        data["RSI"] = self._calculate_rsi(data["Close"], window=14)  # Relative Strength Index
        data["Bollinger_Upper"] = data["SMA_20"] + 2 * data["Volatility"]  # Bollinger Upper Band
        data["Bollinger_Lower"] = data["SMA_20"] - 2 * data["Volatility"]  # Bollinger Lower Band
        return data

    def _calculate_rsi(self, prices, window=14):
        """
        Calculate Relative Strength Index (RSI).
        :param prices: Series of prices.
        :param window: RSI calculation period.
        :return: Series of RSI values.
        """
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def scale_data(self, data, columns=None):
        """
        Scale specified columns using Min-Max scaling.
        :param data: DataFrame with data to scale.
        :param columns: List of columns to scale. If None, scale all numeric columns.
        :return: DataFrame with scaled data.
        """
        print("Scaling data...")
        columns = columns or data.select_dtypes(include=np.number).columns
        for column in columns:
            min_val = data[column].min()
            max_val = data[column].max()
            data[column] = (data[column] - min_val) / (max_val - min_val)
        return data

    def process_and_save(self, ticker, interval="1d"):
        """
        Process raw data and save it to the processed data directory.
        :param ticker: Ticker symbol.
        :param interval: Data interval (e.g., '1d', '1h').
        :return: Processed DataFrame.
        """
        print(f"Processing data for {ticker}...")
        data = self.load_data(ticker, interval)
        data = self.clean_data(data)
        data = self.add_indicators(data)
        processed_file_path = os.path.join(self.processed_data_dir, f"{ticker}_{interval}_processed.csv")
        data.to_csv(processed_file_path)
        print(f"Processed data saved to {processed_file_path}")
        return data
