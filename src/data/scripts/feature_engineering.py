# src/data/scripts/feature_engineering.py

import os
import pandas as pd
import logging

# Set up logging
logging.basicConfig(filename='../data/logs/feature_engineering.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FeatureEngineer:
    def __init__(self, input_dir='../data/processed', output_dir='../data/processed'):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def add_features(self):
        for file_name in os.listdir(self.input_dir):
            if file_name.endswith(".csv"):
                try:
                    file_path = os.path.join(self.input_dir, file_name)
                    data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
                    
                    # Check for required columns
                    if 'Close' not in data.columns:
                        logging.warning(f"{file_name} is missing 'Close' column. Skipping feature engineering.")
                        continue
                    
                    # Add features
                    data['SMA_50'] = data['Close'].rolling(window=50).mean()
                    data['SMA_200'] = data['Close'].rolling(window=200).mean()

                    # Adding RSI
                    delta = data['Close'].diff()
                    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
                    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
                    rs = gain / loss
                    data['RSI'] = 100 - (100 / (1 + rs))

                    # Save the data with features
                    output_path = os.path.join(self.output_dir, file_name)
                    data.to_csv(output_path)
                    logging.info(f"Data with features saved to {output_path}")

                except FileNotFoundError:
                    logging.error(f"File {file_name} not found in {self.input_dir}.")
                except pd.errors.ParserError:
                    logging.error(f"Error parsing {file_name}. File may be corrupted.")
                except Exception as e:
                    logging.error(f"Error processing {file_name}: {e}")

# Example usage
if __name__ == "__main__":
    engineer = FeatureEngineer()
    engineer.add_features()
