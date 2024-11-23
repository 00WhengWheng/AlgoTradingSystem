import pandas as pd

def gamma_scalping(option_data, spot_price, delta_threshold=0.1, gamma_multiplier=2):
    """
    Gamma Scalping Strategy.
    Uses gamma to manage option positions and hedge dynamically.

    :param option_data: pd.DataFrame with columns ['Delta', 'Gamma', 'Quantity'].
    :param spot_price: Current price of the underlying asset.
    :param delta_threshold: Threshold for rebalancing delta.
    :param gamma_multiplier: Factor to scale gamma for dynamic hedging.
    :return: DataFrame with hedging adjustments and rebalancing signals.
    """
    # Calculate position delta and gamma for the portfolio
    option_data["Position Delta"] = option_data["Delta"] * option_data["Quantity"]
    option_data["Position Gamma"] = option_data["Gamma"] * option_data["Quantity"]

    # Total delta and gamma of the portfolio
    total_delta = option_data["Position Delta"].sum()
    total_gamma = option_data["Position Gamma"].sum()

    # Adjustment needed to hedge delta-neutrality considering gamma
    adjustment_needed = -total_delta / (spot_price * gamma_multiplier)

    # Generate rebalancing signal
    signal = "Rebalance" if abs(total_delta) > delta_threshold else "Hold"

    return {
        "Option Portfolio": option_data,
        "Total Delta": total_delta,
        "Total Gamma": total_gamma,
        "Adjustment Needed": adjustment_needed,
        "Signal": signal
    }
