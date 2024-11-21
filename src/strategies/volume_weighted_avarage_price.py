def vwap_trading(prices, volumes, total_order=1000):
    """
    VWAP Trading Strategy.
    
    :param prices: pd.Series of intraday prices.
    :param volumes: pd.Series of intraday volumes.
    :param total_order: Total quantity of the order to be executed.
    :return: Allocation of order volume for each time interval.
    """
    vwap = (prices * volumes).sum() / volumes.sum()
    allocation = (volumes / volumes.sum()) * total_order

    print(f"VWAP: {vwap:.2f}")
    print("Order Allocation by Time Interval:")
    print(allocation)
    
    return pd.DataFrame({
        "Price": prices,
        "Volume": volumes,
        "Order Allocation": allocation
    })
