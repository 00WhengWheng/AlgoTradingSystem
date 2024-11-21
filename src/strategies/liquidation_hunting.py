def liquidation_hunting(exchange_api_url, symbol, leverage_threshold=5):
    """
    Liquidation Hunting Strategy.
    
    :param exchange_api_url: API endpoint for exchange liquidation data.
    :param symbol: Trading pair symbol (e.g., BTC/USDT).
    :param leverage_threshold: Minimum leverage to target high-risk positions.
    :return: List of positions at risk of liquidation.
    """
    response = requests.get(f"{exchange_api_url}/liquidations?symbol={symbol}").json()
    liquidations = response['data']
    
    # Filter liquidations based on leverage threshold
    risky_positions = [
        pos for pos in liquidations if pos['leverage'] >= leverage_threshold
    ]
    
    for pos in risky_positions:
        print(f"Position: {pos['position']} | Leverage: {pos['leverage']}x | Liquidation Price: {pos['liquidation_price']}")
    return risky_positions
