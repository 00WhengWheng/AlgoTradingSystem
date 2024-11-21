import pymc3 as pm
import numpy as np

def bayesian_trading_strategy(prices):
    """
    Bayesian Trading Strategy.
    
    :param prices: np.array of historical price data.
    :return: Posterior distribution of price movements.
    """
    with pm.Model() as model:
        # Define priors
        mean = pm.Normal("mean", mu=np.mean(prices), sigma=10)
        std = pm.HalfNormal("std", sigma=10)
        
        # Likelihood
        likelihood = pm.Normal("likelihood", mu=mean, sigma=std, observed=prices)
        
        # Inference
        trace = pm.sample(1000, return_inferencedata=False)
    
    pm.plot_posterior(trace)
    return trace
