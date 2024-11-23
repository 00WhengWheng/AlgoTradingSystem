import pandas as pd

class OutputManager:
    """
    Manages the consolidation and export of strategy results.
    """
    def __init__(self):
        self.results = {}

    def add_result(self, strategy_name, result):
        self.results[strategy_name] = result

    def consolidate_metrics(self):
        metrics = []
        for strategy_name, result in self.results.items():
            metrics.append({
                "Strategy": strategy_name,
                "Cumulative Return": result["Metrics"]["Cumulative Return"],
                "Sharpe Ratio": result["Metrics"]["Sharpe Ratio"],
                "Max Drawdown": result["Metrics"].get("Max Drawdown", "N/A")
            })
        return pd.DataFrame(metrics)

    def export_to_csv(self, folder_path):
        consolidated_metrics = self.consolidate_metrics()
        consolidated_metrics.to_csv(f"{folder_path}/consolidated_metrics.csv", index=False)
        for strategy_name, result in self.results.items():
            signals = result["Signals"]
            signals.to_csv(f"{folder_path}/{strategy_name}_signals.csv", index=False)

    def display_results(self):
        consolidated_metrics = self.consolidate_metrics()
        print(consolidated_metrics)
