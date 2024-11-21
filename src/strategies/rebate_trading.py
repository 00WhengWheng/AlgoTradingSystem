def rebate_trading(order_book, spread_threshold=0.001):
    """
    Rebate Trading Strategy.
    
    :param order_book: Dict with 'bids' and 'asks' from the order book.
    :param spread_threshold: Minimum spread to place limit orders.
    :return: Suggested bid/ask prices for rebate trading.
    """
    best_bid = float(order_book['bids'][0][0])
    best_ask = float(order_book['asks'][0][0])
    spread = best_ask - best_bid
    
    if spread > spread_threshold:
        bid_price = best_bid + (spread / 4)  # Slightly above best bid
        ask_price = best_ask - (spread / 4)  # Slightly below best ask
        print(f"Place Limit Orders: Buy at {bid_price:.2f}, Sell at {ask_price:.2f}")
        return {"Bid Price": bid_price, "Ask Price": ask_price}
    else:
        print("Spread too narrow for profitable rebate trading.")
        return None
