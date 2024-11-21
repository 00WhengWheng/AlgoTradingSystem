def global_macro_strategy(economic_data, asset_prices):
    """
    Global Macro Strategy.
    
    :param economic_data: pd.DataFrame of macroeconomic indicators.
    :param asset_prices: pd.DataFrame of global asset prices.
    :return: Trade signals based on economic trends.
    """
    # Example: GDP growth vs. equity index performance
    gdp_growth = economic_data['GDP Growth']
    equity_returns = asset_prices['Equity Index'].pct_change()
    
    signals = gdp_growth.apply(
        lambda x: "Buy Equities" if x > 0.02 else "Sell Equities" if x < -0.02 else "Hold"
    )
    
    return pd.DataFrame({
        "GDP Growth": gdp_growth,
        "Equity Returns": equity_returns,
        "Signal": signals
    })
