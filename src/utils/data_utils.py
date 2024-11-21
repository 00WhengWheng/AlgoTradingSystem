# src/utils/data_utils.py

import pandas as pd

def handle_missing_values(df, method='drop'):
    """
    Handles missing values in a DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - method (str): Method to handle missing values ('drop' or 'fill').
    """
    if method == 'drop':
        return df.dropna()
    elif method == 'fill':
        return df.fillna(method='ffill')
    else:
        raise ValueError("Method must be 'drop' or 'fill'")

def calculate_rolling_mean(df, column, window=20):
    """
    Calculates a rolling mean for a specified column.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - column (str): The column name for which to calculate the rolling mean.
    - window (int): The rolling window size.
    """
    return df[column].rolling(window=window).mean()
