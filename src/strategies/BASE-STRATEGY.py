# strategies/base_strategy.py

class BaseStrategy:
    def __init__(self, data, params):
        """
        Initialize the strategy with market data and strategy parameters.

        Parameters:
        - data (pd.DataFrame): Market data with price and volume information.
        - params (dict): Parameters specific to the strategy.
        """
        self.data = data
        self.params = params
        self.signals = []

    def generate_signals(self):
        """
        Abstract method to generate buy/sell signals. Each strategy will define its own logic.
        """
        raise NotImplementedError("Each strategy must implement the generate_signals method.")

    def get_signals(self):
        """
        Return the generated signals.
        """
        return self.signals
