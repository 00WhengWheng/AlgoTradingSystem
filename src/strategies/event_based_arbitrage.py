import yfinance as yf

def event_based_arbitrage(symbol, event_date):
    """
    Event-Based Arbitrage Strategy.
    
    :param symbol: Stock symbol (e.g., AAPL).
    :param event_date: Date of the event in 'YYYY-MM-DD' format.
    :return: DataFrame with price movement before/after the event.
    """
    # Fetch historical data
    stock = yf.Ticker(symbol)
    hist = stock.history(period="2mo")
    
    # Analyze price movements before/after the event
    event_window = hist.loc[event_date]
    before_event = hist.loc[:event_date].iloc[-10:-1]
    after_event = hist.loc[event_date:].iloc[1:11]
    
    before_returns = before_event['Close'].pct_change()
    after_returns = after_event['Close'].pct_change()
    
    results = pd.DataFrame({
        "Before Event Returns": before_returns.values,
        "After Event Returns": after_returns.values
    })
    
    # Plot for visualization
    plt.figure(figsize=(12, 6))
    plt.plot(hist['Close'], label='Price')
    plt.axvline(event_date, color='red', linestyle='--', label='Event Date')
    plt.title(f'Event-Based Arbitrage: {symbol}')
    plt.legend()
    plt.show()
    
    return results
