import requests

def crypto_arbitrage(exchange1_url, exchange2_url, symbol):
    """
    Crypto Arbitrage Strategy.
    
    :param exchange1_url: API endpoint for Exchange 1.
    :param exchange2_url: API endpoint for Exchange 2.
    :param symbol: Trading pair symbol (e.g., BTC/USDT).
    :return: Arbitrage opportunities.
    """
    # Fetch price data from two exchanges
    price1 = requests.get(f"{exchange1_url}/ticker/price?symbol={symbol}").json()['price']
    price2 = requests.get(f"{exchange2_url}/ticker/price?symbol={symbol}").json()['price']
    
    price1 = float(price1)
    price2 = float(price2)
    
    # Calculate arbitrage opportunity
    if price1 > price2:
        print(f"Buy on Exchange 2 at {price2} and Sell on Exchange 1 at {price1}")
    elif price2 > price1:
        print(f"Buy on Exchange 1 at {price1} and Sell on Exchange 2 at {price2}")
    else:
        print("No arbitrage opportunity found.")
