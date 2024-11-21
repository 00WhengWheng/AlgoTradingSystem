def calendar_arbitrage(event_dates, price_data):
    """
    Calendar Arbitrage Strategy based on event-driven price patterns.
    
    :param event_dates: List of dates for key calendar events.
    :param price_data: pd.DataFrame with 'Date' and 'Price' columns.
    :return: DataFrame with price changes around events.
    """
    price_data['Event'] = price_data['Date'].isin(event_dates)
    price_data['Price Change'] = price_data['Price'].pct_change()
    event_changes = price_data.loc[price_data['Event'], ['Date', 'Price Change']]
    
    print("Price Changes Around Events:")
    print(event_changes)
    
    return event_changes


def calendar_arbitrage_strategy(prices, event_dates, window=5):
    """
    Calendar Arbitrage Strategy.
    
    :param prices: pd.Series of price data.
    :param event_dates: List of event dates.
    :param window: Number of days before and after the event to analyze.
    :return: Average price change around events.
    """
    event_analysis = []
    for event in event_dates:
        pre_event = prices.loc[:event].iloc[-window:]
        post_event = prices.loc[event:].iloc[:window]
        
        avg_pre_change = pre_event.pct_change().mean()
        avg_post_change = post_event.pct_change().mean()
        
        event_analysis.append({
            "Event": event,
            "Avg Pre-Event Change": avg_pre_change,
            "Avg Post-Event Change": avg_post_change
        })
    
    return pd.DataFrame(event_analysis)
