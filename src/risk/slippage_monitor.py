import time
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
MAX_SLIPPAGE_PERCENTAGE = 0.5  # Example threshold
MAX_LATENCY_MS = 100  # Example latency threshold

# Function to simulate trade execution
def execute_trade(expected_price):
    # Simulate a delay
    time.sleep(0.05)  # 50ms
    actual_price = expected_price * (1 + (0.001 * (2 * (0.5 - time.time() % 1))))  # Simulating market impact
    return actual_price, time.time()

# Function to monitor slippage
def monitor_execution(expected_price):
    start_time = time.time()
    actual_price, execution_time = execute_trade(expected_price)
    end_time = time.time()
    
    # Calculate slippage and latency
    slippage_percentage = ((actual_price - expected_price) / expected_price) * 100
    latency_ms = (end_time - start_time) * 1000
    
    # Log results
    logging.info(f"Expected Price: {expected_price}, Actual Price: {actual_price:.2f}, Slippage: {slippage_percentage:.2f}%, Latency: {latency_ms:.2f}ms")
    
    # Trigger alerts
    if slippage_percentage > MAX_SLIPPAGE_PERCENTAGE:
        logging.warning(f"Slippage Alert! Slippage of {slippage_percentage:.2f}% exceeds threshold.")
    if latency_ms > MAX_LATENCY_MS:
        logging.warning(f"Latency Alert! Latency of {latency_ms:.2f}ms exceeds threshold.")

# Simulate monitoring trades
for i in range(10):
    monitor_execution(expected_price=100 + i)  # Simulating trades with varying prices
