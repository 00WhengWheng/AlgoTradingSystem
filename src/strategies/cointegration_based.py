def cointegration_trading(asset1, asset2):
    """
    Cointegration-Based Trading Strategy.
    
    :param asset1: Series of prices for asset 1.
    :param asset2: Series of prices for asset 2.
    :return: Cointegration test results and potential trading signals.
    """
    score, p_value, _ = coint(asset1, asset2)

    if p_value < 0.05:
        print("Cointegration detected. Pair is suitable for trading.")
        return {"Score": score, "P-Value": p_value}
    else:
        print("No cointegration detected.")
        return {"Score": score, "P-Value": p_value}
