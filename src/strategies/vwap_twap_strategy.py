
import pandas as pd

def vwap_twap_strategy(prices, volumes, strategy_type="VWAP", total_order=1000, time_intervals=10):
    if strategy_type == "VWAP":
        vwap = (prices * volumes).sum() / volumes.sum()
        allocation = (volumes / volumes.sum()) * total_order
        return pd.DataFrame({"Price": prices, "Volume": volumes, "VWAP Order Allocation": allocation})
    elif strategy_type == "TWAP":
        order_per_interval = total_order / time_intervals
        allocation = [order_per_interval] * time_intervals
        return pd.DataFrame({"Interval": range(1, time_intervals + 1), "TWAP Order Allocation": allocation})
    else:
        raise ValueError("Invalid strategy type. Use 'VWAP' or 'TWAP'.")
