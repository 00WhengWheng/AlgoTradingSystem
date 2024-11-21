from filterpy.kalman import KalmanFilter
import numpy as np

def kalman_filter_hedging(asset1_prices, asset2_prices):
    """
    Dynamic Hedging Using Kalman Filter.
    
    :param asset1_prices: pd.Series of prices for the asset to hedge.
    :param asset2_prices: pd.Series of prices for the hedging instrument.
    :return: Time-varying hedge ratios.
    """
    n = len(asset1_prices)
    kf = KalmanFilter(dim_x=2, dim_z=1)
    kf.F = np.array([[1, 0], [0, 1]])  # State transition matrix
    kf.H = np.array([[1, 0]])          # Measurement function
    kf.P *= 1000                       # Covariance matrix
    kf.R = 1                           # Measurement noise
    kf.Q = np.eye(2)                   # Process noise
    
    hedge_ratios = []
    for i in range(n):
        z = np.array([[asset1_prices.iloc[i]]])  # Observation
        kf.predict()
        kf.update(z)
        hedge_ratios.append(kf.x[1, 0])  # Hedge ratio

    return pd.Series(hedge_ratios, index=asset1_prices.index, name="Hedge Ratio")
