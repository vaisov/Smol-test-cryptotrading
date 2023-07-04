```python
import unittest
from src.strategy_backtester import backtest_strategy
from src.strategy import Strategy
from src.pair import Pair

class TestStrategyBacktester(unittest.TestCase):

    def setUp(self):
        self.strategy = Strategy('Test Strategy', 'This is a test strategy')
        self.pair = Pair('BTC', 'ETH')

    def test_backtest_strategy(self):
        result = backtest_strategy(self.strategy, self.pair)
        self.assertIsInstance(result, float, "The result should be a float representing the profitability")

if __name__ == '__main__':
    unittest.main()
```