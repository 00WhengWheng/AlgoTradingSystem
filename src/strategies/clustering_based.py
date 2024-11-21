from sklearn.cluster import KMeans

def clustering_strategy(asset_returns, n_clusters=3):
    """
    Clustering-Based Strategy.
    
    :param asset_returns: pd.DataFrame of asset returns.
    :param n_clusters: Number of clusters to identify.
    :return: Cluster labels for assets.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(asset_returns)
    
    asset_returns['Cluster'] = clusters
    
    # Analyze clusters
    cluster_means = asset_returns.groupby('Cluster').mean()
    print("Cluster Means:\n", cluster_means)
    
    return asset_returns
