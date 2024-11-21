import numpy as np
import pandas as pd
from .config import PSI_THRESHOLD
from .utils import setup_logger, send_alert

logger = setup_logger("DriftDetection")

class DriftDetection:
    @staticmethod
    def calculate_psi(expected, actual, bucket_count=10):
        """Calculate Population Stability Index (PSI)."""
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

    def monitor_drift(self, baseline_data, live_data):
        """Monitor data drift using PSI."""
        psi_score = self.calculate_psi(baseline_data, live_data)
        logger.info(f"PSI Score: {psi_score:.4f}")

        if psi_score > PSI_THRESHOLD:
            logger.warning(f"Drift Alert! PSI of {psi_score:.4f} exceeds threshold.")
            send_alert(f"Model drift detected! PSI: {psi_score:.4f}")
        return psi_score
