
import pandas as pd

def volume_profile_analysis(prices, volumes, bins=10):
    price_bins = pd.cut(prices, bins=bins, right=False)
    volume_profile = volumes.groupby(price_bins).sum().reset_index()
    volume_profile.columns = ["Price Range", "Total Volume"]
    max_volume_bin = volume_profile.loc[volume_profile["Total Volume"].idxmax()]
    high_activity_levels = volume_profile[volume_profile["Total Volume"] > volume_profile["Total Volume"].mean()]
    return {
        "Volume Profile": volume_profile,
        "Key Level (Max Volume)": max_volume_bin,
        "High Activity Levels": high_activity_levels
    }
