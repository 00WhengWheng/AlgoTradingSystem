
import pandas as pd

def volatility_based_trading_strategy(prices, window=14, threshold=0.02):
    returns = prices.pct_change()
    volatility = returns.rolling(window=window).std()
    signals = volatility.apply(lambda x: "Buy" if x > threshold else ("Sell" if x < -threshold else "Hold"))
    return pd.DataFrame({"Price": prices, "Volatility": volatility, "Signal": signals})
