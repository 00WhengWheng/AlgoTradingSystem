# src/data/scripts/preprocess_data.py

import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='../data/logs/data_preprocessing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataPreprocessor:
    def __init__(self, input_dir='../data/raw', output_dir='../data/processed'):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def preprocess(self):
        for file_name in os.listdir(self.input_dir):
            if file_name.endswith(".csv"):
                try:
                    file_path = os.path.join(self.input_dir, file_name)
                    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
                    
                    if data.empty:
                        logging.warning(f"{file_name} is empty. Skipping preprocessing.")
                        continue

                    # Drop rows with missing values
                    data = data.dropna()
                    if data.isnull().values.any():
                        logging.warning(f"{file_name} still contains NaNs after dropping missing values.")

                    # Save the cleaned data
                    output_path = os.path.join(self.output_dir, file_name)
                    data.to_csv(output_path)
                    logging.info(f"Processed data saved to {output_path}")

                except FileNotFoundError:
                    logging.error(f"File {file_name} not found in {self.input_dir}.")
                except pd.errors.EmptyDataError:
                    logging.error(f"File {file_name} is empty or corrupted.")
                except Exception as e:
                    logging.error(f"Error processing {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    preprocessor = DataPreprocessor()
    preprocessor.preprocess()
