
import pandas as pd

def event_driven_trading_strategy(events, prices, impact_threshold=0.05):
    events["Date"] = pd.to_datetime(events["Date"])
    prices.index = pd.to_datetime(prices.index)
    events = events.set_index("Date")
    merged_data = prices.to_frame(name="Price").merge(events, left_index=True, right_index=True, how="left")
    merged_data["Impact"] = merged_data["Impact"].fillna(0)
    merged_data["Signal"] = merged_data["Impact"].apply(lambda x: "Buy" if x > impact_threshold else ("Sell" if x < -impact_threshold else "Hold"))
    return merged_data
