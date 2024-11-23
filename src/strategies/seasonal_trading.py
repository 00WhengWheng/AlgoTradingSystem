import pandas as pd

def seasonal_trading(prices, period="monthly"):
    """
    Seasonal Trading Strategy.
    Identifies and exploits seasonal patterns in asset prices.

    :param prices: pd.DataFrame with columns ['Date', 'Price'].
    :param period: Period for seasonality analysis ('monthly' or 'weekly').
    :return: DataFrame with seasonal averages and trading signals.
    """
    # Ensure dates are in datetime format
    prices["Date"] = pd.to_datetime(prices["Date"])

    # Extract month or week for seasonality analysis
    if period == "monthly":
        prices["Season"] = prices["Date"].dt.month
    elif period == "weekly":
        prices["Season"] = prices["Date"].dt.week
    else:
        raise ValueError("Period must be 'monthly' or 'weekly'.")

    # Calculate average returns per season
    prices["Returns"] = prices["Price"].pct_change()
    seasonal_avg = prices.groupby("Season")["Returns"].mean().reset_index()
    seasonal_avg.rename(columns={"Returns": "Average Return"}, inplace=True)

    # Merge back seasonal averages and generate signals
    prices = prices.merge(seasonal_avg, on="Season", how="left")
    prices["Signal"] = prices["Average Return"].apply(lambda x: "Buy" if x > 0 else ("Sell" if x < 0 else "Hold"))

    return prices
