
import pandas as pd

def seasonality_based_trading(prices, period="monthly"):
    prices["Date"] = pd.to_datetime(prices["Date"])
    prices["Month"] = prices["Date"].dt.month if period == "monthly" else prices["Date"].dt.week
    prices["Returns"] = prices["Price"].pct_change()
    seasonal_avg = prices.groupby("Month")["Returns"].mean().reset_index()
    seasonal_avg.rename(columns={"Returns": "Avg Returns"}, inplace=True)
    prices = prices.merge(seasonal_avg, on="Month", how="left")
    prices["Signal"] = prices["Avg Returns"].apply(lambda x: "Buy" if x > 0 else ("Sell" if x < 0 else "Hold"))
    return prices
