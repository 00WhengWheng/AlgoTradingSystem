from arch import arch_model

def volatility_clustering(returns, model='GARCH', p=1, q=1):
    """
    Analyze Volatility Clustering using GARCH models.
    
    :param returns: pd.Series of asset returns.
    :param model: Volatility model to use (default: 'GARCH').
    :param p: Order of the GARCH component.
    :param q: Order of the ARCH component.
    :return: Fitted model and volatility predictions.
    """
    garch = arch_model(returns, vol=model, p=p, q=q)
    model_fitted = garch.fit(disp="off")
    
    print("Volatility Clustering Model Summary:")
    print(model_fitted.summary())
    
    forecast = model_fitted.forecast(horizon=5)
    print("5-Day Volatility Forecast:")
    print(forecast.variance[-1:])
    
    return model_fitted, forecast
