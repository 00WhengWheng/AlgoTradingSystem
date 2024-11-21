import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

def seasonal_trading_strategy(data, frequency='M'):
    """
    Seasonal Trading Strategy based on historical patterns.
    
    :param data: pd.DataFrame with 'Date' and 'Price' columns.
    :param frequency: Frequency for seasonal analysis ('M' for monthly, 'Q' for quarterly).
    :return: DataFrame with seasonal average returns.
    """
    data['Month'] = data['Date'].dt.to_period(frequency).dt.strftime('%b')
    seasonal_avg = data.groupby('Month')['Price'].mean()
    
    # Plot seasonal trends
    plt.figure(figsize=(10, 6))
    seasonal_avg.plot(kind='bar', color='skyblue')
    plt.title('Seasonal Average Prices')
    plt.xlabel('Period')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    plt.show()
    
    return seasonal_avg


def seasonal_trading(prices, period='monthly'):
    """
    Seasonal Trading Strategy.
    
    :param prices: pd.DataFrame with columns ['Date', 'Price'].
    :param period: 'monthly' or 'seasonal' segmentation.
    :return: Seasonal performance statistics.
    """
    df = prices.copy()
    df['Month'] = df['Date'].dt.month if period == 'monthly' else df['Date'].dt.quarter
    seasonal_performance = df.groupby('Month')['Price'].mean()
    
    # Plot seasonal trends
    seasonal_performance.plot(kind='bar', figsize=(10, 6), title=f"{period.capitalize()} Seasonal Performance")
    plt.ylabel("Average Price")
    plt.show()
    
    return seasonal_performance
