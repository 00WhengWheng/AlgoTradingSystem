def currency_carry_trade(fx_rates, interest_rate_differentials):
    """
    Currency Carry Trade Strategy.
    
    :param fx_rates: pd.Series of FX rates for the currency pair.
    :param interest_rate_differentials: pd.Series of rate differentials.
    :return: Trade signals.
    """
    carry_signals = interest_rate_differentials.apply(
        lambda x: "Long High-Interest Currency" if x > 0 else "Short High-Interest Currency"
    )
    
    return pd.DataFrame({
        "FX Rate": fx_rates,
        "Rate Differential": interest_rate_differentials,
        "Signal": carry_signals
    })
