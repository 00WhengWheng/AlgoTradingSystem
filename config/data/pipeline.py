from optimization import ParameterOptimizer
from backtesting import Backtester
from database import fetch_financial_data, save_optimized_parameters
from reporting import generate_pdf_report

class TradingPipeline:
    """
    Automates the optimization → backtesting → report cycle for multiple tickers.
    """
    def __init__(self, strategy_name, tickers, parameter_grid, strategy_function):
        """
        Initialize the pipeline.
        :param strategy_name: Name of the strategy.
        :param tickers: List of tickers for the data.
        :param parameter_grid: Grid of parameters for optimization.
        :param strategy_function: Function implementing the strategy.
        """
        self.strategy_name = strategy_name
        self.tickers = tickers
        self.parameter_grid = parameter_grid
        self.strategy_function = strategy_function

    def run_pipeline_for_ticker(self, ticker):
        """
        Run the pipeline for a single ticker.
        :param ticker: Ticker symbol.
        """
        print(f"Starting pipeline for {self.strategy_name} on {ticker}.")
        data = fetch_financial_data(ticker)

        # Step 1: Optimization
        optimizer = ParameterOptimizer(data, self.parameter_grid, self.strategy_function)
        results = optimizer.optimize()
        best_params = results.iloc[0].to_dict()
        save_optimized_parameters(self.strategy_name, best_params)

        # Step 2: Backtesting
        backtester = Backtester(data, self.strategy_name)
        performance = backtester.run_backtest()

        # Step 3: Generate Report
        report_data = {
            "Ticker": ticker,
            "Strategy": self.strategy_name,
            "Parameters": best_params,
            "Performance": performance
        }
        generate_pdf_report(self.strategy_name, report_data)
        print(f"Pipeline completed for {self.strategy_name} on {ticker}.")

    def run(self):
        """
        Run the pipeline for all tickers.
        """
        for ticker in self.tickers:
            try:
                self.run_pipeline_for_ticker(ticker)
            except Exception as e:
                print(f"Error processing {ticker}: {e}")
