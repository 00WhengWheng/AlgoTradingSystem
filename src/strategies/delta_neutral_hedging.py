
import pandas as pd

def delta_neutral_hedging(option_data, spot_price, delta_threshold=0.1):
    option_data["Position Delta"] = option_data["Delta"] * option_data["Quantity"]
    total_delta = option_data["Position Delta"].sum()
    adjustment_needed = -total_delta / spot_price
    if abs(total_delta) > delta_threshold:
        signal = "Rebalance"
    else:
        signal = "Hold"
    return {
        "Option Portfolio": option_data,
        "Total Delta": total_delta,
        "Adjustment Needed": adjustment_needed,
        "Signal": signal
    }
