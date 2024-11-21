def tokenomic_analysis(token_name, supply_growth, burn_rate, staking_yield):
    """
    Tokenomic Strategy to assess token health.
    
    :param token_name: Name of the token (e.g., ETH, MATIC).
    :param supply_growth: Annual supply growth as a percentage.
    :param burn_rate: Annual burn rate as a percentage.
    :param staking_yield: Annual staking yield as a percentage.
    :return: Analysis of token's tokenomics.
    """
    net_inflation = supply_growth - burn_rate
    net_yield = staking_yield - net_inflation
    
    print(f"Token: {token_name}")
    print(f"Supply Growth: {supply_growth * 100:.2f}%")
    print(f"Burn Rate: {burn_rate * 100:.2f}%")
    print(f"Net Yield: {net_yield * 100:.2f}%")
    return {
        "Token": token_name,
        "Supply Growth": supply_growth,
        "Burn Rate": burn_rate,
        "Net Yield": net_yield
    }
