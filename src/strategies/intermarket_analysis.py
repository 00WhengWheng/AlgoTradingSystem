def intermarket_analysis(market_data):
    """
    Intermarket Analysis Strategy.
    
    :param market_data: pd.DataFrame of prices/returns for multiple markets.
    :return: Correlation matrix and potential signals.
    """
    correlation_matrix = market_data.corr()
    print("Intermarket Correlation Matrix:")
    print(correlation_matrix)

    # Example signal: Identify inverse correlations
    inverse_correlations = correlation_matrix[(correlation_matrix < -0.7) & (correlation_matrix != 1.0)]

    return {
        "Correlation Matrix": correlation_matrix,
        "Inverse Correlations": inverse_correlations
    }
