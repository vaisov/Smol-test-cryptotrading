```python
import pandas as pd
from src.strategy import Strategy
from src.pair import Pair
from src.binance_api import BinanceAPI

class StrategyBacktester:
    def __init__(self, strategies, selected_pair):
        self.strategies = strategies
        self.selected_pair = selected_pair
        self.api = BinanceAPI()
        self.results = []

    def backtest_strategy(self, strategy):
        data = self.api.get_historical_data(self.selected_pair)
        profit, trades = strategy.run(data)
        return profit, trades

    def backtest_all_strategies(self):
        for strategy in self.strategies:
            profit, trades = self.backtest_strategy(strategy)
            self.results.append({
                'strategy': strategy.name,
                'profit': profit,
                'trades': trades
            })

    def get_results(self):
        return pd.DataFrame(self.results)

if __name__ == "__main__":
    strategies = Strategy().gather_strategies()
    selected_pair = Pair().get_selected_pair()
    backtester = StrategyBacktester(strategies, selected_pair)
    backtester.backtest_all_strategies()
    print(backtester.get_results())
```