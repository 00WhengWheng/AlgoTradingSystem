def calendar_spread_pricing(spot_price, long_expiration, short_expiration, volatility, interest_rate):
    """
    Calendar Spread Pricing Strategy.
    
    :param spot_price: Current price of the underlying asset.
    :param long_expiration: Expiration date for the long option.
    :param short_expiration: Expiration date for the short option.
    :param volatility: Annualized volatility of the underlying asset.
    :param interest_rate: Risk-free interest rate.
    :return: Calendar spread price differential.
    """
    # Set up QuantLib variables
    spot = ql.SimpleQuote(spot_price)
    volatility_handle = ql.BlackConstantVol(0, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(volatility)), ql.Actual360())
    risk_free_curve = ql.YieldTermStructureHandle(ql.FlatForward(0, ql.NullCalendar(), ql.QuoteHandle(ql.SimpleQuote(interest_rate)), ql.Actual360()))

    # Define pricing engine
    engine = ql.AnalyticEuropeanEngine(ql.BlackScholesProcess(ql.QuoteHandle(spot), risk_free_curve, volatility_handle))
    
    # Set up options
    option_long = ql.EuropeanOption(ql.PlainVanillaPayoff(ql.Option.Call, spot_price), long_expiration)
    option_long.setPricingEngine(engine)
    
    option_short = ql.EuropeanOption(ql.PlainVanillaPayoff(ql.Option.Call, spot_price), short_expiration)
    option_short.setPricingEngine(engine)
    
    # Calculate prices
    long_price = option_long.NPV()
    short_price = option_short.NPV()
    
    spread_price = long_price - short_price
    print(f"Calendar Spread Price: {spread_price:.2f}")
    return spread_price
