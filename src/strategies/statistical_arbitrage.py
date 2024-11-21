from sklearn.decomposition import PCA

def statistical_arbitrage_strategy(price_data):
    """
    Statistical Arbitrage Strategy using PCA.
    
    :param price_data: pd.DataFrame of price data for multiple securities.
    :return: Signal DataFrame with mispricing signals.
    """
    pca = PCA(n_components=1)  # Extract first principal component
    price_data['PCA_Component'] = pca.fit_transform(price_data)
    
    # Calculate residuals
    reconstructed = pca.inverse_transform(price_data['PCA_Component'].values.reshape(-1, 1))
    residuals = price_data.values - reconstructed
    
    # Compute z-scores for residuals
    z_scores = (residuals - residuals.mean(axis=0)) / residuals.std(axis=0)
    signals = np.where(z_scores > 2, 'Sell', np.where(z_scores < -2, 'Buy', 'Hold'))
    
    # Convert signals into a DataFrame
    signal_df = pd.DataFrame(signals, columns=price_data.columns, index=price_data.index)
    return signal_df
