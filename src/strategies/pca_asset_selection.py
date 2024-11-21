from sklearn.decomposition import PCA

def pca_asset_selection(returns, n_components=2):
    """
    Principal Component Analysis for Asset Selection.
    
    :param returns: DataFrame of historical returns for multiple assets.
    :param n_components: Number of principal components to retain.
    :return: PCA results and explained variance ratios.
    """
    pca = PCA(n_components=n_components)
    pca.fit(returns)

    explained_variance = pca.explained_variance_ratio_
    components = pca.components_

    print(f"Explained Variance Ratios: {explained_variance}")
    print(f"Principal Components:\n{components}")

    return {
        "Explained Variance Ratios": explained_variance,
        "Principal Components": components
    }
