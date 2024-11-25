# File: backtesting/walk_forward.py
class WalkForwardTester:
    def __init__(self, strategy, db_config, training_window, testing_window):
        self.strategy = strategy
        self.db_config = db_config
        self.training_window = training_window
        self.testing_window = testing_window

    def split_data(self, data):
        """Divide i dati in finestre di allenamento e test."""
        for i in range(0, len(data) - self.training_window - self.testing_window, self.testing_window):
            training_data = data[i:i + self.training_window]
            testing_data = data[i + self.training_window:i + self.training_window + self.testing_window]
            yield training_data, testing_data

    def simulate(self, symbol, start_date, end_date):
        """Esegue il walk-forward test."""
        data = self.fetch_data(symbol, start_date, end_date)
        results = []

        for training_data, testing_data in self.split_data(data):
            self.strategy.optimize(training_data)  # Ottimizza i parametri
            backtester = Backtester(self.strategy, self.db_config)
            metrics = backtester.simulate(testing_data)
            results.append(metrics)

        return results
