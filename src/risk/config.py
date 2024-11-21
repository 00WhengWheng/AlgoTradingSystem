# Slippage Monitor Config
MAX_SLIPPAGE_PERCENTAGE = 0.5  # Example threshold
MAX_LATENCY_MS = 100  # Example threshold in milliseconds

# Drift Detection Config
PSI_THRESHOLD = 0.2  # Threshold for Population Stability Index

# Logging Config
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"

# Path: src/risk/handle_slippage_monitor.py


from src.risk.handle_slippage_monitor import SlippageMonitor
from src.risk.drift_detection import DriftDetection
import numpy as np

# Handle Slippage Monitoring
handle_slippage_monitor = SlippageMonitor()
handle_slippage_monitor.monitor_execution(expected_price=100)

# Drift Detection
baseline_data = np.random.normal(0, 1, 1000)
live_data = np.random.normal(0.5, 1.2, 1000)
drift_detector = DriftDetection()
drift_detector.monitor_drift(baseline_data, live_data)
