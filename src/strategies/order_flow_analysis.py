
import pandas as pd

def order_flow_analysis(order_book, depth=5):
    top_levels = order_book.iloc[:depth]
    ofi = (top_levels["Bid Size"].sum() - top_levels["Ask Size"].sum()) / (
        top_levels["Bid Size"].sum() + top_levels["Ask Size"].sum()
    )
    signal = "Buy" if ofi > 0 else "Sell" if ofi < 0 else "Neutral"
    return {
        "Top Levels": top_levels,
        "Order Flow Imbalance": ofi,
        "Signal": signal
    }
