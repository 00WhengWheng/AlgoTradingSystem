import QuantLib as ql

def fixed_income_arbitrage(bond1_price, bond2_price, bond1_yield, bond2_yield):
    """
    Fixed-Income Arbitrage Strategy.
    
    :param bond1_price: Price of Bond 1.
    :param bond2_price: Price of Bond 2.
    :param bond1_yield: Yield of Bond 1.
    :param bond2_yield: Yield of Bond 2.
    :return: Arbitrage signal based on yield spread.
    """
    yield_spread = bond1_yield - bond2_yield

    if yield_spread > 0.5:
        signal = "Sell Bond 1, Buy Bond 2"
    elif yield_spread < -0.5:
        signal = "Buy Bond 1, Sell Bond 2"
    else:
        signal = "Hold"

    return {
        "Yield Spread": yield_spread,
        "Signal": signal
    }
