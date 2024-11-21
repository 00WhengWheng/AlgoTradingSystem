def twap_trading(total_order, time_intervals):
    """
    TWAP Trading Strategy.
    
    :param total_order: Total quantity of the order to be executed.
    :param time_intervals: Number of time intervals for execution.
    :return: Order size per interval.
    """
    order_per_interval = total_order / time_intervals
    allocation = [order_per_interval] * time_intervals

    print(f"TWAP Order Allocation: {allocation}")
    return pd.DataFrame({
        "Interval": range(1, time_intervals + 1),
        "Order Allocation": allocation
    })
