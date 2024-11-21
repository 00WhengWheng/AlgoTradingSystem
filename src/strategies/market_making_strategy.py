def market_making(order_book, spread_threshold=0.01):
    """
    Market Making Strategy.
    
    :param order_book: DataFrame with bid and ask prices.
    :param spread_threshold: Minimum spread for market making.
    :return: Suggested bid and ask prices for placement.
    """
    best_bid = order_book['bids'][0]
    best_ask = order_book['asks'][0]
    spread = best_ask - best_bid

    if spread > spread_threshold:
        bid_price = best_bid + (spread / 3)
        ask_price = best_ask - (spread / 3)
        print(f"Place orders: Bid at {bid_price}, Ask at {ask_price}")
        return {"Bid Price": bid_price, "Ask Price": ask_price}
    else:
        print("Spread too narrow for profitable market making.")
        return None
