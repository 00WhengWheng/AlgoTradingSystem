from strategy_pipeline import StrategyPipeline
from output_manager import OutputManager
from visualization_manager import VisualizationManager

class HierarchicalStrategyPipelineWithVisualization(StrategyPipeline):
    """
    A hierarchical strategy pipeline with integrated visualization capabilities.
    """
    def __init__(self):
        super().__init__()
        self.hierarchy = []
        self.output_manager = OutputManager()
        self.visualization_manager = VisualizationManager()

    def define_hierarchy(self, strategy_groups):
        """
        Define the execution hierarchy for strategies.
        :param strategy_groups: List of lists, where each sublist represents a group of strategies to run sequentially.
        """
        self.hierarchy = strategy_groups

    def execute_hierarchy(self, train_size, test_size):
        """
        Execute strategies according to the defined hierarchy and manage output.
        :param train_size: Size of the training period.
        :param test_size: Size of the testing period.
        :return: Consolidated results for all strategies.
        """
        if not self.hierarchy:
            raise ValueError("Hierarchy is not defined. Use define_hierarchy() first.")

        consolidated_results = {}
        for group in self.hierarchy:
            print(f"Executing group: {group}")
            group_results = {}
            for strategy_name in group:
                print(f"Running strategy: {strategy_name}")
                strategy_instance = self.get_strategy_instance(strategy_name)

                # Walk-Forward Testing
                wft_results = self.walk_forward_test(strategy_instance, train_size, test_size)

                # Backtesting
                backtest_results = self.run_backtest(strategy_instance)

                # Consolidate results
                group_results[strategy_name] = {"Backtest": backtest_results, "Walk-Forward": wft_results}
                self.output_manager.add_result(strategy_name, group_results[strategy_name])

            consolidated_results.update(group_results)

        return consolidated_results

    def generate_visualizations(self, strategy_name, results):
        """
        Generate visualizations for a specific strategy.
        :param strategy_name: Name of the strategy.
        :param results: Results dictionary containing signals, equity, etc.
        """
        print(f"Generating visualizations for {strategy_name}...")
        equity = results["Backtest"]["Metrics"].get("Equity Curve")
        signals = results["Backtest"]["Signals"]
        prices = signals["Price"]

        self.visualization_manager.plot_equity_curve(equity, title=f"{strategy_name} - Equity Curve")
        self.visualization_manager.plot_trading_signals(prices, signals, title=f"{strategy_name} - Trading Signals")
