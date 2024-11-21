def copy_trading(api_url, top_trader_id, allocation_amount):
    """
    Copy Trading Strategy.
    
    :param api_url: API endpoint of the social trading platform.
    :param top_trader_id: ID of the top trader to copy trades from.
    :param allocation_amount: Amount to allocate per trade.
    :return: Executed trades.
    """
    # Fetch top trader's live trades
    trades_response = requests.get(f"{api_url}/traders/{top_trader_id}/trades").json()
    trades = trades_response['trades']
    
    executed_trades = []
    
    for trade in trades:
        # Execute the trade (dummy implementation)
        print(f"Copying Trade: {trade['asset']} | Action: {trade['action']} | Amount: {allocation_amount}")
        executed_trades.append({
            'Asset': trade['asset'],
            'Action': trade['action'],
            'Amount': allocation_amount
        })
    
    return pd.DataFrame(executed_trades)
