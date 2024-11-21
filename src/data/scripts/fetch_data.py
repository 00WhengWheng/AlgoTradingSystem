import os
import time
import logging
import yfinance as yf
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import HTTPError, ConnectionError

# Set up logging
logging.basicConfig(filename='../data/logs/data_fetch.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataFetcher:
    def __init__(self, tickers, start_date, end_date, interval='1d', data_dir='../data/raw',
                 max_retries=3, num_threads=5):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.interval = interval
        self.data_dir = data_dir
        self.max_retries = max_retries
        self.num_threads = num_threads
        os.makedirs(self.data_dir, exist_ok=True)

    def fetch_ticker_data(self, ticker):
        """
        Fetch data for a single ticker with retry logic.
        """
        retries = 0
        success = False
        while retries < self.max_retries and not success:
            try:
                logging.info(f"Fetching data for {ticker}...")
                data = yf.download(ticker, start=self.start_date, end=self.end_date, interval=self.interval)
                
                if data.empty:
                    logging.warning(f"No data returned for {ticker}. Check if the ticker is valid.")
                    return None

                # Save data to CSV
                file_path = os.path.join(self.data_dir, f"{ticker}.csv")
                data.to_csv(file_path)
                logging.info(f"Successfully saved data for {ticker} to {file_path}")
                success = True
                return ticker  # Return ticker name if successful

            except (HTTPError, ConnectionError) as e:
                retries += 1
                logging.error(f"Error fetching data for {ticker}: {e}. Retrying ({retries}/{self.max_retries})...")
                time.sleep(2 ** retries)  # Exponential backoff

            except Exception as e:
                logging.error(f"Unexpected error for {ticker}: {e}")
                break  # Exit retry loop for unknown errors

        logging.error(f"Failed to fetch data for {ticker} after {self.max_retries} retries.")
        return None

    def validate_data(self, file_path):
        """
        Perform basic validation on the fetched data.
        """
        try:
            data = pd.read_csv(file_path)
            if data.isnull().values.any():
                logging.warning(f"Data in {file_path} contains missing values.")
            return True
        except Exception as e:
            logging.error(f"Error validating data in {file_path}: {e}")
            return False

    def fetch_and_save_all(self):
        """
        Fetch data for all tickers using parallel execution.
        """
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            results = list(executor.map(self.fetch_ticker_data, self.tickers))

        successful_tickers = [ticker for ticker in results if ticker is not None]
        failed_tickers = set(self.tickers) - set(successful_tickers)
        
        logging.info(f"Successfully fetched data for: {successful_tickers}")
        logging.warning(f"Failed to fetch data for: {failed_tickers}")

# Example usage
if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOG", "INVALIDTICKER"]
    fetcher = DataFetcher(tickers=tickers, start_date="2020-01-01", end_date="2023-01-01", num_threads=3)
    fetcher.fetch_and_save_all()
