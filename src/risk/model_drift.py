import numpy as np
import pandas as pd
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Define PSI function
def calculate_psi(expected, actual, bucket_count=10):
    """Calculate the Population Stability Index (PSI)"""
    def get_bins(data, buckets):
        return np.histogram(data, bins=buckets)[0]

    # Normalize to proportions
    expected_bins = get_bins(expected, bucket_count) / len(expected)
    actual_bins = get_bins(actual, bucket_count) / len(actual)
    
    # Avoid division by zero
    expected_bins = np.where(expected_bins == 0, 0.0001, expected_bins)
    actual_bins = np.where(actual_bins == 0, 0.0001, actual_bins)
    
    # Calculate PSI
    psi_values = (actual_bins - expected_bins) * np.log(actual_bins / expected_bins)
    return np.sum(psi_values)

# Simulate data
baseline_data = np.random.normal(0, 1, 1000)  # Baseline distribution
live_data = np.random.normal(0.5, 1.2, 1000)  # Simulated drift

# Calculate PSI
psi_score = calculate_psi(baseline_data, live_data)
logging.info(f"PSI Score: {psi_score:.4f}")

# Set threshold for drift
PSI_THRESHOLD = 0.2
if psi_score > PSI_THRESHOLD:
    logging.warning(f"Drift Alert! PSI of {psi_score:.4f} exceeds threshold.")

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Create a drift report
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=pd.DataFrame(baseline_data, columns=["feature"]),
           current_data=pd.DataFrame(live_data, columns=["feature"]))
report.save_html("drift_report.html")
