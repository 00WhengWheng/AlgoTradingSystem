def order_flow_analysis(order_book, volume_threshold=1000):
    """
    Order Flow Analysis Strategy.
    
    :param order_book: DataFrame with order flow data (e.g., buy/sell volume).
    :param volume_threshold: Minimum volume for significant order imbalance.
    :return: Order flow imbalance and trading signals.
    """
    order_flow_imbalance = order_book['buy_volume'] - order_book['sell_volume']
    
    signals = ["Buy" if imbalance > volume_threshold else "Sell" if imbalance < -volume_threshold else "Hold"
               for imbalance in order_flow_imbalance]
    
    return pd.DataFrame({
        "Buy Volume": order_book['buy_volume'],
        "Sell Volume": order_book['sell_volume'],
        "Imbalance": order_flow_imbalance,
        "Signal": signals
    })
