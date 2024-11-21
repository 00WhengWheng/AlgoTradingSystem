from sklearn.cluster import KMeans

def asset_clustering(data, n_clusters=3):
    """
    Unsupervised Learning for Asset Clustering.
    
    :param data: pd.DataFrame of historical returns or other asset features.
    :param n_clusters: Number of clusters to create.
    :return: DataFrame with cluster assignments.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    
    data['Cluster'] = clusters
    print("Asset Clusters:")
    print(data.groupby('Cluster').mean())
    
    return data
