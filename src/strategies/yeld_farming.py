from web3 import Web3

def yield_farming_opportunities(protocol_api_url):
    """
    Yield Farming Strategy to find the best APY opportunities.
    
    :param protocol_api_url: API endpoint for the DeFi protocol.
    :return: List of high-APY pools.
    """
    response = requests.get(f"{protocol_api_url}/pools").json()
    pools = response['data']
    
    # Filter pools with APY > threshold
    high_apy_pools = [pool for pool in pools if pool['apy'] > 0.15]
    
    for pool in high_apy_pools:
        print(f"Pool: {pool['name']} | APY: {pool['apy'] * 100:.2f}%")
