from statsmodels.tsa.stattools import coint

def statistical_arbitrage(pair_prices):
    """
    Statistical Arbitrage Strategy using cointegration.
    
    :param pair_prices: DataFrame with prices of two assets.
    :return: Trading signals based on z-scores.
    """
    spread = pair_prices.iloc[:, 0] - pair_prices.iloc[:, 1]
    mean_spread = spread.mean()
    std_spread = spread.std()
    z_scores = (spread - mean_spread) / std_spread

    signals = z_scores.apply(
        lambda x: "Buy Spread" if x > 2 else "Sell Spread" if x < -2 else "Hold"
    )

    return pd.DataFrame({
        "Spread": spread,
        "Z-Score": z_scores,
        "Signal": signals
    })
