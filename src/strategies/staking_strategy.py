def staking_strategy(token_name, annual_rewards, inflation_rate, fees):
    """
    Staking Strategy to calculate net yield.
    
    :param token_name: Name of the staked token (e.g., ETH, SOL).
    :param annual_rewards: Annual staking rewards as a percentage (e.g., 5% = 0.05).
    :param inflation_rate: Annual token inflation rate as a percentage.
    :param fees: Total fees as a percentage (e.g., 1% = 0.01).
    :return: Net yield after inflation and fees.
    """
    net_yield = annual_rewards - inflation_rate - fees
    print(f"Net Staking Yield for {token_name}: {net_yield * 100:.2f}%")
    return net_yield
