# File: data_pipeline/preprocessor.py
import pandas as pd
import logging

class DataPreprocessor:
    def clean_data(self, data):
        """Remove missing values and normalize data."""
        logging.info("Cleaning data.")
        data.dropna(inplace=True)
        data.index = pd.to_datetime(data.index).tz_convert("UTC")
        return data
