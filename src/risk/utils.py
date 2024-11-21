import logging

# Setup Logger
def setup_logger(name, level="INFO"):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger

# Alert Function
def send_alert(message):
    # Example: integrate with email, Slack, or another alerting system
    print(f"ALERT: {message}")
