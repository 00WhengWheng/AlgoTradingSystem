class BacktestingPipeline:
    """
    A pipeline for executing backtesting on all strategies registered in the strategy pipeline.
    """
    def __init__(self, strategy_pipeline):
        """
        Initialize the backtesting pipeline.
        :param strategy_pipeline: Instance of the strategy pipeline containing registered strategies.
        """
        self.strategy_pipeline = strategy_pipeline

    def execute(self, data):
        """
        Execute backtesting for all registered strategies.
        :param data: Historical data for backtesting (pd.DataFrame).
        :return: Consolidated backtesting results for all strategies.
        """
        results = {}
        for strategy_name in self.strategy_pipeline.list_strategies():
            print(f"Running backtest for strategy: {strategy_name}")
            
            # Get strategy instance and parameters
            strategy_config = self.strategy_pipeline.strategies[strategy_name]
            strategy_instance = strategy_config["class"](params=strategy_config.get("params", {}))
            
            # Train and execute strategy
            strategy_instance.train(data)
            results[strategy_name] = strategy_instance.execute(data)
        
        return results
