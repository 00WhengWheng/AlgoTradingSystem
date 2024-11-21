import time
from .config import MAX_SLIPPAGE_PERCENTAGE, MAX_LATENCY_MS
from .utils import setup_logger, send_alert

logger = setup_logger("SlippageMonitor")

class SlippageMonitor:
    def __init__(self):
        self.trades = []

    def execute_trade(self, expected_price):
        """Simulate trade execution."""
        time.sleep(0.05)  # Simulate latency
        actual_price = expected_price * (1 + 0.001 * (2 * (0.5 - time.time() % 1)))
        return actual_price, time.time()

    def monitor_execution(self, expected_price):
        """Monitor trade execution and calculate slippage."""
        start_time = time.time()
        actual_price, execution_time = self.execute_trade(expected_price)
        end_time = time.time()

        # Calculate metrics
        slippage_percentage = ((actual_price - expected_price) / expected_price) * 100
        latency_ms = (end_time - start_time) * 1000

        # Log results
        logger.info(f"Expected: {expected_price}, Actual: {actual_price:.2f}, "
                    f"Slippage: {slippage_percentage:.2f}%, Latency: {latency_ms:.2f}ms")

        # Trigger alerts
        if slippage_percentage > MAX_SLIPPAGE_PERCENTAGE:
            logger.warning(f"Slippage Alert! {slippage_percentage:.2f}% exceeds threshold.")
            send_alert(f"Slippage exceeded: {slippage_percentage:.2f}%")
        if latency_ms > MAX_LATENCY_MS:
            logger.warning(f"Latency Alert! {latency_ms:.2f}ms exceeds threshold.")
            send_alert(f"Latency exceeded: {latency_ms:.2f}ms")

        # Store the trade
        self.trades.append({"expected_price": expected_price, "actual_price": actual_price,
                            "slippage": slippage_percentage, "latency": latency_ms})
