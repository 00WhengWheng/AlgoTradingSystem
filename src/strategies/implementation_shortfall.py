def implementation_shortfall_optimization(order_book, target_price, total_order, max_slippage=0.005):
    """
    Implementation Shortfall Optimization Strategy.
    
    :param order_book: DataFrame with bid/ask prices and volumes.
    :param target_price: Desired execution price.
    :param total_order: Total quantity of the order to be executed.
    :param max_slippage: Maximum allowable slippage as a fraction of the target price.
    :return: Executed order size and cost.
    """
    executed_volume = 0
    executed_cost = 0
    
    for _, row in order_book.iterrows():
        price, volume = row['price'], row['volume']
        if abs(price - target_price) / target_price <= max_slippage:
            trade_volume = min(volume, total_order - executed_volume)
            executed_volume += trade_volume
            executed_cost += trade_volume * price
            if executed_volume >= total_order:
                break

    avg_execution_price = executed_cost / executed_volume if executed_volume > 0 else None
    print(f"Executed Volume: {executed_volume}, Avg Execution Price: {avg_execution_price:.2f}")
    return {"Executed Volume": executed_volume, "Avg Execution Price": avg_execution_price}
