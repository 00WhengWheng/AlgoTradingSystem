import yfinance as yf
import requests
import logging

class DataCollector:
    def fetch_from_yfinance(self, symbol, start_date, end_date, interval="1d"):
        """Fetch data from yFinance."""
        logging.info(f"Fetching data from yFinance for {symbol}.")
        try:
            data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
            data.reset_index(inplace=True)
            data.rename(columns={"Date": "date_time"}, inplace=True)
            return data
        except Exception as e:
            logging.error(f"Failed to fetch data from yFinance: {str(e)}")
            raise

    def fetch_from_alpha_vantage(self, symbol, api_key, function="TIME_SERIES_DAILY"):
        """Fetch data from Alpha Vantage."""
        logging.info(f"Fetching data from Alpha Vantage for {symbol}.")
        url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"Failed to fetch data from Alpha Vantage: {str(e)}")
            raise
