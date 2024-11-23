
import pandas as pd

def momentum_trading_strategy(prices, window=14):
    momentum = prices.diff(window)
    signals = momentum.apply(lambda x: 'Buy' if x > 0 else ('Sell' if x < 0 else 'Hold'))
    return pd.DataFrame({"Price": prices, "Momentum": momentum, "Signal": signals})
