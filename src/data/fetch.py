import yfinance as yf
import os
import pandas as pd
import pickle
from concurrent.futures import ThreadPoolExecutor
import logging
import time

class DataFetcher:
    """
    Intelligent data fetching system with advanced error handling.
    """
    def __init__(self, raw_data_dir="data/raw_data", cache_dir="data/cache", log_file="data_fetcher.log"):
        """
        Initialize the DataFetcher.
        :param raw_data_dir: Directory where raw CSV data will be stored.
        :param cache_dir: Directory where cached binary data will be stored.
        :param log_file: Path to the log file for error reporting.
        """
        self.raw_data_dir = raw_data_dir
        self.cache_dir = cache_dir
        os.makedirs(self.raw_data_dir, exist_ok=True)
        os.makedirs(self.cache_dir, exist_ok=True)
        logging.basicConfig(filename=log_file, level=logging.ERROR, format="%(asctime)s - %(message)s")
        self.log_file = log_file

    def _log_error(self, message):
        """
        Log an error message to the log file.
        """
        print(f"ERROR: {message}")
        logging.error(message)

    def _get_file_path(self, ticker, interval, extension="csv"):
        if extension == "csv":
            return os.path.join(self.raw_data_dir, f"{ticker}_{interval}.csv")
        elif extension == "pkl":
            return os.path.join(self.cache_dir, f"{ticker}_{interval}.pkl")
        raise ValueError("Unsupported file extension.")

    def _load_cached_data(self, ticker, interval):
        file_path = self._get_file_path(ticker, interval, extension="pkl")
        if os.path.exists(file_path):
            print(f"Loading cached data for {ticker} at {interval}.")
            with open(file_path, "rb") as f:
                return pickle.load(f)
        return None

    def _cache_data(self, data, ticker, interval):
        file_path = self._get_file_path(ticker, interval, extension="pkl")
        with open(file_path, "wb") as f:
            pickle.dump(data, f)
        print(f"Data for {ticker} cached in {file_path}.")

    def _is_data_up_to_date(self, file_path, end_date):
        if not os.path.exists(file_path):
            return False
        try:
            data = pd.read_csv(file_path, parse_dates=["Date"])
            return data["Date"].max() >= pd.to_datetime(end_date)
        except Exception as e:
            self._log_error(f"Error reading file {file_path}: {e}")
            return False

    def validate_data(self, data):
        if data.isnull().any().any():
            print("Data contains missing values. Filling them with forward fill.")
            data.fillna(method="ffill", inplace=True)
        if data.empty:
            raise ValueError("Data is empty after validation.")
        return data

    def fetch(self, ticker, start_date, end_date, interval="1d", retries=3, delay=5):
        file_path = self._get_file_path(ticker, interval)
        
        if self._is_data_up_to_date(file_path, end_date):
            print(f"Data for {ticker} at {interval} is up to date.")
            try:
                data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
                return self.validate_data(data)
            except Exception as e:
                self._log_error(f"Error loading existing data for {ticker}: {e}")

        # Retry mechanism
        for attempt in range(1, retries + 1):
            try:
                print(f"Fetching data for {ticker}, attempt {attempt}...")
                data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
                if data.empty:
                    raise ValueError(f"No data found for ticker {ticker}.")
                data.to_csv(file_path)
                data = self.validate_data(data)
                self._cache_data(data, ticker, interval)
                return data
            except Exception as e:
                self._log_error(f"Attempt {attempt} failed for {ticker}: {e}")
                if attempt < retries:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)

        raise RuntimeError(f"Failed to fetch data for {ticker} after {retries} attempts.")

    def fetch_multiple(self, tickers, start_date, end_date, interval="1d", max_workers=5):
        results = {}

        def fetch_ticker(ticker):
            try:
                results[ticker] = self.fetch(ticker, start_date, end_date, interval)
            except Exception as e:
                self._log_error(f"Failed to fetch data for {ticker}: {e}")

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            executor.map(fetch_ticker, tickers)

        return results
