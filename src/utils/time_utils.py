# src/utils/time_utils.py

import pandas as pd

def convert_to_datetime(df, column):
    """
    Converts a column to datetime format.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name to convert.
    """
    df[column] = pd.to_datetime(df[column])
    return df

def resample_data(df, freq='D'):
    """
    Resamples data to a specified frequency.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame with a datetime index.
    - freq (str): Resampling frequency (e.g., 'D' for daily, 'H' for hourly).
    """
    return df.resample(freq).ffill()
