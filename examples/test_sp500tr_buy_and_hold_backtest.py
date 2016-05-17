from qstrader.backtest.backtest import Backtest
from qstrader.execution_handler.execution_handler import IBSimulatedExecutionHandler
from qstrader.portfolio_handler.portfolio_handler import PortfolioHandler
from qstrader.position_sizer.position_sizer import TestPositionSizer
from qstrader.price_handler.yahoo_price_handler import YahooDailyBarPriceHandler
from qstrader.risk_manager.risk_manager import TestRiskManager
from qstrader import settings
from qstrader.strategy.strategy import BuyAndHoldStrategy


if __name__ == "__main__":
    tickers = ["SP500TR"]

    backtest = Backtest(
        tickers, YahooDailyBarPriceHandler, 
        BuyAndHoldStrategy, PortfolioHandler, 
        IBSimulatedExecutionHandler,
        TestPositionSizer, TestRiskManager, 
        equity=500000.00
    )
    backtest.simulate_trading()
